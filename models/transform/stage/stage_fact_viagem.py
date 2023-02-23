from .stage import Stage
from models.transform.stage.stage_fact_abastecimento import StageFactAbastecimento
from models.load.facts.fact_viagem import FactViagem



class StageFactViagem(Stage, FactViagem):

    def __init__(self):
        self.dt_col_name = "dt_final"
        self.stage_cols = [
            "cd_viagem",
            "cd_motorista",
            "cd_veiculo",
            "cd_reboque",
            "dt_inicial",
            "dt_final",
            "nr_kminicial",
            "nr_kmfinal",
            "nr_hrinicial",
            "nr_hrfinal",
            "nr_kmrodado",
            "nr_horastrabalhadas"
        ]
        Stage.__init__(self)
        FactViagem.__init__(self)

