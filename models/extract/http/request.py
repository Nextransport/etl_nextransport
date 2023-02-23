import xml.dom.minidom as dom
import requests
import pandas as pd
import os
import re
from models.transform.xml.xml_handle import XmlHandle
from models.transform.dataframe.dataframe_handle import DataframeHandle
from datetime import date, datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class Request:

    wsdl = os.environ["wsdl"]
    token = os.environ["token"]
    endpoint = ''
    action = ''
    body = ''
    headers = ''
    xml_handle = XmlHandle()
    df_handle = DataframeHandle()
    qtd_registros = 0
    namespaces = ()
    offset = 0
    offset_days = 0
    offset_date = 0
    today_date = 0
    limit = 0
    dataframe_results = 0
    limit_type = "ASC"

    def set_limit_dates(self):
        self.today_date = date.today()
        self.offset_days = timedelta(int(os.environ["offset_days"]))
        self.offset_date = self.today_date - self.offset_days

    def set_headers_request(self):
        self.wsdl = os.environ["wsdl"] + self.endpoint + '.svc'
        self.headers = {
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'http://tempuri.org/I' + self.endpoint + '/' + self.action
        }

    def restart_limits(self):
        self.offset = 0
        self.limit = 1

    def reset_limits(self):
        self.offset = 0
        self.limit = 0

    def set_asc_limits(self):
        self.offset = int(os.environ[f"Offset_{self.action}"])
        self.limit = int(os.environ[f"Limit_{self.action}"])

    def set_desc_limits(self):
        self.offset = self.qtd_registros - int(os.environ[f"Limit_{self.action}"])
        self.limit = int(os.environ[f"Limit_{self.action}"])
    def post_request(self):
        try:
            print(f"Buscando registros em '{self.action}': de {self.offset} a {self.limit+self.offset}...")
            self.body = self.xml_handle.create_xml_request(self.token, self.namespaces, self.action, self.offset, self.limit)
            response = requests.request("POST", url=self.wsdl, headers=self.headers, data=self.body)
            response_txt = re.sub(r'&#([a-zA-Z0-9]+);?', "", response.content.decode("utf-8"))
            return response_txt
        except Exception as e:
            print(e)
            exit()

    def post_request_fatur(self):
        try:
            print(f"Buscando registros em '{self.action}': de {self.offset} a {self.limit+self.offset}...")
            self.body = self.xml_handle.create_xml_faturamento_request(self.token, self.namespaces, self.action, self.offset, self.limit)
            response = requests.request("POST", url=self.wsdl, headers=self.headers, data=self.body)
            response_txt = re.sub(r'&#([a-zA-Z0-9]+);?', "", response.content.decode("utf-8"))
            return response_txt
        except Exception as e:
            print(e)
            exit()

    def post_request_viagem(self, load_id, order_id):
        try:
            # print(f"Buscando registros em '{self.action}': de {self.offset + self.limit} a {self.offset}")
            self.body = self.xml_handle.create_xml_carga_request(self.token, self.namespaces, self.action, load_id, order_id)
            response = requests.request("POST", url=self.wsdl, headers=self.headers, data=self.body)
            response_txt = re.sub(r'&#([a-zA-Z0-9]+);?', "", response.content.decode("utf-8"))
            return response_txt
        except Exception as e:
            print(e)
            exit()
    def get_response_xml(self):
        return dom.parseString(self.post_request())

    def get_response_xml_viagem(self, load_id, order_id):
        return dom.parseString(self.post_request_viagem(load_id=load_id, order_id=order_id))

    def get_response_xml_fatur(self):
        return dom.parseString(self.post_request_fatur())

    def get_response_xml_by_tag_name(self, tag_name, fl_viagem=None, load_id=None, order_id=None, fl_fatur=None):
        if fl_viagem is True:
            data_xml = self.get_response_xml_viagem(load_id, order_id)
        elif fl_fatur is True:
            data_xml = self.get_response_xml_fatur()
        else:
            data_xml = self.get_response_xml()

        return data_xml.getElementsByTagName(tag_name)

    def get_response_txt(self):
        return self.post_request()

    def set_qtd_registros(self, fl_fatur=None):
        self.restart_limits()
        self.set_headers_request()

        if fl_fatur is True:
            self.body = self.xml_handle.create_xml_faturamento_request(self.token, self.namespaces, self.action, self.offset, self.limit)
            response_xml = self.get_response_xml_fatur()
        else:
            self.body = self.xml_handle.create_xml_request(self.token, self.namespaces, self.action, self.offset,self.limit)
            response_xml = self.get_response_xml()

        node_qtd_registros = response_xml.getElementsByTagName("a:NumeroTotalDeRegistro")

        if node_qtd_registros == []:
            node_qtd_registros = response_xml.getElementsByTagName("b:NumeroTotalDeRegistro")

        self.qtd_registros = int(node_qtd_registros[0].firstChild.nodeValue)


    def get_dataframe(self, nodelist_name, flow_name, date_nodename, date_colname, fl_fatur=None):

        fl_escape = int(os.environ["escape_requests"])
        max_requests = int(os.environ["max_requests"])
        dataframe_results = pd.DataFrame()

        min_date = datetime.today()
        offset_days = timedelta(int(os.environ["offset_days"]))
        offset_date = min_date - offset_days
        count = 0
        df_handle = DataframeHandle()

        while self.get_offset_condition() and fl_escape > 0 and count <= max_requests:

            node_list = self.get_response_xml_by_tag_name(tag_name=nodelist_name, fl_fatur=fl_fatur)

            if len(node_list) == 0:
                self.reset_offset_condition()

            len_df_before = len(dataframe_results)
            df = df_handle.proccess_data_xml(node_list, date_nodename, offset_date, flow_name)
            print('Min data:', df[date_colname].min())
            dataframe_results = pd.concat([dataframe_results, df])
            len_df_after = len(dataframe_results)

            print('Len node_list:', len(node_list))
            print('Len df:', len(df))
            print('Len dataframe_results:', len(dataframe_results))

            if (len_df_after - len_df_before) == 0 and len(node_list) > 0:
                fl_escape -= 1

            self.set_offset_condition()
            count += 1

        self.dataframe_results = df_handle.reindex_dataframe(dataframe_results)

        return self.dataframe_results

    def get_offset_condition(self):
        if self.limit_type == "ASC":
            return (self.offset + self.limit) < self.qtd_registros
        else:
            return self.offset >= 0

    def set_offset_condition(self):
        if self.limit_type == "ASC":
            self.offset += self.limit
        else:
            self.offset -= self.limit

    def reset_offset_condition(self):
        if self.limit_type == "ASC":
            self.offset -= self.limit
        else:
            self.offset += self.limit

    def get_dataframe_with_nodate(self, nodelist_name, flow_name):

        fl_escape = int(os.environ["escape_requests"])
        max_requests = 0
        count = 0
        df_handle = DataframeHandle()
        dataframe_results = pd.DataFrame()

        while self.offset >= 0 and fl_escape > 0 and count <= max_requests:
            node_list = self.get_response_xml_by_tag_name(tag_name=nodelist_name)
            len_df_before = len(self.dataframe_results.index)
            dataframe_results = df_handle.proccess_data_xml(node_list, None, self.offset_date, flow_name)
            len_df_after = len(self.dataframe_results.index)

            if (len_df_after - len_df_before) == 0:
                fl_escape -= 1
            self.offset -= self.limit

            count += 1

        dataframe_results = df_handle.reindex_dataframe(dataframe_results)
        return dataframe_results

    def get_dataframe_w2params(self, nodelist_name, flow_name, load_id, order_id):

        df_handle = DataframeHandle()
        print(f"Buscando carga {load_id}/{order_id}.")
        node_list = self.get_response_xml_by_tag_name(tag_name=nodelist_name, fl_viagem=True, load_id=load_id, order_id=order_id)
        df = df_handle.proccess_data_xml(node_list, None, self.offset_date, flow_name)

        return df

    def get_node_text(self, node_list, node_names):
        return self.xml_handle.search_node_data(node_list, node_names)

    def get_node_date(self, node_list, node_names):
        return self.xml_handle.search_node_date(node_list, node_names)
