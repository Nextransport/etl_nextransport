from .fact import Fact

class FactFaturamento(Fact):



    def __init__(self):
        self.table_name = "stg_fto_faturamento"
        self.stg_table = self.stg_table("stg_faturamento", "stg_faturamento")
        stg_table = self.stg_table.tb_name
        self.dt_col_name = "dt_emissao"
        self.fact_fks = [
            {"table": "dim_cliente", "tb_alias": "dim_cliente", "schema": "dw", "fkey": "sk_cliente",
             "bkey": "cd_cliente", "bkeyf": "cd_cliente", "type": "inner"},
            # {"table": "dim_conta_gerencial", "tb_alias": "dim_conta_gerencial", "schema": "dw",
            # "fkey": "sk_contagerencial", "bkey": "cd_contagerencial", "bkeyf": "cd_contagerencial", "type": "inner"},
            {"table": "dim_relacionado", "schema": "dw", "fkey": "sk_relacionado", "bkey": "cd_relacionado",
             "bkeyf": "cd_relacionado", "type": "inner", "tb_alias": "dim_relacionado"},
            {"table": "dim_motorista", "tb_alias": "dim_motorista", "schema": "dw", "fkey": "sk_motorista",
             "bkey": "cd_motorista", "bkeyf": "cd_motorista", "type": "left"},
            # {"table": "dim_periodo", "tb_alias": "dim_periodo", "schema": "sk", "fkey": "sk_periodo",
            # "bkey": "dt_emissao", "bkeyf": "dt_emissao", "type": "inner"},
            # {"table": "dim_rota", "tb_alias": "dim_rota", "schema": "dw", "fkey": "sk_rota", "bkey": "cd_rota",
            # "bkeyf": "cd_rota", "type": "inner"},
            # {"table": "dim_titulo", "tb_alias": "dim_titulo", "schema": "dw", "fkey": "sk_titulo",
            # "bkey": "cd_titulo", # "bkeyf": "cd_titulo", "type": "inner"},
            {"table": "dim_veiculo", "tb_alias": "dim_veiculo", "schema": "dw", "fkey": "sk_veiculo",
             "bkey": "cd_veiculo", "bkeyf": "cd_veiculo", "type": "inner"},
            # {"table": "dim_viagem", "tb_alias": "dim_viagem", "schema": "dw", "fkey": "sk_viagem", "bkey": "cd_viagem",
            #  "bkeyf": "cd_viagem", "type": "inner"},
        ]
        self.fact_columns = [
            {"table": stg_table, "column": "dt_emissao", "alias": "dt_emissao", "schema": "stage", "tb_alias": stg_table},
            {"table": "dim_cliente", "column": "sk", "alias": "sk_cliente", "schema": "dw", "tb_alias": "dim_cliente"},
            # "dim_periodo", "sk_periodo", "left",
            {"table": "dim_motorista", "column": "sk", "alias": "sk_motorista", "schema": "dw", "tb_alias": "dim_motorista"},
            {"table": "dim_veiculo", "column": "sk", "alias": "sk_veiculo", "schema": "dw", "tb_alias": "dim_veiculo"},
            {"table": "dim_relacionado", "column": "sk", "alias": "sk_relacionado", "schema": "dw",
             "tb_alias": "dim_relacionado"},
            # {"table": "dim_conta_gerencial", "column": "sk", "alias": "sk_contagerencial", "schema": "dw",
            #  "tb_alias": "dim_conta_gerencial"},
            # {"table": "dim_titulo", "column": "sk", "alias": "sk_titulo", "schema": "dw",
            #  "tb_alias": "dim_titulo"},
            # {"table": "dim_rota", "column": "sk", "alias": "sk_rota", "schema": "dw",
            #  "tb_alias": "dim_rota"},
            # {"table": "dim_viagem", "column": "sk", "alias": "sk_viagem", "schema": "dw",
            #  "tb_alias": "dim_viagem"},
            {"table": stg_table, "column": "nr_valorfrete", "alias": "nr_valorfrete", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "nr_valorpedagio", "alias": "nr_valorpedagio", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "nr_valortotal", "alias": "nr_valortotal", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "nr_aliqicms", "alias": "nr_aliqicms", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "dt_criacao", "alias": "dt_criacao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "ds_situacao", "alias": "ds_situacao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": None, "column": "dt_atualizacao", "alias": "dt_atualizacao", "schema": "dw"},
        ]
        Fact.__init__(self)




