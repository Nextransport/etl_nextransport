from .stage import Stage
from models.load.dims.dim_motorista import DimMotorista


class StageDimMotorista(Stage, DimMotorista):

    def __init__(self):
        self.dt_col_name = "dt_criacao"
        self.fk_name = "cd_motorista"
        self.stage_cols = [
            "cd_motorista",
            "ds_nome",
            "ds_cpf",
            "ds_rg",
            "dt_nascimento",
            "ds_estadocivil",
            "fl_ativo",
            "ds_endereco",
            "ds_cidade",
            "ds_uf",
            "ds_cep",
            "ds_pais"
        ]
        Stage.__init__(self)
        DimMotorista.__init__(self)