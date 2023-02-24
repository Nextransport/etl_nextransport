from .stage import Stage
from models.load.dims.dim_pedidofrete import DimPedidoFrete

class StageDimPedidoFrete(Stage, DimPedidoFrete):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.fk_name = "cd_pedidofrete"
        self.stage_cols = [
            "dt_emissao",
            "cd_pedidofrete",
            "ds_cidadeorigem",
            "ds_cidadedestino",
            "ds_uforigem",
            "ds_ufdestino",
            "ds_siglauforigem",
            "ds_siglaufdestino"
        ]
        Stage.__init__(self)
        DimPedidoFrete.__init__(self)

    # def insert_update_data(self, client_id, dataframe):
    #     dataframe["dt_emissao"] = dataframe["dt_final"]
    #     dataframe = dataframe[self.stage_cols]
    #     DimViagem.insert_update_data(self, client_id=client_id, dataframe=dataframe)
