import os

import pandas as pd

from .stage import Stage
from models.load.facts.fact_abastecimento import FactAbastecimento
from models.transform.dataframe.dataframe_handle import DataframeHandle

class StageFactAbastecimento(Stage, FactAbastecimento):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.stage_cols = [
            "cd_produto",
            # "cd_bomba_propria",
            "cd_viagem",
            "cd_veiculo",
            "cd_relacionado",
            "cd_motorista",
            "dt_emissao",
            "cd_abastecimento",
            "nr_notafiscal",
            "nr_quantidade",
            "nr_preco",
            "nr_valortotal",
            "nr_kmhorimetro"
        ]
        Stage.__init__(self)
        FactAbastecimento.__init__(self)

    def insert_stg_data(self, client_id, dataframe):
        dataframe["nr_kmhorimetro"] = ""

        for index in dataframe.index:
            data = dataframe.loc[index]
            if float(data["nr_km"]) > 0:
                dataframe["nr_kmhorimetro"].iloc[index] = data["nr_km"]
            else:
                dataframe["nr_kmhorimetro"].iloc[index] = data["nr_horimetro"]

        dataframe = dataframe[self.stage_cols]
        Stage.insert_stg_data(self, client_id, dataframe)
        self.exec_triggers()

    def exec_triggers(self):
        schema = os.environ["db_schema_stage"]
        offset_days = os.environ["offset_days"]
        try:
            self.exec_sql(f"select {schema}.update_nrprecotabela_full({offset_days});")
            print(f"Function {schema}.update_nrprecotabela_full executada com sucesso!")
        except Exception as e:
            print(f"Nao foi possivel executar a function update_nrprecotabela_full: {e}")

        try:
            self.exec_sql(f"select {schema}.update_kmrodado_full({offset_days});")
            print(f"Function {schema}.update_kmrodado_full executada com sucesso!")
        except Exception as e:
            print(f"Nao foi possivel executar a function update_kmrodado_full: {e}")

    def select_registers_by_viagem(self, cd_viagem):
        df_handle = DataframeHandle()
        df = pd.DataFrame(columns=self.stage_cols)

        query = f"select "
        for col in self.stage_cols:
            query += f"{col}, "
        query = query[:-2]
        query += f" from {self.table_name} where cd_viagem = '{cd_viagem}'"

        try:
            with self.engine.connect() as connection:
                result = connection.execute(query)
                for row in result:
                    df2 = df_handle.row2frame(row, self.stage_cols)
                    df = pd.concat([df, df2])
                df = df.reset_index(drop=True)
                return df
        except Exception as e:
            print(f"Erro ao consultar registros na tabela {self.table_name}: {e}")
            exit()
