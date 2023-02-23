from .dimension import Dimension

class DimManutencao(Dimension):


    def __init__(self):
        self.table_name = "stg_dim_manutencao"
        self.fk_name = "cd_manutencao"
        self.dt_col_name = "dt_emissao"
        self.dim_columns = [
            "sk",
            "cd_cliente",
            "cd_manutencao",
            "nr_documento",
            "ds_historico",
            "nr_versao",
            "dt_atualizacao",
            "dt_criacao"
        ]
        self.flow_columns = [
            "cd_manutencao",
            "dt_emissao",
            "nr_documento",
            "ds_historico"
        ]
        self.unique_columns = self.dim_columns
        Dimension.__init__(self)
        self.scd = False