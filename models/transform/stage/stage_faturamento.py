from .stage import Stage


class StageFaturamento(Stage):

    def __init__(self):
        self.table_name = "stg_faturamento"
        self.dt_col_name = "dt_emissao"
        Stage.__init__(self)