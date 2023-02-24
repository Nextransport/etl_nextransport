from .dimension import Dimension

class DimPedidoFrete(Dimension):


    def __init__(self):
        self.table_name = "stg_dim_pedidofrete"
        self.fk_name = "cd_pedidofrete"
        self.dt_col_name = "dt_emissao"
        self.dim_columns = [
            "sk",
            "cd_cliente",
            "cd_pedidofrete",
            "dt_emissao",
            "cd_pedidofrete",
            "ds_cidadeorigem",
            "ds_cidadedestino",
            "ds_uforigem",
            "ds_ufdestino",
            "ds_siglauforigem",
            "ds_siglaufdestino",
        ]
        self.flow_columns = [
            "cd_pedidofrete",
        ]
        self.unique_columns = self.dim_columns
        Dimension.__init__(self)
        self.scd = False

