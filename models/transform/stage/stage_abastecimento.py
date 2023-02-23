from .stage import Stage


class StageAbastecimento(Stage):

    def __init__(self):
        self.table_name = "stg_abastecimento"
        self.dt_col_name = "dt_emissao"
        Stage.__init__(self)
