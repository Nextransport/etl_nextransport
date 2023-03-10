import os
import logging
import pandas as pd
from datetime import datetime, date

from models.extract.http.request_abastecimento import RequestAbastecimento
from models.extract.http.request_pedidofrete import RequestPedidoFrete
from models.extract.http.request_faturamento import RequestFaturamento
from models.extract.http.request_manutencao import RequestManutencao
from models.extract.http.request_tabelapreco import RequestTabelaPreco

from models.transform.stage.stage_dim_relacionado import StageDimRelacionado
from models.transform.stage.stage_dim_viagem import StageDimViagem
from models.transform.dataframe.dataframe_storage import DataframeStorage

logging.basicConfig(filename=f'./log/{date.today()}.log', encoding='utf-8', level=logging.INFO)

def init():
    client_id = 1
    df_st = DataframeStorage()
    ts = datetime.now()
    logging.info(f"Inicio: {ts.strftime('%H:%M:%S')}")

    extract(df_st)
    dim_load(df_st, client_id)
    fct_load(df_st, client_id)

    ts = datetime.now()
    logging.info(f"Final: {ts.strftime('%H:%M:%S')}")

def extract(df_st):

    request_abastecimento(df_st)
    request_pedidofrete(df_st)
    request_faturamento(df_st)
    request_manutencao(df_st)
    request_tabelapreco(df_st)

def dim_load(df_st, client_id):

    print("Carregando informações em stg_dim_produto")
    df_st.stg_dim_produto.truncate_table()
    df_st.stg_dim_produto.insert_update_data(client_id=client_id, dataframe=df_st.df_produto, unique_cols=["cd_produto"])

    print("Carregando informações em stg_dim_relacionado")
    df_st.stg_dim_relacionado.truncate_table()
    df_st.stg_dim_relacionado.insert_update_data(client_id=client_id, dataframe=df_st.df_relacionado, unique_cols=["cd_relacionado"])

    print("Carregando informações em stg_dim_veiculo")
    df_st.stg_dim_veiculo.truncate_table()
    df_st.stg_dim_veiculo.insert_update_data(client_id=client_id, dataframe=df_st.df_veiculo, unique_cols=["ds_placa"])

    print("Carregando informações em stg_dim_pedidofrete")
    df_st.stg_dim_pedidofrete.truncate_table()
    df_st.stg_dim_pedidofrete.insert_update_data(client_id=client_id, dataframe=df_st.df_pedidofrete[df_st.stg_dim_pedidofrete.stage_cols], unique_cols=["cd_pedidofrete"])

    print("Carregando informações em stg_dim_viagem")
    df_st.stg_dim_viagem.truncate_table()
    df_st.stg_dim_viagem.insert_update_data(client_id=client_id, dataframe=df_st.df_viagem)

    print("Carregando informações em stg_dim_motorista")
    df_st.stg_dim_motorista.truncate_table()
    df_st.stg_dim_motorista.insert_update_data(client_id=client_id, dataframe=df_st.df_motorista, unique_cols=["ds_cpf"])

    print("Carregando informações em stg_dim_manutencao")
    df_st.stg_dim_manutencao.truncate_table()
    df_st.stg_dim_manutencao.insert_update_data(client_id=client_id, dataframe=df_st.df_manutencao)

def fct_load(df_st, client_id):

    df_st.stg_fact_abastecimento.truncate_table()
    df_st.stg_fact_abastecimento.insert_stg_data(client_id=client_id, dataframe=df_st.df_abastecimento)

    df_st.stg_fact_viagem.truncate_table()
    df_st.stg_fact_viagem.insert_stg_data(client_id=client_id, dataframe=df_st.df_viagem[df_st.stg_fact_viagem.stage_cols])

    df_st.stg_fact_pedidofrete.truncate_table()
    df_st.stg_fact_pedidofrete.insert_stg_data(client_id=client_id, dataframe=df_st.df_pedidofrete[df_st.stg_fact_pedidofrete.stage_cols])

    df_st.stg_fact_manutencao.truncate_table()
    df_st.stg_fact_manutencao.insert_stg_data(client_id=client_id, dataframe=df_st.df_manutencao[df_st.stg_fact_manutencao.stage_cols])

    df_st.stg_fact_faturamento.truncate_table()
    df_st.stg_fact_faturamento.insert_stg_data(client_id=client_id, dataframe=df_st.df_faturamento[df_st.stg_fact_faturamento.stage_cols])

    df_st.stg_fact_tabelapreco.truncate_table()
    df_st.stg_fact_tabelapreco.insert_stg_data(client_id=client_id, dataframe=df_st.df_tabelapreco[df_st.stg_fact_tabelapreco.stage_cols])

