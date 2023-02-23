import pandas as pd

from models.load.dims.dim_relacionado import DimRelacionado
from models.load.dims.dim_motorista import DimMotorista
from models.load.dims.dim_produto import DimProduto
from models.load.dims.dim_veiculo import DimVeiculo
from models.load.dims.dim_viagem import DimViagem
from models.load.dims.dim_manutencao import DimManutencao

from models.load.facts.fact_abastecimento import FactAbastecimento
from models.load.facts.fact_viagem import FactViagem
from models.load.facts.fact_faturamento import FactFaturamento
from models.load.facts.fact_manutencao import FactManutencao
from models.load.facts.fact_tabelapreco import FactTabelaPreco

from models.transform.stage.stage_dim_manutencao import StageDimManutencao
from models.transform.stage.stage_dim_motorista import StageDimMotorista
from models.transform.stage.stage_dim_produto import StageDimProduto
from models.transform.stage.stage_dim_relacionado import StageDimRelacionado
from models.transform.stage.stage_dim_veiculo import StageDimVeiculo
from models.transform.stage.stage_dim_viagem import StageDimViagem

from models.transform.stage.stage_fact_abastecimento import StageFactAbastecimento
from models.transform.stage.stage_fact_faturamento import StageFactFaturamento
from models.transform.stage.stage_fact_manutencao import StageFactManutencao
from models.transform.stage.stage_fact_tabelapreco import StageFactTabelaPreco
from models.transform.stage.stage_fact_viagem import StageFactViagem

class DataframeStorage:

    df_abastecimento = pd.DataFrame()
    df_faturamento = pd.DataFrame()
    df_manutencao = pd.DataFrame()
    df_motorista = pd.DataFrame()
    df_produto = pd.DataFrame()
    df_relacionado = pd.DataFrame()
    df_tabelapreco = pd.DataFrame()
    df_veiculo = pd.DataFrame()
    df_viagem = pd.DataFrame()

    dim_motorista = DimMotorista()
    dim_produto = DimProduto()
    dim_relacionado = DimRelacionado()

    stg_dim_relacionado = StageDimRelacionado()
    stg_dim_motorista = StageDimMotorista()
    stg_dim_produto = StageDimProduto()
    stg_dim_veiculo = StageDimVeiculo()
    stg_dim_viagem = StageDimViagem()
    stg_dim_manutencao = StageDimManutencao()

    stg_fact_abastecimento = StageFactAbastecimento()
    stg_fact_faturamento = StageFactFaturamento()
    stg_fact_manutencao = StageFactManutencao()
    stg_fact_tabelapreco = StageFactTabelaPreco()
    stg_fact_viagem = StageFactViagem()

