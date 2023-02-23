from .dimension import Dimension


class DimMotorista(Dimension):

    def __init__(self):
        self.table_name = "stg_dim_motorista"
        self.fk_name = "cd_motorista"
        self.dim_columns = [
            "sk",
            "cd_cliente",
            "cd_motorista",
            "ds_nome",
            "ds_cpf",
            "ds_rg",
            "dt_nascimento",
            "ds_estadocivil",
            "ds_endereco",
            "ds_cidade",
            "ds_uf",
            "ds_pais",
            "nr_versao",
            "dt_criacao",
            "dt_atualizacao"
        ]
        self.flow_columns = [
            "cd_motorista",
            "ds_nomemotorista",
            "ds_cpf",
            "ds_rg",
            "dt_nascimento",
            "ds_estadocivil",
            "ds_enderecomotorista",
            "ds_cidademotorista",
            "ds_ufmotorista",
            "ds_paismotorista",
        ]
        self.exchange_columns = {
            "ds_nomemotorista": "ds_nome",
            "ds_enderecomotorista": "ds_endereco",
            "ds_cidademotorista": "ds_cidade",
            "ds_ufmotorista": "ds_uf",
            "ds_paismotorista": "ds_pais"
        }
        self.unique_columns = self.dim_columns
        Dimension.__init__(self)
        self.renamecols_type = 2




