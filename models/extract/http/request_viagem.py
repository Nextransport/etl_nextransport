from .request import Request
from .request_carga import RequestCarga
from models.transform.dataframe.dataframe_handle import DataframeHandle
import pandas as pd
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename=f'{os.environ["base_dir"]}\log\{date.today()}.log', encoding='utf-8', level=logging.INFO)


class RequestViagem(Request):

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


    def get_dataframe_viagem(self):

        df_via_acum = pd.DataFrame()
        df_carga_acum = pd.DataFrame()
        req_carga = RequestCarga()

        min_date = datetime.today()
        offset_days = timedelta(int(os.environ["offset_days"]))
        offset_date = min_date - offset_days

        max_requests = int(os.environ["max_requests"])
        escape_requests = int(os.environ["escape_requests"])
        req_carga.set_desc_limits()

        count = 0
        while ((min_date >= offset_date and count <= max_requests) or escape_requests > 0) and count < 3:

            df_cargas = req_carga.get_dataframe_carga()
            list_viagem_carga = self.get_dataframe_single_viagem(df_cargas)
            df_via_acum = pd.concat([df_via_acum, list_viagem_carga[0]])
            df_carga_acum = pd.concat([df_carga_acum, list_viagem_carga[1]])

            if len(df_via_acum) > 0:
                min_date = self.check_mindate_dataframe(min_date, list_viagem_carga[0])

                if min_date < offset_date:
                    escape_requests -= 1


        df_carga_acum = self.filter_by_date(dataframe=df_carga_acum, colname="dt_emissao", date=offset_date)

        df_via_acum = self.filter_by_date(df_via_acum, "dt_final", offset_date)
        df_via_acum = self.df_handle.order_dataframe_by_column(dataframe=df_via_acum, column_name=["cd_viagem", "dt_final"])
        df_via_acum = self.df_handle.reindex_dataframe(dataframe=df_via_acum, list_columns_consider=["cd_viagem"])

        return [df_via_acum, df_carga_acum]

    def filter_by_date(self, dataframe, colname, date):
        dataframe[colname] = pd.to_datetime(dataframe[colname], format='%Y-%m-%d')
        dataframe = dataframe.loc[(dataframe[colname] >= date)]

        return dataframe

    def get_dataframe_single_viagem(self, df_cargas):
        df = pd.DataFrame()
        df_pedido = pd.DataFrame()
        for index in df_cargas.index:
            load_id = df_cargas['cd_carga'].iloc[index]
            order_id = df_cargas['cd_pedido'].iloc[index]
            list_viagem_carga = self.get_dataframe_w2params(
                nodelist_name="b:CargaIntegracao",
                flow_name="flow_viagem",
                load_id=load_id,
                order_id=order_id
            )
            df = pd.concat([df, list_viagem_carga[0]])
            df_pedido = pd.concat([df_pedido, list_viagem_carga[1]])
        if len(df) > 0:
            where = df["dt_final"].notnull()
            df = df[where]
        return [df, df_pedido]

    def check_mindate_dataframe(self, min_date, df):

        filter_df = self.df_handle.reindex_dataframe(df)
        min_date_df = filter_df["dt_final"].min()

        if pd.notna(min_date_df):
            return min_date_df
        else:
            return min_date


