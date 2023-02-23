from .fact import Fact

class FactViagem(Fact):

    def __init__(self):
        self.stg_table = self.stg_table("stg_viagem", "stg_viagem")
        self.table_name = "stg_fto_viagem"
        self.dt_col_name = "dt_final"
        stg_table = self.stg_table.tb_name
        self.fact_fks = [
            {"table": "dim_cliente", "schema": "dw", "fkey": "sk_cliente", "bkey": "cd_cliente", "bkeyf": "cd_cliente", "type": "inner",
             "tb_alias": "dim_cliente"},
            {"table": "dim_viagem", "schema": "dw", "fkey": "sk_viagem", "bkey": "cd_viagem", "bkeyf": "cd_viagem", "type": "inner",
             "tb_alias": "dim_viagem"},
            {"table": "dim_motorista", "schema": "dw", "fkey": "sk_motorista", "bkey": "cd_motorista", "bkeyf": "cd_motorista", "type": "left",
             "tb_alias": "dim_motorista"},
            {"table": "dim_veiculo", "schema": "dw", "fkey": "sk_veiculo", "bkey": "cd_veiculo",  "bkeyf": "cd_veiculo","type": "inner",
             "tb_alias": "dim_veiculo"},
            {"table": "dim_veiculo", "schema": "dw", "fkey": "sk_reboque", "bkey": "cd_veiculo",  "bkeyf": "cd_veiculoreboque", "type": "left",
             "tb_alias": "dim_reboque"},
        ]
        self.fact_columns = [
            {"table": "dim_cliente", "column": "sk", "alias": "sk_cliente", "schema": "dw", "tb_alias": "dim_cliente"},
            {"table": "dim_veiculo", "column": "sk", "alias": "sk_veiculo", "schema": "dw", "tb_alias": "dim_veiculo"},
            {"table": "dim_veiculo", "column": "sk", "alias": "sk_reboque", "schema": "dw", "tb_alias": "dim_reboque"},
            {"table": "dim_motorista", "column": "sk", "alias": "sk_motorista", "schema": "dw",
             "tb_alias": "dim_motorista"},
            {"table": "dim_viagem", "column": "sk", "alias": "sk_viagem", "schema": "dw",
             "tb_alias": "dim_viagem"},
            {"table": stg_table, "column": "dt_inicial", "alias": "dt_inicial", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "dt_final", "alias": "dt_final", "schema": "stage",
             "tb_alias": stg_table},
            {"table": stg_table, "column": "dt_criacao", "alias": "dt_criacao", "schema": "stage",
             "tb_alias": stg_table},
            {"table": None, "column": "dt_atualizacao", "alias": "dt_atualizacao", "schema": "dw",
             "tb_alias": "dim_viagem"},
        ]
        Fact.__init__(self)