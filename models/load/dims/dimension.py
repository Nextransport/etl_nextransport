import pandas as pd
from datetime import datetime, date
from ..table import Table
from dotenv import load_dotenv
from sqlalchemy import text
import os

load_dotenv()

class Dimension(Table):

    dim_columns = []
    dim_dataframe = pd.DataFrame()
    exchange_columns = []
    renamecols_type = None
    unique_columns = []
    scd = None

    schema = ""

    def __init__(self):
        self.scd = True
        self.schema = os.environ["db_schema_dw"]
        self.renamecols_type = None
        Table.__init__(self)

    def rename_flow_columns(self):
        for index in self.exchange_columns:
            self.flow_dataframe = self.df_handle.rename_column(self.flow_dataframe, index, self.exchange_columns[index])

        count = 0
        for index in self.flow_columns:
            for index2 in self.exchange_columns:
                val_exchange = self.exchange_columns[index2]
                if index2 == index:
                    self.flow_columns[count] = val_exchange

            count += 1

        return self.flow_dataframe

    def undo_rename_flow_columns(self):
        for index in self.exchange_columns:
            self.flow_dataframe = self.df_handle.rename_column(self.flow_dataframe, self.exchange_columns[index], index)

        count = 0
        for index in self.flow_columns:
            for index2 in self.exchange_columns:
                val_exchange = self.exchange_columns[index2]
                if val_exchange == index:
                    self.flow_columns[count] = index2

            count += 1

    def get_register_versions(self, client_id, fk_value):

        self.dim_dataframe = pd.DataFrame()

        with self.engine.connect() as connection:
            query = text(f"select * from {self.table_name} where cd_cliente = {client_id} and {self.fk_name} = '{fk_value}'")

            result = connection.execute(query)
            count = 0
            for row in result:
                count2 = 2
                for index in self.stage_cols:
                    self.dim_dataframe.at[count, index] = row[count2]
                    count2 += 1
                count += 1

            return self.dim_dataframe


    def proccess_flow_dataframe(self, dataframe, renamecols=None):

        self.select_cols_dataframe(dataframe)

        if renamecols == 1:
            self.rename_flow_columns()
            self.select_cols_dataframe(dataframe)
            self.undo_rename_flow_columns()
        elif renamecols == 2:
            self.select_cols_dataframe(dataframe)
            self.rename_flow_columns()
        else:
            self.select_cols_dataframe(dataframe)

        self.flow_dataframe = self.df_handle.reindex_dataframe(self.flow_dataframe)
        return self.flow_dataframe

    def select_cols_dataframe(self, dataframe):
        self.flow_dataframe = dataframe[:]
        self.flow_dataframe = self.flow_dataframe[self.flow_columns]

    def insert_update_data(self, dataframe, client_id, unique_cols=None):

        insert_query = self.create_insert_query(dataframe=dataframe, client_id=client_id, unique_cols=unique_cols)

        if insert_query == "":
            return False

        try:
            self.exec_sql(insert_query)
        except Exception as e:
            print(f"Erro no insert de registros na tabela {self.table_name}: {e}")
            exit()

    def compare_versions(self, old_version, new_version):
        count = 0
        for index in self.flow_columns:
            if index in self.unique_columns:
                if isinstance(old_version[count], date):
                    if pd.to_datetime(old_version[count]) != pd.to_datetime(old_version[count]):
                        return False
                else:
                    if str(old_version[count]) != str(new_version[count]):
                        return False
            count += 1
        return True

    #
    # Otimizar código para reduzir a quantidade de consultas / Atualmente uma por registro
    #
    def select_old_version(self, client_id, version, data):
        query = self.create_select_query_old_version(client_id, version, data)

        with self.engine.connect() as connection:
            result = connection.execute(query)
            for row in result:
                return row


    def create_select_query_old_version(self, client_id, version, data):

        query = "select "
        for col in self.stage_cols:
            query += f"{col}, "
        query = query[:-2]
        query += f" from {self.table_name} where"
        query += f" cd_cliente = {client_id} and"
        query += f" {self.fk_name} = '{data[self.fk_name]}' and"
        query += f" nr_versao = {version};"

        return text(query)

    def create_dataframe_for_insert(self, dataframe, client_id, unique_cols=None):

        dataframe = self.df_handle.reindex_dataframe(dataframe=dataframe, list_columns_consider=unique_cols, filter=[self.fk_name])
        df = pd.DataFrame(columns=dataframe.columns)
        df.insert(len(df.columns), "nr_versao", [])

        for index in dataframe.index:
            data = dataframe.iloc[index].copy()

            versions = self.get_register_versions(client_id, data[self.fk_name])
            version_num = len(versions) + 1
            data["nr_versao"] = version_num

            if version_num == 1:
                df.loc[len(df.index)] = data
            else:
                old_version = self.select_old_version(client_id, (version_num - 1), data)
                if not self.compare_versions(old_version, data):
                    if self.scd is True:
                        self.update_att_date(client_id, (version_num-1), data)
                        df.loc[len(df.index)] = data
                    else:
                        self.update_register(client_id, (version_num-1), data)

        df = self.df_handle.reindex_dataframe(df)

        return df
    #
    # Otimizar até aqui
    #

    def create_insert_query(self, dataframe, client_id, unique_cols=None):

        timestamp = datetime.now()
        # df = self.create_dataframe_for_insert(dataframe=dataframe, client_id=client_id, unique_cols=unique_cols)
        df = dataframe.reset_index(drop=True)
        if len(df) == 0:
            return ""

        query = f"insert into {self.table_name} ("

        for col in dataframe.columns:
            query += f"{col}, "
        query = query[:-2]
        query += ") values "

        for index1 in df.index:

            data = df.iloc[index1]
            query += "("

            for index2 in data.index:

                value = "null" if data[index2] is None or pd.isna(data[index2]) else data[index2]
                query += f"{value}, " if value == "null" else f"'{value}', "

            query = query[:-2]
            query += "), "

        query = query[:-2]
        query += ";"

        return query

    def update_register(self, client_id, version, data):
        timestamp = datetime.now()
        query = self.create_update_query_att_register(client_id, version, data, timestamp)

        try:
            self.exec_sql(query)
            print(f"Registro {data[self.fk_name]} da tabela {self.table_name} atualizado.")
        except Exception as e:
            print(f"Erro ao atualizar registros na tabela {self.table_name}: {e}")
            exit()


    def create_update_query_att_register(self, client_id, version, data, timestamp):
        query = f"update {self.table_name} set "
        cols = ["sk", "cd_cliente", "dt_atualizacao", "dt_criacao"]
        data["nr_versao"] = version

        for col in self.dim_columns:
            if col not in cols:
                value = "null" if data[col] is None or pd.isna(data[col]) else data[col]
                query += f" {col} = "
                query += f"{value}, " if value == "null" else f"'{value}', "

        query += f" dt_atualizacao = '{timestamp}' "
        query += f" where cd_cliente = {client_id} and "
        query += f"{self.fk_name} = '{data[self.fk_name]}' and "
        query += f"nr_versao = {version}"

        return query

    def update_att_date(self, client_id, version, data):
        timestamp = datetime.now()
        query = self.create_update_query_att_date(client_id, version, data, timestamp)
        try:
            self.exec_sql(query)
            print(f"Atualizacao do registro na tabela {self.table_name} {self.fk_name} = {data[self.fk_name]} executada com sucesso!")
        except Exception as e:
            print(f"Erro na atualizacao do registro na tabela {self.table_name} {self.fk_name} = {data[self.fk_name]}: {e}")
            exit()

    def create_update_query_att_date(self, client_id, version, data, timestamp):

        query = f"update {self.table_name} set dt_atualizacao = '{timestamp}' where "
        query += f"cd_cliente = {client_id} and "
        query += f"{self.fk_name} = '{data[self.fk_name]}' and "
        query += f"nr_versao = {version}"

        return query
