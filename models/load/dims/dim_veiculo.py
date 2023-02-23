from .dimension import Dimension

class DimVeiculo(Dimension):

    def __init__(self):
        self.table_name = "stg_dim_veiculo"
        self.fk_name = "cd_veiculo"
        self.undo_renamecols = True
        self.dim_columns = [
            "sk",
            "cd_cliente",
            "cd_veiculo",
            "ds_tipoveiculo",
            "ds_placa",
            "ds_chassi",
            "ds_renavam",
            "ds_marca",
            "ds_modelo",
            "nr_anofabricacao",
            "nr_anomodelo",
            "dt_aquisicao",
            "nr_frota",
            "ds_frota",
            "nr_versao",
            "dt_criacao",
            "dt_atualizacao"
        ]
        self.flow_columns = [
            "cd_veiculo",
            "ds_tipoveiculo",
            "ds_placa",
            "ds_chassi",
            "ds_renavam",
            "ds_marca",
            "ds_modelo",
            "nr_anofabricacao",
            "nr_anomodelo",
            "dt_aquisicao",
            "nr_frota",
            "ds_frota"
        ]
        self.exchange_columns = {
            "cd_veiculoreboque": "cd_veiculo",
            "ds_tipoveiculoreboque": "ds_tipoveiculo",
            "ds_placareboque": "ds_placa",
            "ds_chassireboque": "ds_chassi",
            "ds_renavamreboque": "ds_renavam",
            "ds_marcareboque": "ds_marca",
            "ds_modeloreboque": "ds_modelo",
            "nr_anofabricacaoreboque": "nr_anofabricacao",
            "nr_anomodeloreboque": "nr_anomodelo",
            "dt_aquisicaoreboque": "dt_aquisicao",
            "nr_frotareboque": "nr_frota",
            "ds_frotareboque": "ds_frota"
        }
        self.unique_columns = self.dim_columns
        Dimension.__init__(self)




