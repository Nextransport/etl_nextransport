from .stage import Stage
from models.load.facts.fact_tabelapreco import FactTabelaPreco


class StageFactTabelaPreco(Stage, FactTabelaPreco):

    def __init__(self):
        self.dt_col_name = "dt_inicial"
        self.stage_cols = [
            "cd_relacionado",
            "cd_produto",
            "cd_tabela",
            "dt_inicial",
            "dt_final",
            "nr_valor"
        ]
        Stage.__init__(self)
        FactTabelaPreco.__init__(self)