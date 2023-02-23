from .request import Request
import pandas as pd

class RequestAbastecimento(Request):

    def __init__(self):

        self.dataframe_results = pd.DataFrame()
        self.endpoint = "Empresa"
        self.action = "BuscarAbastecimentosPendentesIntegracao"
        self.namespaces = (
            ['soapenv', 'http://schemas.xmlsoap.org/soap/envelope/'],
            ['tem', 'http://tempuri.org/']
        )
        self.set_qtd_registros()
        self.set_asc_limits()
        self.set_limit_dates()


    def get_dataframe_abas(self):
        return self.get_dataframe(nodelist_name="b:ConsultaAbastecimento", flow_name="flow_abastecida_cavalo", date_nodename="b:Data", date_colname="dt_emissao")
