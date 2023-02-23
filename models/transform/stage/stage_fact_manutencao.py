from .stage import Stage
from models.load.facts.fact_manutencao import FactManutencao


class StageFactManutencao(Stage, FactManutencao):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.stage_cols = [
            "dt_emissao",
            "cd_manutencao",
            "cd_relacionado",
            "cd_veiculo",
            "cd_motorista",
            "ds_tipomanutencao",
            "nr_valortotal"
        ]
        Stage.__init__(self)
        FactManutencao.__init__(self)