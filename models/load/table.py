import pandas as pd
import sqlalchemy
from sqlalchemy import text, Connection
from models.transform.dataframe.dataframe_handle import DataframeHandle
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

class Table:

    schema = ""
    stage_schema = ""
    flow_columns = []
    dt_col_name = ""
    sk_name = ""
    fk_name = ""
    table_name = ""
    flow_dataframe = pd.DataFrame()
    df_handle = DataframeHandle()
    engine = ""

    def __init__(self):
        self.table_name = self.schema + "." + self.table_name
        eng_string = "postgresql+psycopg2://"
        eng_string += f"{os.environ['db_user']}:{os.environ['db_passwd']}@{os.environ['db_host']}/{os.environ['db_name']}"
        self.engine = sqlalchemy.create_engine(eng_string)

    def truncate_table(self, offset_date=None, limit_date=None):

        query = f"delete from {self.table_name}"
        txt_success = f"Tabela {self.table_name} truncada"

        if offset_date is not None:
            query += f" where {self.dt_col_name} >= '{offset_date}'"
            txt_success += f" a partir de {offset_date}"

        if limit_date is not None:
            query += f" and {self.dt_col_name} <= '{limit_date}'"
            txt_success += f" até {limit_date}"

        try:
            self.exec_sql(query)
            print(txt_success)
        except Exception as e:
            print(f"Nao foi possivel truncar a tabela {self.table_name}: {e}")
            exit()

    def truncate_table_after_offset(self):
        today = datetime.today()
        offset_days = timedelta(int(os.environ["offset_days"]))
        offset_date = (today - offset_days).strftime("%Y-%m-%d")
        limit_date = os.environ["limit_date"]

        self.truncate_table(offset_date=offset_date, limit_date=limit_date)

    def exec_sql(self, sql):
        with self.engine.connect() as con:
            con.execute(text(sql))
            con.commit()