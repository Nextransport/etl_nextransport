from ...load.table import Table
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

class Stage(Table):

    schema = os.environ["db_schema_stage"]
    stage_cols = []

    def __init__(self):
        Table.__init__(self)

    def insert_stg_data(self, client_id, dataframe):
        query = self.create_query_insert_stage(client_id=client_id, dataframe=dataframe)

        try:
            self.exec_sql(query)
            print(f"{len(dataframe)} registro(s) inserido(s) em {self.table_name}")
        except Exception as e:
            print(f"Erro na insercao do registros na tabela {self.table_name}: {e}")
            exit()

    def create_query_insert_stage(self, client_id, dataframe):
        timestamp = datetime.now()
        query = f"insert into {self.table_name} ("

        for col in self.stage_cols:
            query += f"{col}, "
        query = query[:-2]
        query += ", cd_cliente, dt_criacao) values"

        for index in dataframe.index:
            data = dataframe.loc[index]

            query += "("

            for val in data:
                if val is None or pd.isna(val):
                    value = "null"
                else:
                    value = val
                query += f"{value}, " if isinstance(value, int) or isinstance(value, float) or value == "null" else f"'{value}', "
            query += f"{client_id}, '{timestamp}'), "

        query = query[:-2]
        query += ";"

        return str(query)


    def insert_data(self, dataframe, client_id):
        dataframe = dataframe[self.stage_cols]
        query = self.create_insert_query(dataframe, client_id)
        try:
            with self.engine.connect() as connection:
                self.truncate_table_after_offset()
                connection.execute(query)
                print(f"{len(dataframe)} registro inseridos em {self.table_name}")
        except Exception as e:
            print(f"Erro na insercao do registros na tabela {self.table_name}: {e}")
            exit()

    # def create_insert_query(self, dataframe, client_id):
    #     timestamp = datetime.now()
    #     query = f"insert into {self.table_name} ("
    #
    #     for ind in dataframe.columns:
    #         query += f"{ind}, "
    #     query = query[:-2]
    #     query += ", cd_cliente, dt_criacao) values "
    #
    #     for row in dataframe.index:
    #         query += f"("
    #         for col in dataframe.columns:
    #             val = dataframe[col].iloc[row]
    #             value = "null" if val is None else val
    #             query += f"{value}, " if isinstance(value, int) or isinstance(value, float) or value == "null" else f"'{value}', "
    #         query += f"'{client_id}', '{timestamp}'), "
    #
    #     query = query[:-2]
    #     return query
