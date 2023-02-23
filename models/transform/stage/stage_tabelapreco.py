from .stage import Stage


class StageTabelaPreco(Stage):

    def __init__(self):
        self.table_name = "stg_tabelapreco"
        self.dt_col_name = "dt_inicial"
        Stage.__init__(self)