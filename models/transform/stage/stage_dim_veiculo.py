from .stage import Stage
from models.load.dims.dim_veiculo import DimVeiculo


class StageDimVeiculo(Stage, DimVeiculo):

    def __init__(self):
        self.dt_col_name = "dt_criacao"
        self.fk_name = "cd_veiculo"
        self.stage_cols = [
            "cd_veiculo",
            "ds_tipoveiculo",
            "ds_placa",
            "ds_chassi",
            "ds_renavam",
            "ds_marca",
            "ds_modelo",
            "nr_anofabricacao",
            "nr_anomodelo",
            "dt_aquisicao",
            "nr_frota",
            "ds_frota"
        ]
        Stage.__init__(self)
        DimVeiculo.__init__(self)