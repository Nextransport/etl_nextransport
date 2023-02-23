from .stage import Stage
from models.load.dims.dim_manutencao import DimManutencao

class StageDimManutencao(Stage, DimManutencao):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.fk_name = "cd_manutencao"
        self.stage_cols = [
            "dt_emissao",
            "cd_manutencao",
            "nr_documento",
            "ds_historico"
        ]
        Stage.__init__(self)
        DimManutencao.__init__(self)

    def insert_update_data(self, client_id, dataframe):
        dataframe = dataframe[self.stage_cols]
        DimManutencao.insert_update_data(self, client_id=client_id, dataframe=dataframe)
