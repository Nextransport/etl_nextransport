from .dimension import Dimension

class DimViagem(Dimension):


    def __init__(self):
        self.table_name = "stg_dim_viagem"
        self.fk_name = "cd_viagem"
        self.dt_col_name = "dt_final"
        self.dim_columns = [
            "sk",
            "cd_cliente",
            "cd_viagem",
            "dt_inicial",
            "dt_final",
            "nr_kminicial",
            "nr_kmfinal",
            "nr_hrinicial",
            "nr_hrfinal",
            "nr_kmrodado",
            "nr_horas_totais",
            "dt_criacao",
            "dt_atualizacao"
        ]
        self.flow_columns = [
            "cd_viagem",
        ]
        self.unique_columns = self.dim_columns
        Dimension.__init__(self)
        self.scd = False

