from .stage import Stage


class StageViagem(Stage):

    def __init__(self):
        self.table_name = "stg_viagem"
        self.dt_col_name = "dt_final"
        Stage.__init__(self)

    def insert_data(self, dataframe, client_id):
        dataframe.reset_index(inplace=True, drop=True)
        Stage.insert_data(self, dataframe, client_id)