import pandas as pd

from .stage import Stage
from models.load.dims.dim_pedidofrete import DimPedidoFrete

class StageDimPedidoFrete(Stage, DimPedidoFrete):

    def __init__(self):
        self.dt_col_name = "dt_emissao"
        self.fk_name = "cd_pedidofrete"
        self.stage_cols = [
            "dt_emissao",
            "cd_pedidofrete",
            "ds_cidadeorigem",
            "ds_cidadedestino",
            "ds_uforigem",
            "ds_ufdestino",
            "ds_siglauforigem",
            "ds_siglaufdestino"
        ]
        Stage.__init__(self)
        DimPedidoFrete.__init__(self)

    def insert_update_data(self, client_id, dataframe, unique_cols):
        dataframe = self.input_estados(dataframe)
        DimPedidoFrete.insert_update_data(self, client_id=client_id, dataframe=dataframe, unique_cols=unique_cols)

    def input_estados(self, dataframe):
        list_uf = {
            "AC": "ACRE",
            "AL": "ALAGOAS",
            "AP": "AMAPA",
            "AM": "AMAZONAS",
            "BA": "BAHIA",
            "CE": "CEARA",
            "DF": "DISTRITO FEDERAL",
            "ES": "ESPIRITO SANTO",
            "GO": "GOIAS",
            "MA": "MARANHAO",
            "MT": "MATO GROSSO",
            "MS": "MATO GROSSO DO SUL",
            "MG": "MINAS GERAIS",
            "PA": "PARA",
            "PB": "PARAIBA",
            "PR": "PARANA",
            "PE": "PERNAMBUCO",
            "PI": "PIAUI",
            "RJ": "RIO DE JANEIRO",
            "RN": "RIO GRANDE DO NORTE",
            "RS": "RIO GRANDE DO SUL",
            "RO": "RONDONIA",
            "RR": "RORAIMA",
            "SC": "SANTA CATARINA",
            "SP": "SAO PAULO",
            "SE": "SERGIPE",
            "TO": "TOCANTINS",
            "EX": "EXTERIOR"
        }
        dataframe.reset_index(inplace=True, drop=True)
        for index in dataframe.index:
            data = dataframe.iloc[index].copy()
            if pd.notna(data["ds_siglauforigem"]) and pd.notna(data["ds_siglaufdestino"]):
                dataframe.at[index, "ds_uforigem"] = list_uf[data["ds_siglauforigem"]]
                dataframe.at[index, "ds_ufdestino"] = list_uf[data["ds_siglaufdestino"]]
        return dataframe