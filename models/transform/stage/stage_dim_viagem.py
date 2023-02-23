from .stage import Stage
from models.load.dims.dim_viagem import DimViagem

class StageDimViagem(Stage, DimViagem):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.fk_name = "cd_viagem"
        self.stage_cols = [
            "dt_emissao",
            "cd_viagem"
        ]
        Stage.__init__(self)
        DimViagem.__init__(self)

    def insert_update_data(self, client_id, dataframe):
        dataframe["dt_emissao"] = dataframe["dt_final"]
        dataframe = dataframe[self.stage_cols]
        DimViagem.insert_update_data(self, client_id=client_id, dataframe=dataframe)
