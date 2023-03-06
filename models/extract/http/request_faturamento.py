from .request import Request
import pandas as pd

class RequestFaturamento(Request):

    def __init__(self):

        self.dataframe_results = pd.DataFrame()
        self.endpoint = "CTe"
        self.action = "BuscarCTesPorPeriodo"
        self.namespaces = (
            ['soapenv', 'http://schemas.xmlsoap.org/soap/envelope/'],
            ['tem', 'http://tempuri.org/']
        )
        self.set_qtd_registros(fl_fatur=True)
        self.set_desc_limits()
        self.set_limit_dates()


    def get_dataframe_fatu(self):
        return self.get_dataframe(nodelist_name="b:CTe", flow_name="flow_faturamento", date_nodename="b:DataEmissao", date_colname="dt_emissao", fl_fatur=True)