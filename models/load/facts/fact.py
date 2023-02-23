import pandas as pd
from collections import namedtuple
from models.transform.dataframe.dataframe_handle import DataframeHandle
from ..table import Table
from dotenv import load_dotenv
import os

load_dotenv()

class Fact(Table):

    stg_table = namedtuple('stg_table', ['tb_name', 'alias'])
    fact_dataframe = pd.DataFrame()
    fact_columns = {}
    fact_bks = {}
    fact_fks = {}
    schema = os.environ["db_schema_dw"]
    stage_schema = os.environ["db_schema_stage"]
    df_handle = DataframeHandle()

    def create_query_select_fact(self):
        query = "select distinct "

        for col in self.fact_columns:
            if col['table'] is None:
                pass
            elif isinstance(col['column'], str):
                query += f"{col['tb_alias']}.{col['column']} as {col['alias']}, "
            else:
                query += 'case '
                count = 1
                for col2 in col['column']:
                    if count < len(col['column']):
                        query += f"when {col['table']}.{col2} is not null then {col['table']}.{col2}"
                    else:
                        query += f" else {col['table']}.{col2}"
                    count += 1
                query += f" end as {col['alias']}, "

        query = query[:-2]
        query += f" from {self.stage_schema}.{self.stg_table.tb_name} as {self.stg_table.alias}"

        for join in self.fact_fks:
            query += f" {join['type']} join {join['schema']}.{join['table']} as {join['tb_alias']} on"
            query += f" {join['tb_alias']}.{join['bkey']}::text = {self.stg_table.alias}.{join['bkeyf']}"
            query += f" and {join['tb_alias']}.cd_cliente::text = {self.stg_table.alias}.cd_cliente"
            query += f" and {self.stg_table.alias}.dt_criacao between {join['tb_alias']}.dt_criacao and {join['tb_alias']}.dt_atualizacao"

        return query

    def create_query_insert(self, dataframe):

        query = f"insert into {self.table_name} ("

        for col in self.stage_cols:
            query += f"{col['alias']}, "
        query = query[:-2]
        query += ") values "

        for index1 in dataframe.index:
            data = dataframe.iloc[index1].copy()
            query += "("
            for index2 in data.index:
                if data[index2] is None or pd.isna(data[index2]):
                    value = "null"
                else:
                    value = data[index2]
                query += f"{value}, " if isinstance(value, int) or isinstance(value, float) or value == "null" else f"'{value}', "
            query = query[:-2]
            query += "), "
        query = query[:-2]

        return query
    def insert_data(self, dataframe):

        if len(dataframe) == 0:
            print(f"Não há registros a inserir em {self.table_name}.")
            return False

        dataframe["dt_atualizacao"] = "2199-12-31 23:59:59"
        query = self.create_query_insert(dataframe)

        try:
            self.truncate_table_after_offset()
            self.exec_sql(query)
            print(f"{len(dataframe)} registros inseridos na tabela {self.table_name}.")
        except Exception as e:
            print(f"Erro ao inserir registros em {self.table_name}: {e}")
            exit()

    def select_fks_by_version(self, stage_dataframe):
        query_select = self.create_query_select_fact()

        try:
            with self.engine.connect() as connection:
                result = connection.execute(query_select)
                self.insert_data(pd.DataFrame(result))
        except Exception as e:
            print(f"Erro ao consultar registros em {self.table_name}: {e}")
            exit()