def request_abastecimento(df_st):
    request = RequestAbastecimento()
    df_abas = request.get_dataframe_abas()

    if len(df_abas) > 0:
        df_st.df_relacionado = pd.concat([df_st.df_relacionado, df_abas[df_st.stg_dim_relacionado.stage_cols]])

        df_motorista = df_abas[df_st.stg_dim_motorista.flow_columns]
        df_st.df_motorista = pd.concat([df_st.df_motorista, df_motorista.rename(columns=df_st.stg_dim_motorista.exchange_columns)])

        df_st.df_produto = pd.concat([df_st.df_produto, df_abas[df_st.stg_dim_produto.stage_cols]])

        df_st.df_veiculo = pd.concat([df_st.df_veiculo, df_abas[df_st.stg_dim_veiculo.stage_cols]])

        df_st.df_abastecimento = pd.concat([df_st.df_abastecimento, df_abas])

def request_pedidofrete(df_st):

    request = RequestPedidoFrete()
    df_pedidofrete_viagem = request.get_dataframe_pedidofrete()
    df_pedidofrete = df_pedidofrete_viagem[0]
    df_viagem = df_pedidofrete_viagem[1]

    if len(df_pedidofrete) > 0:
        df_motorista = df_pedidofrete[df_st.stg_dim_motorista.flow_columns]
        df_st.df_motorista = pd.concat([df_st.df_motorista, df_motorista.rename(columns=df_st.stg_dim_motorista.exchange_columns)])

        df_st.df_relacionado = pd.concat([df_st.df_relacionado, df_pedidofrete[df_st.stg_dim_relacionado.stage_cols]])

        df_st.df_veiculo = pd.concat([df_st.df_veiculo, df_pedidofrete[df_st.stg_dim_veiculo.stage_cols]])

        df_reboque = df_pedidofrete[df_st.stg_dim_veiculo.exchange_columns.keys()]
        df_st.df_veiculo = pd.concat([df_st.df_veiculo, df_reboque.rename(columns=df_st.stg_dim_veiculo.exchange_columns)])

        df_pedidofrete["cd_pedidofrete"] = df_pedidofrete["cd_carga"] + "-" + df_pedidofrete["cd_pedido"]
        df_st.df_pedidofrete = pd.concat([df_st.df_pedidofrete, df_pedidofrete])

        df_st.df_viagem = pd.concat([df_st.df_viagem, df_viagem[df_st.stg_fact_viagem.stage_cols]])
        df_st.df_viagem.drop_duplicates(inplace=True)


def request_faturamento(df_st):
    request = RequestFaturamento()
    df_fat = request.get_dataframe_fatu()

    if len(df_fat) > 0:
        df_motorista = df_fat[df_st.stg_dim_motorista.flow_columns]
        df_st.df_motorista = pd.concat([df_st.df_motorista, df_motorista.rename(columns=df_st.stg_dim_motorista.exchange_columns)])

        df_st.df_veiculo = pd.concat([df_st.df_veiculo, df_fat[df_st.stg_dim_veiculo.stage_cols]])

        df_reboque = df_fat[df_st.stg_dim_veiculo.exchange_columns.keys()]
        df_st.df_veiculo = pd.concat([df_st.df_veiculo, df_reboque.rename(columns=df_st.stg_dim_veiculo.exchange_columns)])

        df_st.df_faturamento = pd.concat([df_st.df_faturamento, df_fat[df_st.stg_fact_faturamento.stage_cols]])

        df_st.df_relacionado = pd.concat([df_st.df_relacionado, df_fat[df_st.stg_dim_relacionado.stage_cols]])

def request_manutencao(df_st):
    request = RequestManutencao()
    df_man = request.get_dataframe_manu()

    if len(df_man) > 0:
        df_motorista = df_man[df_st.stg_dim_motorista.flow_columns]
        df_st.df_motorista = pd.concat([df_st.df_motorista, df_motorista.rename(columns=df_st.stg_dim_motorista.exchange_columns)])

        df_st.df_veiculo = pd.concat([df_st.df_veiculo, df_man[df_st.stg_dim_veiculo.stage_cols]])

        df_st.df_relacionado = pd.concat([df_st.df_relacionado, df_man[df_st.stg_dim_relacionado.stage_cols]])

        df_st.df_produto = pd.concat([df_st.df_produto, df_man[df_st.stg_dim_produto.stage_cols]])

        df_st.df_manutencao = pd.concat([df_st.df_manutencao, df_man])

def request_tabelapreco(df_st):
    request = RequestTabelaPreco()
    df_tab = request.get_dataframe_tab()

    if len(df_tab) > 0:
        df_st.df_relacionado = pd.concat([df_st.df_relacionado, df_tab[df_st.stg_dim_relacionado.stage_cols]])

        df_st.df_produto = pd.concat([df_st.df_produto, df_tab[df_st.stg_dim_produto.stage_cols]])

        df_st.df_tabelapreco = pd.concat([df_st.df_tabelapreco, df_tab[df_st.stg_fact_tabelapreco.stage_cols]])

init()
