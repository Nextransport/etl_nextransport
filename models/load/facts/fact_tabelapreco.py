from .fact import Fact

class FactTabelaPreco(Fact):

    def __init__(self):
        self.stg_table = self.stg_table("stg_tabelapreco", "stg_tabelapreco")
        self.table_name = "stg_fto_tabelapreco"
        self.dt_col_name = "dt_inicial"
        stg_table = self.stg_table.tb_name
        self.fact_fks = [
            {"table": "dim_cliente", "schema": "dw", "fkey": "sk_cliente", "bkey": "cd_cliente", "bkeyf": "cd_cliente", "type": "inner",
             "tb_alias": "dim_cliente"},
            {"table": "dim_relacionado", "schema": "dw", "fkey": "sk_relacionado", "bkey": "cd_relacionado", "bkeyf": "cd_relacionado",
             "type": "inner", "tb_alias": "dim_relacionado"},
            {"table": "dim_produto", "schema": "dw", "fkey": "sk_produto", "bkey": "cd_produto", "bkeyf": "cd_produto",
             "type": "inner", "tb_alias": "dim_produto"},
        ]
        self.fact_columns = [
            {"table": "dim_cliente", "column": "sk", "alias": "sk_cliente", "schema": "dw",
             "tb_alias": "dim_cliente"},
            {"table": "dim_relacionado", "column": "sk", "alias": "sk_relacionado", "schema": "dw",
             "tb_alias": "dim_relacionado"},
            {"table": "dim_produto", "column": "sk", "alias": "sk_produto", "schema": "dw",
             "tb_alias": "dim_produto"},
            {"table": stg_table, "column": "dt_inicial", "alias": "dt_inicial", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "dt_final", "alias": "dt_final", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "nr_valor", "alias": "nr_valor", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "dt_criacao", "alias": "dt_criacao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "cd_tabela", "alias": "cd_tabela", "schema": "stage",
             "tb_alias": stg_table},
            {"table": None, "column": "dt_atualizacao", "alias": "dt_atualizacao", "schema": "dw"},
        ]
        Fact.__init__(self)