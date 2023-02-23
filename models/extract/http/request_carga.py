from .request import Request
import pandas as pd

class RequestCarga(Request):

    def __init__(self):

        self.dataframe_results = pd.DataFrame()
        self.endpoint = "Cargas"
        self.action = "BuscarCargasPendentesIntegracao"
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
        self.set_qtd_registros()
        self.set_desc_limits()
        self.set_limit_dates()
        self.limit_type = "DESC"


    def get_dataframe_carga(self):

        df = self.get_dataframe_with_nodate(nodelist_name="b:Protocolos", flow_name="flow_carga")
        return df