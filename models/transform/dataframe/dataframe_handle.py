import pandas

from models.transform.xml.xml_handle import XmlHandle
from .dataframe_define import DataframeDefine
import pandas as pd
import numpy as np

class DataframeHandle():

    xml_handle = XmlHandle()
    def get_node_text(self, node_list, node_names):
        return self.xml_handle.search_node_data(node_list, node_names)

    def get_node_date(self, node_list, node_names):
        return self.xml_handle.search_node_date(node_list, node_names)

    def check_index_exists(self, index_name, list):
        try:
            aux = list[index_name]
            return True
        except IndexError:
            return False

    def proccess_data_xml(self, node_list, date_nodename, offset_date, flow_name):
        cols = DataframeDefine.columns[flow_name]
        cd_equipto = None
        dataframe_results = pd.DataFrame(columns=list(cols))

        for node in node_list:

            childs = node.childNodes
            dt_emissao = pd.to_datetime(self.get_node_date(childs, [date_nodename]))

            if "flow_abastecida" in flow_name:
                cd_equipto = self.get_node_text(childs, ["b:Equipamento", "b:Codigo"])
                if cd_equipto is not None:
                    cols = DataframeDefine.columns["flow_abastecida_equipamento"]

            if dt_emissao is None or dt_emissao >= pd.to_datetime(offset_date):
                df = pd.DataFrame(columns=list(cols))

                for index in list(cols):
                    prefix = ""
                    if cols[index] is not None:
                        prefix = cols[index][0]
                        if "prefix:" in prefix:
                            prefix = prefix.split(":")[1]

                    if "dt_" not in index:

                        if isinstance(cols[index], str):
                            df.at[0, index] = cols[index]
                        else:
                            value = self.get_node_text(childs, cols[index])
                            df.at[0, index] = prefix + value if value is not None else value
                    else:
                        try:
                            dt = pd.to_datetime(self.get_node_date(childs, cols[index]))
                            df.at[0, index] = dt if pd.notna(dt) else None
                        except:
                            df.at[0, index] = None

                dataframe_results = pd.concat([dataframe_results, df])

        return dataframe_results

    def reindex_dataframe(self, dataframe, list_columns_consider=None, filter=None):

        if not isinstance(dataframe, pandas.DataFrame):
            dataframe = pd.DataFrame(dataframe)

        if filter is not None:
            dataframe = dataframe.dropna(subset=filter)

        dataframe = dataframe.drop_duplicates(subset=list_columns_consider).copy()

        if len(dataframe) > 1:
            dataframe = dataframe.reset_index(drop=True)

        return dataframe

    def concat_daframe(self, dataframe1, dataframe2):

        dataframe1 = dataframe1.reset_index(drop=True)
        dataframe1 = pd.concat([dataframe1, dataframe2])

        return dataframe1

    def rename_column(self, dataframe, old_name, new_name):
        return dataframe.rename(columns={old_name: new_name})

    def rename_columns(self, exchange_columns, dataframe):
        for index in exchange_columns:
            dataframe = self.rename_column(dataframe, index, exchange_columns[index])
        return dataframe

    def order_dataframe_by_column(self, dataframe, column_name):
        return dataframe.sort_values(by=column_name, ascending=True)

    def row2series(self, row, columns):
        count = 0
        sr = pd.Series(index=columns, dtype="float64")
        for col in columns:
            sr[col] = row[count]
            count += 1

        return sr

    def row2frame(self, row, columns):
        count = 0
        df = pd.DataFrame(columns=columns)
        for col in columns:
            df.at[0, col] = row[count]
            count += 1

        return df