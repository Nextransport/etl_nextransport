from .stage import Stage
from models.load.dims.dim_relacionado import DimRelacionado


class StageDimRelacionado(Stage, DimRelacionado):

    def __init__(self):
        self.fk_name = "cd_relacionado"
        self.dt_col_name = "dt_criacao"
        self.stage_cols = [
            "cd_relacionado",
            "ds_nomerazaosocial",
            "ds_cnpjcpf",
            "ds_ierg",
            "ds_endereco",
            "ds_cep",
            "ds_cidade",
            "ds_uf",
            "ds_pais",
            "ds_telefone1",
            "ds_telefone2",
            "ds_latitude",
            "ds_longitude",
            "ds_email",
            "ds_grupo",
            "dt_nascfundacao"
        ]
        Stage.__init__(self)
        DimRelacionado.__init__(self)