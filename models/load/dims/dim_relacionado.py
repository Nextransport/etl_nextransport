from .dimension import Dimension

class DimRelacionado(Dimension):

    def __init__(self):
        self.table_name = "stg_dim_relacionado"
        self.fk_name = "cd_relacionado"
        self.dim_columns = [
            "sk",
            "cd_cliente",
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
            "dt_nascfundacao",
            "nr_versao",
            "dt_atualizacao",
            "dt_criacao"
        ]
        self.flow_columns = [
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
            "dt_nascfundacao",
        ]
        self.unique_columns = self.dim_columns
        Dimension.__init__(self)




