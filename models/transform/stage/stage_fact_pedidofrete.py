from .stage import Stage
from models.load.facts.fact_pedidofrete import FactPedidoFrete


class StageFactPedidoFrete(Stage, FactPedidoFrete):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.stage_cols = [
            "dt_emissao",
            "cd_pedidofrete",
            "cd_relacionado",
            "cd_viagem",
            "nr_km",
            "nr_peso",
        ]
        Stage.__init__(self)
        FactPedidoFrete.__init__(self)

    def insert_stg_data(self, client_id, dataframe):
        dataframe.reset_index(inplace=True, drop=True)

        for index in dataframe.index:
            data = dataframe.loc[index]
            if data["cd_viagem"] == "0":
                dataframe.at[index, "cd_viagem"] = "null"

        Stage.insert_stg_data(self, client_id, dataframe)