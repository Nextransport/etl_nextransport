from .request import Request
import pandas as pd

class RequestManutencao(Request):

    def __init__(self):

        self.dataframe_results = pd.DataFrame()
        self.endpoint = "Empresa"
        self.action = "BuscarOrdemServicoFinalizacaPendenteIntegracao"
        self.namespaces = (
            ['soapenv', 'http://schemas.xmlsoap.org/soap/envelope/'],
            ['tem', 'http://tempuri.org/']
        )
        self.set_qtd_registros()
        self.set_asc_limits()
        self.set_limit_dates()


    def get_dataframe_manu(self):
        return self.get_dataframe(nodelist_name="b:OrdemServico", flow_name="flow_manutencao", date_nodename="b:DataFechamento", date_colname="dt_emissao")
