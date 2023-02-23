from .request import Request
import pandas as pd

class RequestTabelaPreco(Request):

    def __init__(self):

        self.dataframe_results = pd.DataFrame()
        self.endpoint = "Empresa"
        self.action = "BuscarTabelaPostoPendentesIntegracao"
        self.namespaces = (
            ['soapenv', 'http://schemas.xmlsoap.org/soap/envelope/'],
            ['tem', 'http://tempuri.org/']
        )
        self.set_qtd_registros()
        self.set_asc_limits()
        self.set_limit_dates()


    def get_dataframe_tab(self):
        return self.get_dataframe(nodelist_name="b:TabelaPosto", flow_name="flow_tabelapreco", date_nodename="b:DataInicial", date_colname="dt_inicial")
