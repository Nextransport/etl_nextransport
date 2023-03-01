from .request import Request
from .request_carga import RequestCarga
from models.transform.dataframe.dataframe_handle import DataframeHandle
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os
# import logging

load_dotenv()

# logging.basicConfig(filename=f'{os.environ["base_dir"]}\log\{date.today()}.log', encoding='utf-8', level=logging.INFO)


class RequestPedidoFrete(Request):
    def __init__(self):

        self.dataframe_results = pd.DataFrame()
        self.filter_dataframe_results = pd.DataFrame()
        self.df_handle = DataframeHandle()
        self.endpoint = "Cargas"
        self.action = "BuscarCarga"
        self.namespaces = (
            ['soapenv', 'http://schemas.xmlsoap.org/soap/envelope/'],
            ['tem', 'http://tempuri.org/'],
            ['dom', 'http://schemas.datacontract.org/2004/07/Dominio.ObjetosDeValor.WebService.Carga'],
            ['dom1', 'http://schemas.datacontract.org/2004/07/Dominio.ObjetosDeValor.Embarcador.Pessoas'],
            ['dom2', 'http://schemas.datacontract.org/2004/07/Dominio.ObjetosDeValor.Embarcador.Localidade'],
            ['dom3', 'http://schemas.datacontract.org/2004/07/Dominio.ObjetosDeValor'],
            ['dom4', 'http://schemas.datacontract.org/2004/07/Dominio.ObjetosDeValor.Embarcador.Carga'],
            ['arr', 'http://schemas.microsoft.com/2003/10/Serialization/Arrays']
        )
        self.set_headers_request()
        self.set_limit_dates()

    def get_dataframe_pedidofrete(self):

        df_pedidosfrete = pd.DataFrame()
        req_carga = RequestCarga()

        offset_date = pd.to_datetime(self.get_offset_date())
        limit_date = pd.to_datetime(os.environ["limit_date"])
        max_requests = int(os.environ["max_requests"])
        escape_requests = int(os.environ["escape_requests"])
        print("Offset date:", offset_date)
        while escape_requests > 0 and max_requests > 0:
            df_num_pedidofrete = req_carga.get_dataframe_carga()
            df_pedidofrete = self.get_dataframe_single_viagem(df_num_pedidofrete)
            df_pedidosfrete = pd.concat([df_pedidosfrete, df_pedidofrete])

            if len(df_pedidosfrete) > 0:
                min_date = self.check_mindate_dataframe(offset_date, df_pedidofrete)
                if min_date < offset_date:
                    escape_requests -= 1
            max_requests -= 1

        df_viagem = self.filter_df_viagem(df_pedidofrete, offset_date, limit_date)

        df_pedidosfrete = df_pedidosfrete[(df_pedidosfrete.dt_emissao >= offset_date) & (df_pedidosfrete.dt_emissao <= limit_date)]

        return [df_pedidosfrete, df_viagem]

    def filter_df_viagem(self, df_pedidofrete, offset_date, limit_date):
        df_viagem = df_pedidofrete.drop_duplicates(subset=["cd_viagem"]).copy()

        filter1 = df_viagem["cd_viagem"] != "0"
        df_viagem.where(filter1, inplace=True)
        filter1 = df_viagem["dt_final"] >= offset_date
        df_viagem.where(filter1, inplace=True)
        df_viagem.dropna(subset=["cd_viagem"], inplace=True)
        df_viagem.rename(columns={"cd_veiculoreboque": "cd_reboque"}, inplace=True)

        return df_viagem

    def filter_by_date(self, dataframe, colname, date):
        dataframe[colname] = pd.to_datetime(dataframe[colname], format='%Y-%m-%d')
        dataframe = dataframe.loc[(dataframe[colname] >= date)]
        return dataframe

    def get_dataframe_single_viagem(self, df_cargas):
        df_pedidosfrete = pd.DataFrame()
        for index in df_cargas.index:
            load_id = df_cargas['cd_carga'].iloc[index]
            order_id = df_cargas['cd_pedido'].iloc[index]
            df_pedidofrete = self.get_dataframe_w2params(
                nodelist_name="b:CargaIntegracao",
                flow_name="flow_pedido_frete",
                load_id=load_id,
                order_id=order_id
            )
            df_pedidosfrete = pd.concat([df_pedidosfrete, df_pedidofrete])

        return df_pedidosfrete

    def check_mindate_dataframe(self, min_date, df):

        filter_df = self.df_handle.reindex_dataframe(df)
        min_date_df = filter_df["dt_emissao"].min()

        if pd.notna(min_date_df):
            return min_date_df
        else:
            return min_date

    def check_maxdate_dataframe(self, max_date, df):

        filter_df = self.df_handle.reindex_dataframe(df)
        max_date_df = filter_df["dt_final"].max()

        if pd.notna(max_date_df):
            return max_date_df
        else:
            return max_date
