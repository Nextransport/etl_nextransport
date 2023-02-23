from .fact import Fact

class FactManutencao(Fact):

    def __init__(self):
        self.stg_table = self.stg_table("stg_manutencao", "stg_manutencao")
        self.table_name = "stg_fto_manutencao"
        self.dt_col_name = "dt_emissao"
        stg_table = self.stg_table.tb_name
        self.fact_fks = [
            {"table": "dim_manutencao", "schema": "dw", "fkey": "sk_manutencao", "bkey": "cd_manutencao",
             "bkeyf": "cd_manutencao", "type": "inner", "tb_alias": "dim_manutencao"},
            {"table": "dim_cliente", "schema": "dw", "fkey": "sk_cliente", "bkey": "cd_cliente", "bkeyf": "cd_cliente", "type": "inner",
             "tb_alias": "dim_cliente"},
            {"table": "dim_relacionado", "schema": "dw", "fkey": "sk_relacionado", "bkey": "cd_relacionado",
             "bkeyf": "cd_relacionado", "type": "left", "tb_alias": "dim_relacionado"},
            {"table": "dim_motorista", "schema": "dw", "fkey": "sk_motorista", "bkey": "cd_motorista", "bkeyf": "cd_motorista", "type": "left",
             "tb_alias": "dim_motorista"},
            # "dim_periodo", "sk_periodo", "left",
            # {"table": "dim_produto", "schema": "dw", "fkey": "sk_produto", "bkey": "cd_produto",
            #  "bkeyf": "cd_produto", "type": "left", "tb_alias": "dim_produto"},
            {"table": "dim_veiculo", "schema": "dw", "fkey": "sk_veiculo", "bkey": "cd_veiculo", "type": "left", "bkeyf": "cd_veiculo",
             "tb_alias": "dim_veiculo"},
            # {"table": "dim_viagem", "schema": "dw", "fkey": "sk_viagem", "bkey": "cd_viagem", "type": "left",
            #  "bkeyf": "cd_viagem", "tb_alias": "dim_viagem"},
        ]
        self.fact_columns = [
            {"table": stg_table, "column": "dt_emissao", "alias": "dt_emissao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "ds_tipomanutencao", "alias": "ds_tipomanutencao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": "dim_manutencao", "column": "sk", "alias": "sk_manutencao", "schema": "dw",
             "tb_alias": "dim_manutencao"},
            {"table": "dim_cliente", "column": "sk", "alias": "sk_cliente", "schema": "dw", "tb_alias": "dim_cliente"},
            # {"table": "dim_produto", "column": "sk", "alias": "sk_produto", "schema": "dw", "tb_alias": "dim_produto"},
            {"table": "dim_relacionado", "column": "sk", "alias": "sk_relacionado", "schema": "dw",
             "tb_alias": "dim_relacionado"},
            {"table": "dim_veiculo", "column": "sk", "alias": "sk_veiculo", "schema": "dw",
             "tb_alias": "dim_veiculo"},
            {"table": "dim_motorista", "column": "sk", "alias": "sk_motorista", "schema": "dw",
             "tb_alias": "dim_motorista"},
            {"table": stg_table, "column": "nr_valortotal", "alias": "nr_valortotal", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": ["nr_kilometragem", "nr_horimetro"], "alias": "nr_kmhorimetro",
             "schema": "stage", "tb_alias": stg_table},
            {"table": stg_table, "column": "dt_criacao", "alias": "dt_criacao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": None, "column": "dt_atualizacao", "alias": "dt_atualizacao", "schema": "dw"},
        ]
        Fact.__init__(self)