from .stage import Stage
from models.load.dims.dim_produto import DimProduto


class StageDimProduto(Stage, DimProduto):

    def __init__(self):
        self.dt_col_name = "dt_criacao"
        self.fk_name = "cd_produto"
        self.stage_cols = [
            "cd_produto",
            "ds_produto",
            "ds_ncm"
        ]
        Stage.__init__(self)
        DimProduto.__init__(self)