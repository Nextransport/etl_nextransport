import xml.dom.minidom as Minidom
from datetime import date, datetime

class XmlHandle:

    xml_creator = Minidom.Document()


    def normalize_string(self, string_value):
        chars = {"'"}

        for char in chars:
            string_value = string_value.replace(char, "")

        return string_value

    def search_node_data(self, nodelist, nodes):
        if nodes is None:
            return None

        for nodeName in nodes:
            for node in nodelist:
                if node.nodeName == nodeName:
                    try:
                        return self.normalize_string(node.firstChild.data.upper())
                    except:
                        nodelist = node.childNodes
                        break
        return None

    def search_node_date(self, nodeList, nodes):
        str_timestamp = self.search_node_data(nodeList, nodes)
        if str_timestamp is None:
            return None

        if " " in str_timestamp:
            str_timestamp = str_timestamp.split(" ")
            str_date = str_timestamp[0]
            str_hours = str_timestamp[1]
        else:
            str_date = str_timestamp
            str_hours = ""

        if str_date[2] == "/" and str_date[5] == "/":
            str_timestamp = str_date.split("/")[2] + "-" + str_date.split("/")[1] + "-" + str_date.split("/")[0]

        if str_hours is not None:
            str_timestamp = str_timestamp + " " + str_hours

        return str_timestamp


    def create_header_xml_request(self, token, namespaces):
        envelope_xml = self.xml_creator.createElementNS('', 'soapenv:Envelope')

        for n in namespaces:
            envelope_xml.setAttribute('xmlns:' + n[0], n[1])

        header_xml = self.xml_creator.createElementNS('', 'soapenv:Header')
        token_xml = self.xml_creator.createElementNS('', 'Token')
        token_xml.setAttribute('xmlns', 'Token')
        token_xml.appendChild(self.xml_creator.createTextNode(token))
        header_xml.appendChild(token_xml)
        envelope_xml.appendChild(header_xml)

        return envelope_xml

    def create_body_xml_request(self, action, offset, limit, envelope_xml):
        body_xml = self.xml_creator.createElement('soapenv:Body')
        action_xml = self.xml_creator.createElementNS('', 'tem:' + action)

        inicio_xml = self.xml_creator.createElementNS('', 'tem:inicio')
        inicio_xml.appendChild(self.xml_creator.createTextNode(str(offset)))
        limite_xml = self.xml_creator.createElementNS('', 'tem:limite')
        limite_xml.appendChild(self.xml_creator.createTextNode(str(limit)))

        action_xml.appendChild(inicio_xml)
        action_xml.appendChild(limite_xml)

        body_xml.appendChild(action_xml)
        envelope_xml.appendChild(body_xml)

        return envelope_xml

    def create_body_xml_confirm_request(self, action, id_ext, envelope_xml):
        body_xml = self.xml_creator.createElement('soapenv:Body')
        action_xml = self.xml_creator.createElementNS('', 'tem:' + action)

        inicio_xml = self.xml_creator.createElementNS('', 'tem:protocolo')
        inicio_xml.appendChild(self.xml_creator.createTextNode(id_ext))

        action_xml.appendChild(inicio_xml)
        body_xml.appendChild(action_xml)
        envelope_xml.appendChild(body_xml)

        return envelope_xml

    def create_body_xml_carga_request(self, action, id_carga, id_pedido, envelope_xml):
        body_xml = self.xml_creator.createElement('soapenv:Body')
        action_xml = self.xml_creator.createElementNS('', 'tem:' + action)
        protocolo_xml = self.xml_creator.createElementNS('', 'tem:protocolo')

        id_carga_xml = self.xml_creator.createElementNS('', 'dom:protocoloIntegracaoCarga')
        id_carga_xml.appendChild(self.xml_creator.createTextNode(id_carga))
        id_pedido_xml = self.xml_creator.createElementNS('', 'dom:protocoloIntegracaoPedido')
        id_pedido_xml.appendChild(self.xml_creator.createTextNode(id_pedido))

        protocolo_xml.appendChild(id_carga_xml)
        protocolo_xml.appendChild(id_pedido_xml)
        action_xml.appendChild(protocolo_xml)
        body_xml.appendChild(action_xml)
        envelope_xml.appendChild(body_xml)

        return envelope_xml

    def create_body_xml_faturamento_request(self, action, offset, limit, envelope_xml, data_ini=None, data_fim=None):

        current_datetime = datetime.now()
        current_date = current_datetime.date()
        data_ini = date(2022, 1, 1)
        data_fim = date(current_date.year, 12, 31)

        body_xml = self.xml_creator.createElement('soapenv:Body')
        action_xml = self.xml_creator.createElementNS('', 'tem:' + action)

        dataini_xml = self.xml_creator.createElementNS('', 'tem:dataInicial')
        dataini_xml.appendChild(self.xml_creator.createTextNode(data_ini.strftime("%d/%m/%Y")))
        datafim_xml = self.xml_creator.createElementNS('', 'tem:dataFinal')
        datafim_xml.appendChild(self.xml_creator.createTextNode(data_fim.strftime("%d/%m/%Y")))

        offset_xml = self.xml_creator.createElementNS('', 'tem:inicio')
        offset_xml.appendChild(self.xml_creator.createTextNode(str(offset)))
        limit_xml = self.xml_creator.createElementNS('', 'tem:limite')
        limit_xml.appendChild(self.xml_creator.createTextNode(str(limit)))

        action_xml.appendChild(dataini_xml)
        action_xml.appendChild(datafim_xml)
        action_xml.appendChild(offset_xml)
        action_xml.appendChild(limit_xml)

        body_xml.appendChild(action_xml)
        envelope_xml.appendChild(body_xml)

        return envelope_xml

    def create_xml_request(self, token, namespaces, action, offset, limit):
        envelope_xml = self.create_header_xml_request(token, namespaces)
        envelope_xml = self.create_body_xml_request(action, offset, limit, envelope_xml)

        return envelope_xml.toxml()

    def create_xml_carga_request(self, token, namespaces, action, id_carga, id_pedido):
        envelope_xml = self.create_header_xml_request(token, namespaces)
        envelope_xml = self.create_body_xml_carga_request(action, id_carga, id_pedido, envelope_xml)

        return envelope_xml.toxml()

    def create_xml_faturamento_request(self, token, namespaces, action, offset, limit, data_ini=None, data_fim=None):
        envelope_xml = self.create_header_xml_request(token, namespaces)
        envelope_xml = self.create_body_xml_faturamento_request(action, offset, limit, envelope_xml, data_ini, data_fim)

        return envelope_xml.toxml()

    def create_xml_confirm_request(self, token, namespaces, action, id_ext):
        envelope_xml = self.create_header_xml_request(token, namespaces)
        envelope_xml = self.create_body_xml_confirm_request(action, id_ext, envelope_xml)

        return envelope_xml.toxml()
