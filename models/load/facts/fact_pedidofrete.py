from .fact import Fact

class FactPedidoFrete(Fact):

    def __init__(self):
        self.stg_table = self.stg_table("stg_fto_pedidofrete", "stg_fto_pedidofrete")
        self.table_name = "stg_fto_pedidofrete"
        self.dt_col_name = "dt_emissao"
        stg_table = self.stg_table.tb_name
        self.fact_fks = [
            {"table": "dim_cliente", "schema": "dw", "fkey": "sk_cliente", "bkey": "cd_cliente", "bkeyf": "cd_cliente",
             "type": "inner", "tb_alias": "dim_cliente"},
            {"table": "dim_pedidofrete", "schema": "dw", "fkey": "sk_pedidofrete", "bkey": "cd_pedidofrete",
             "bkeyf": "cd_pedidofrete", "type": "inner", "tb_alias": "dim_pedidofrete"},
            {"table": "dim_relacionado", "schema": "dw", "fkey": "sk_relacionado", "bkey": "cd_relacionado",
             "bkeyf": "cd_relacionado", "type": "inner", "tb_alias": "dim_relacionado"},
            {"table": "dim_viagem", "schema": "dw", "fkey": "sk_viagem", "bkey": "cd_viagem", "bkeyf": "cd_viagem",
             "type": "inner", "tb_alias": "dim_viagem"},
        ]
        self.fact_columns = [
            {"table": "dim_cliente", "column": "sk", "alias": "sk_cliente", "schema": "dw", "tb_alias": "dim_cliente"},
            {"table": "dim_pedidofrete", "column": "sk", "alias": "sk_pedidofrete", "schema": "dw", "tb_alias": "dim_pedidofrete"},
            {"table": "dim_relacionado", "column": "sk", "alias": "sk_relacionado", "schema": "dw", "tb_alias": "dim_relacionado"},
            {"table": "dim_viagem", "column": "sk", "alias": "sk_viagem", "schema": "dw",
             "tb_alias": "dim_viagem"},
            {"table": stg_table, "column": "dt_emissao", "alias": "dt_emissao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "nr_km", "alias": "nr_km", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "nr_peso", "alias": "nr_peso", "schema": "stage",
             "tb_alias": stg_table},
            {"table": None, "column": "dt_criacao", "alias": "dt_criacao", "schema": "dw",
             "tb_alias": "dim_pedidofrete"},
        ]
        Fact.__init__(self)