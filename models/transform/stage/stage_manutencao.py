from .stage import Stage


class StageManutencao(Stage):

    def __init__(self):
        self.table_name = "stg_manutencao"
        self.dt_col_name = "dt_emissao"
        Stage.__init__(self)