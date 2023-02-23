from .dimension import Dimension

class DimProduto(Dimension):

    def __init__(self):
        self.table_name = "stg_dim_produto"
        self.fk_name = "cd_produto"
        self.dim_columns = [
            "sk",
            "cd_cliente",
            "cd_produto",
            "ds_produto",
            "ds_ncm",
            "ds_undmedida"
        ]
        self.flow_columns = [
            "cd_produto",
            "ds_produto",
            "ds_ncm",
            "ds_undmedida",
        ]
        self.unique_columns = [
            "cd_cliente",
            "cd_produto"
        ]
        Dimension.__init__(self)




