from .stage import Stage
from models.load.facts.fact_faturamento import FactFaturamento


class StageFactFaturamento(Stage, FactFaturamento):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.stage_cols = [
            "dt_emissao",
            "cd_motorista",
            "cd_veiculo",
            "cd_relacionado",
            "nr_valorfrete",
            "nr_valortotal",
            "nr_aliqicms",
            "nr_km",
            "ds_situacao"
        ]
        Stage.__init__(self)
        FactFaturamento.__init__(self)