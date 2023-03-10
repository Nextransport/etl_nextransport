
class DataframeDefine:
    
    columns = {
        "flow_abastecida_cavalo": {
            "cd_abastecimento": ["prefix:", "prefix:", "b:Codigo"],
            "nr_notafiscal": ["prefix:", "b:Documento"],
            "dt_emissao": ["prefix:", "b:Data"],
            "cd_relacionado": ["prefix:FC", "b:Posto", "c:CodigoIntegracao"],
            "ds_cnpjcpf": ["prefix:", "b:Posto", "c:CPFCNPJ"],
            "ds_ierg": ["prefix:", "b:Posto", "c:RGIE"],
            "ds_nomerazaosocial": ["prefix:", "b:Posto", "c:RazaoSocial"],
            "ds_nomefantasia": ["prefix:", "b:Posto", "c:NomeFantasia"],
            "ds_email": ["prefix:", "b:Posto", "c:Email"],
            "ds_telefone1": ["prefix:", "b:Posto", "c:Endereco", "d:Telefone"],
            "ds_telefone2": ["prefix:", "b:Posto", "c:Endereco", "d:Telefone2"],
            "ds_endereco": ["prefix:", "b:Posto", "c:Endereco", "d:Logradouro"],
            "ds_cep": ["prefix:", "b:Posto", "c:Endereco", "d:CEP"],
            "ds_latitude": ["prefix:", "b:Posto", "c:Endereco", "d:Latitude"],
            "ds_longitude": ["prefix:", "b:Posto", "c:Endereco", "d:Longitude"],
            "dt_nascfundacao": None,
            "ds_cidade": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_uf": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_pais": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "ds_grupo": ["prefix:", "b:Posto", "c:NomeFantasia"],
            "cd_produto": ["prefix:", "b:Produto", "c:Codigo"],
            "ds_produto": ["prefix:", "b:Produto", "c:Descricao"],
            "ds_ncm": ["prefix:", "b:Produto", "c:NCM"],
            "ds_undmedida": "LITRO",
            "cd_veiculo": ["prefix:", "b:Veiculo", "b:Codigo"],
            "ds_placa": ["prefix:", "b:Veiculo", "b:Placa"],
            "ds_nrfrota": ["prefix:", "b:Veiculo", "b:NumeroFrota"],
            "ds_chassi": ["prefix:", "b:Veiculo", "b:NumeroChassi"],
            "ds_renavam": ["prefix:", "b:Veiculo", "b:Renavam"],
            "nr_anofabricacao": ["prefix:", "b:Veiculo", "b:AnoFabricacao"],
            "nr_anomodelo": ["prefix:", "b:Veiculo", "b:AnoModelo"],
            "ds_marca": ["prefix:", "b:Veiculo", "b:Modelo", "b:Marca", "b:Descricao"],
            "ds_modelo": ["prefix:", "b:Veiculo", "b:Modelo", "b:Descricao"],
            "ds_tipoveiculo": ["prefix:", "b:Veiculo", "b:TipoVeiculo"],
            "ds_frota": ["prefix:", "b:Veiculo", "b:SegmentoVeiculo", "b:Descricao"],
            "nr_frota": ["prefix:", "b:Veiculo", "b:NumeroFrota"],
            "dt_aquisicao": ["prefix:", "b:Veiculo", "b:DataAquisicao"],
            "nr_km": ["prefix:", "b:Kilometragem"],
            "nr_horimetro": ["prefix:", "b:Horimetro"],
            "nr_litros": ["prefix:", "b:Litros"],
            "nr_quantidade": ["prefix:", "b:Litros"],
            "nr_valorunitario": ["prefix:", "b:ValorUnitario"],
            "nr_preco": ["prefix:", "b:ValorUnitario"],
            "nr_valortotal": ["prefix:", "b:ValorTotal"],
            "cd_viagem": ["prefix:", "b:NumeroAcerto"],
            "cd_motorista": ["prefix:", "b:Motorista", "c:Codigo"],
            "ds_nomemotorista": ["prefix:", "b:Motorista", "c:Nome"],
            "ds_cpf":  ["prefix:", "b:Motorista", "c:CPF"],
            "ds_rg":  ["prefix:", "b:Motorista", "c:RG"],
            "dt_nascimento":  ["prefix:", "b:Motorista", "c:DataNascimento"],
            "ds_estadocivil":  ["prefix:", "b:Motorista", "c:EstadoCivil"],
            "ds_enderecomotorista":  ["prefix:", "b:Motorista", "c:Endereco", "d:Logradouro"],
            "ds_cidademotorista":  ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_ufmotorista":  ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_paismotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "fl_ativo": None
        },
        "flow_abastecida_equipamento": {
            "cd_abastecimento": ["prefix:", "b:Codigo"],
            "nr_notafiscal": ["prefix:", "b:Documento"],
            "dt_emissao": ["prefix:", "b:Data"],
            "cd_relacionado": ["prefix:FC", "b:Posto", "c:CodigoIntegracao"],
            "ds_cnpjcpf": ["prefix:", "b:Posto", "c:CPFCNPJ"],
            "ds_ierg": ["prefix:", "b:Posto", "c:RGIE"],
            "ds_nomerazaosocial": ["prefix:", "b:Posto", "c:RazaoSocial"],
            "ds_nomefantasia": ["prefix:", "b:Posto", "c:NomeFantasia"],
            "ds_email": ["prefix:", "b:Posto", "c:Email"],
            "ds_telefone1": ["prefix:", "b:Posto", "c:Endereco", "d:Telefone"],
            "ds_telefone2": ["prefix:", "b:Posto", "c:Endereco", "d:Telefone2"],
            "ds_endereco": ["prefix:", "b:Posto", "c:Endereco", "d:Logradouro"],
            "ds_cep": ["prefix:", "b:Posto", "c:Endereco", "d:CEP"],
            "ds_latitude": ["prefix:", "b:Posto", "c:Endereco", "d:Latitude"],
            "ds_longitude": ["prefix:", "b:Posto", "c:Endereco", "d:Longitude"],
            "dt_nascfundacao": None,
            "ds_cidade": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_uf": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_pais": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "ds_grupo": ["prefix:", "b:Posto", "c:NomeFantasia"],
            "cd_produto": ["prefix:", "b:Produto", "c:Codigo"],
            "ds_produto": ["prefix:", "b:Produto", "c:Descricao"],
            "ds_ncm": ["prefix:", "b:Produto", "c:NCM"],
            "ds_undmedida": "LITRO",
            "cd_veiculo": ["prefix:E", "b:Equipamento", "b:Codigo"],
            "ds_placa": ["prefix:", "b:Equipamento", "b:Descricao"],
            "ds_nrfrota": ["prefix:", "b:Equipamento", "b:Numero"],
            "ds_chassi": "N??O INFORMADO",
            "ds_renavam": "N??O INFORMADO",
            "nr_anofabricacao": ["prefix:", "b:Equipamento", "b:AnoFabricacao"],
            "nr_anomodelo": ["prefix:", "b:Equipamento", "b:AnoModelo"],
            "ds_marca": ["prefix:", "b:Equipamento", "b:Marca"],
            "ds_modelo": ["prefix:", "b:Equipamento", "b:Modelo"],
            "ds_tipoveiculo": "EQUIPAMENTO",
            "ds_frota": ["prefix:", "b:Equipamento", "b:Segmento"],
            "nr_frota": ["prefix:", "b:Equipamento", "b:Numero"],
            "dt_aquisicao": ["prefix:", "b:Equipamento", "b:DataAquisicao"],
            "nr_km": ["prefix:", "b:Kilometragem"],
            "nr_horimetro": ["prefix:", "b:Horimetro"],
            "nr_litros": ["prefix:", "b:Litros"],
            "nr_quantidade": ["prefix:", "b:Litros"],
            "nr_valorunitario": ["prefix:", "b:ValorUnitario"],
            "nr_preco": ["prefix:", "b:ValorUnitario"],
            "nr_valortotal": ["prefix:", "b:ValorTotal"],
            "cd_viagem": ["prefix:", "b:NumeroAcerto"],
            "cd_motorista": ["prefix:", "b:Motorista", "c:Codigo"],
            "ds_nomemotorista": ["prefix:", "b:Motorista", "c:Nome"],
            "ds_cpf": ["prefix:", "b:Motorista", "c:CPF"],
            "ds_rg": ["prefix:", "b:Motorista", "c:RG"],
            "dt_nascimento": ["prefix:", "b:Motorista", "c:DataNascimento"],
            "ds_estadocivil": ["prefix:", "b:Motorista", "c:EstadoCivil"],
            "ds_enderecomotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Logradouro"],
            "ds_cidademotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_ufmotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_paismotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "fl_ativo": None
        },
        "flow_carga": {
                "cd_carga": ["prefix:", "b:protocoloIntegracaoCarga"],
                "cd_pedido": ["prefix:", "b:protocoloIntegracaoPedido"]
        },
        "flow_viagem": {
            "cd_viagem": ["prefix:", "b:NumeroAcerto"],
            "dt_inicial": ["prefix:", "b:DataInicialAcerto"],
            "dt_final": ["prefix:", "b:DataFinalAcerto"],
            "nr_kminicial": None,
            "nr_kmfinal": None,
            "nr_hrinicial": None,
            "nr_hrfinal": None,
            "nr_kmrodado": None,
            "nr_horastrabalhadas": None,
            "cd_motorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Codigo"],
            "ds_nomemotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Nome"],
            "ds_cpf": ["prefix:", "b:Motoristas", "c:Motorista", "c:CPF"],
            "ds_rg": ["prefix:", "b:Motoristas", "c:Motorista", "c:RG"],
            "dt_nascimento": ["prefix:", "b:Motoristas", "c:Motorista", "c:DataNascimento"],
            "ds_estadocivil": ["prefix:", "b:Motoristas", "c:Motorista", "c:EstadoCivil"],
            "ds_enderecomotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Logradouro"],
            "ds_cidademotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_ufmotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_paismotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "cd_veiculo": ["prefix:", "b:Veiculo", "c:Codigo"],
            "ds_placa": ["prefix:", "b:Veiculo", "c:Placa"],
            "ds_nrfrota": ["prefix:", "b:Veiculo", "c:NumeroFrota"],
            "ds_chassi": ["prefix:", "b:Veiculo", "c:NumeroChassi"],
            "ds_renavam": ["prefix:", "b:Veiculo", "c:Renavam"],
            "nr_anofabricacao": ["prefix:", "b:Veiculo", "c:AnoFabricacao"],
            "nr_anomodelo": ["prefix:", "b:Veiculo", "c:AnoModelo"],
            "ds_marca": ["prefix:", "b:Veiculo", "c:Modelo", "c:Marca", "c:Descricao"],
            "ds_modelo": ["prefix:", "b:Veiculo", "c:Modelo", "c:Descricao"],
            "ds_tipoveiculo": ["prefix:", "b:Veiculo", "c:TipoVeiculo"],
            "ds_frota": ["prefix:", "b:Veiculo", "c:SegmentoVeiculo", "c:Descricao"],
            "nr_frota": ["prefix:", "b:Veiculo", "c:NumeroFrota"],
            "dt_aquisicao": ["prefix:", "b:Veiculo", "c:DataAquisicao"],
            "cd_veiculoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Codigo"],
            "ds_placareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Placa"],
            "ds_nrfrotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroFrota"],
            "ds_chassireboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroChassi"],
            "ds_renavamreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Renavam"],
            "nr_anofabricacaoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:AnoFabricacao"],
            "nr_anomodeloreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:AnoModelo"],
            "ds_marcareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Modelo", "c:Marca", "c:Descricao"],
            "ds_modeloreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Modelo", "c:Descricao"],
            "ds_tipoveiculoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:TipoVeiculo"],
            "ds_frotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:SegmentoVeiculo", "c:Descricao"],
            "nr_frotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroFrota"],
            "dt_aquisicaoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:DataAquisicao"],
        },
        "flow_pedido_frete": {
            "cd_carga": ["prefix:", "b:ProtocoloCarga"],
            "cd_pedido": ["prefix:", "b:ProtocoloPedido"],
            "dt_emissao": ["prefix:", "b:DataCriacaoCarga"],
            "ds_cidadeorigem": ["prefix:", "b:Origem", "c:Cidade", "d:Descricao"],
            "ds_cidadedestino": ["prefix:", "b:Destino", "c:Cidade", "d:Descricao"],
            "ds_siglauforigem": ["prefix:", "b:Origem", "c:Cidade", "d:SiglaUF"],
            "ds_siglaufdestino": ["prefix:", "b:Destino", "c:Cidade", "d:SiglaUF"],
            "ds_uforigem": None,
            "ds_ufdestino": None,
            "cd_veiculo": ["prefix:", "b:Veiculo", "c:Codigo"],
            "ds_placa": ["prefix:", "b:Veiculo", "c:Placa"],
            "ds_nrfrota": ["prefix:", "b:Veiculo", "c:NumeroFrota"],
            "ds_chassi": ["prefix:", "b:Veiculo", "c:NumeroChassi"],
            "ds_renavam": ["prefix:", "b:Veiculo", "c:Renavam"],
            "nr_anofabricacao": ["prefix:", "b:Veiculo", "c:AnoFabricacao"],
            "nr_anomodelo": ["prefix:", "b:Veiculo", "c:AnoModelo"],
            "ds_marca": ["prefix:", "b:Veiculo", "c:Modelo", "c:Marca", "c:Descricao"],
            "ds_modelo": ["prefix:", "b:Veiculo", "c:Modelo", "c:Descricao"],
            "ds_tipoveiculo": ["prefix:", "b:Veiculo", "c:TipoVeiculo"],
            "ds_frota": ["prefix:", "b:Veiculo", "c:SegmentoVeiculo", "c:Descricao"],
            "nr_frota": ["prefix:", "b:Veiculo", "c:NumeroFrota"],
            "dt_aquisicao": ["prefix:", "b:Veiculo", "c:DataAquisicao"],
            "cd_relacionado": ["prefix:CF", "b:Tomador", "c:CodigoIntegracao"],
            "ds_cnpjcpf": ["prefix:", "b:Tomador", "c:CPFCNPJ"],
            "ds_ierg": ["prefix:", "b:Tomador", "c:RGIE"],
            "ds_nomerazaosocial": ["prefix:", "b:Tomador", "c:RazaoSocial"],
            "ds_nomefantasia": ["prefix:", "b:Tomador", "c:NomeFantasia"],
            "ds_email": ["prefix:", "b:Tomador", "c:Email"],
            "ds_telefone1": ["prefix:", "b:Tomador", "c:Endereco", "d:Telefone"],
            "ds_telefone2": ["prefix:", "b:Tomador", "c:Endereco", "d:Telefone2"],
            "ds_endereco": ["prefix:", "b:Tomador", "c:Endereco", "d:Logradouro"],
            "ds_cep": ["prefix:", "b:Tomador", "c:Endereco", "d:CEP"],
            "ds_latitude": ["prefix:", "b:Tomador", "c:Endereco", "d:Latitude"],
            "ds_longitude": ["prefix:", "b:Tomador", "c:Endereco", "d:Longitude"],
            "dt_nascfundacao": None,
            "ds_cidade": ["prefix:", "b:Tomador", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_uf": ["prefix:", "b:Tomador", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_pais": ["prefix:", "b:Tomador", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "ds_grupo": ["prefix:", "b:Tomador", "c:NomeFantasia"],
            "nr_km": ["prefix:", "b:Distancia"],
            "nr_peso": ["prefix:", "b:PesoLiquido"],
            "cd_viagem": ["prefix:", "b:NumeroAcerto"],
            "dt_inicial": ["prefix:", "b:DataInicialAcerto"],
            "dt_final": ["prefix:", "b:DataFinalAcerto"],
            "nr_kminicial": None,
            "nr_kmfinal": None,
            "nr_hrinicial": None,
            "nr_hrfinal": None,
            "nr_kmrodado": None,
            "nr_horastrabalhadas": None,
            "cd_motorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Codigo"],
            "ds_nomemotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Nome"],
            "ds_cpf": ["prefix:", "b:Motoristas", "c:Motorista", "c:CPF"],
            "ds_rg": ["prefix:", "b:Motoristas", "c:Motorista", "c:RG"],
            "dt_nascimento": ["prefix:", "b:Motoristas", "c:Motorista", "c:DataNascimento"],
            "ds_estadocivil": ["prefix:", "b:Motoristas", "c:Motorista", "c:EstadoCivil"],
            "ds_enderecomotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Logradouro"],
            "ds_cidademotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_ufmotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_paismotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "cd_veiculoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Codigo"],
            "ds_placareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Placa"],
            "ds_nrfrotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroFrota"],
            "ds_chassireboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroChassi"],
            "ds_renavamreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Renavam"],
            "nr_anofabricacaoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:AnoFabricacao"],
            "nr_anomodeloreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:AnoModelo"],
            "ds_marcareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Modelo", "c:Marca", "c:Descricao"],
            "ds_modeloreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Modelo", "c:Descricao"],
            "ds_tipoveiculoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:TipoVeiculo"],
            "ds_frotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:SegmentoVeiculo", "c:Descricao"],
            "nr_frotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroFrota"],
            "dt_aquisicaoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:DataAquisicao"],
        },
        "flow_faturamento": {
            "ds_situacao": ["prefix:", "b:SituacaoCTeSefaz"],
            "dt_emissao": ["prefix:", "b:DataEmissao"],
            "nr_valorfrete": ["prefix:", "b:ValorFrete", "c:ValorPrestacaoServico"],
            "nr_valorpedagio": None,
            "nr_valortotal": ["prefix:", "b:ValorFrete", "c:ValorTotalAReceber"],
            "nr_aliqicms": ["prefix:", "b:ValorFrete", "c:ICMS", "d:Aliquota"],
            "nr_km": None,
            "cd_relacionado": ["prefix:CF", "b:Tomador", "c:CodigoIntegracao"],
            "ds_cnpjcpf": ["prefix:", "b:Tomador", "c:CPFCNPJ"],
            "ds_ierg": ["prefix:", "b:Tomador", "c:RGIE"],
            "ds_nomerazaosocial": ["prefix:", "b:Tomador", "c:RazaoSocial"],
            "ds_nomefantasia": ["prefix:", "b:Tomador", "c:NomeFantasia"],
            "ds_grupo": ["prefix:", "b:Tomador", "c:NomeFantasia"],
            "ds_email": ["prefix:", "b:Tomador", "c:Email"],
            "ds_telefone1": ["prefix:", "b:Tomador", "c:Endereco", "d:Telefone"],
            "ds_telefone2": ["prefix:", "b:Tomador", "c:Endereco", "d:Telefone2"],
            "ds_endereco": ["prefix:", "b:Tomador", "c:Endereco", "d:Logradouro"],
            "ds_cep": ["prefix:", "b:Tomador", "c:Endereco", "d:CEP"],
            "ds_latitude": ["prefix:", "b:Tomador", "c:Endereco", "d:Latitude"],
            "ds_longitude": ["prefix:", "b:Tomador", "c:Endereco", "d:Longitude"],
            "dt_nascfundacao": None,
            "ds_cidade": ["prefix:", "b:Tomador", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_uf": ["prefix:", "b:Tomador", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_pais": ["prefix:", "b:Tomador", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "cd_motorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Codigo"],
            "ds_nomemotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Nome"],
            "ds_cpf": ["prefix:", "b:Motoristas", "c:Motorista", "c:CPF"],
            "ds_rg": ["prefix:", "b:Motoristas", "c:Motorista", "c:RG"],
            "dt_nascimento": ["prefix:", "b:Motoristas", "c:Motorista", "c:DataNascimento"],
            "ds_estadocivil": ["prefix:", "b:Motoristas", "c:Motorista", "c:EstadoCivil"],
            "ds_enderecomotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Logradouro"],
            "ds_cidademotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_ufmotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_paismotorista": ["prefix:", "b:Motoristas", "c:Motorista", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "cd_veiculo": ["prefix:", "b:Veiculo", "c:Codigo"],
            "ds_placa": ["prefix:", "b:Veiculo", "c:Placa"],
            "ds_nrfrota": ["prefix:", "b:Veiculo", "c:NumeroFrota"],
            "ds_chassi": ["prefix:", "b:Veiculo", "c:NumeroChassi"],
            "ds_renavam": ["prefix:", "b:Veiculo", "c:Renavam"],
            "nr_anofabricacao": ["prefix:", "b:Veiculo", "c:AnoFabricacao"],
            "nr_anomodelo": ["prefix:", "b:Veiculo", "c:AnoModelo"],
            "ds_marca": ["prefix:", "b:Veiculo", "c:Modelo", "c:Marca", "c:Descricao"],
            "ds_modelo": ["prefix:", "b:Veiculo", "c:Modelo", "c:Descricao"],
            "ds_tipoveiculo": ["prefix:", "b:Veiculo", "c:TipoVeiculo"],
            "ds_frota": ["prefix:", "b:Veiculo", "c:SegmentoVeiculo", "c:Descricao"],
            "nr_frota": ["prefix:", "b:Veiculo", "c:NumeroFrota"],
            "dt_aquisicao": ["prefix:", "b:Veiculo", "c:DataAquisicao"],
            "cd_veiculoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Codigo"],
            "ds_placareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Placa"],
            "ds_nrfrotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroFrota"],
            "ds_chassireboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroChassi"],
            "ds_renavamreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Renavam"],
            "nr_anofabricacaoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:AnoFabricacao"],
            "nr_anomodeloreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:AnoModelo"],
            "ds_marcareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Modelo", "c:Marca", "c:Descricao"],
            "ds_modeloreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:Modelo", "c:Descricao"],
            "ds_tipoveiculoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:TipoVeiculo"],
            "ds_frotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:SegmentoVeiculo", "c:Descricao"],
            "nr_frotareboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:NumeroFrota"],
            "dt_aquisicaoreboque": ["prefix:", "b:Veiculo", "c:Reboques", "c:Veiculo", "c:DataAquisicao"],
        },
        "flow_manutencao": {
            "dt_emissao": ["prefix:", "b:DataFechamento"],
            "cd_manutencao": ["prefix:", "b:Codigo"],
            "nr_documento": ["prefix:", "b:Numero"],
            "ds_historico": ["prefix:", "b:Observacao"],
            "nr_kilometragem": ["prefix:", "b:KMAtual"],
            "nr_horimetro": ["prefix:", "b:Horimetro"],
            "nr_valortotal": ["prefix:", "b:ValorRealiazdo"],
            "cd_produto": None,
            "ds_produto": None,
            "ds_ncm": None,
            "ds_undmedida": None,
            "ds_tipomanutencao": ["prefix:", "b:TipoManutencao"],
            "cd_relacionado": ["prefix:FM", "b:LocalManutencao", "c:CodigoIntegracao"],
            "ds_cnpjcpf": ["prefix:", "b:LocalManutencao", "c:CPFCNPJ"],
            "ds_ierg": ["prefix:", "b:LocalManutencao", "c:RGIE"],
            "ds_nomerazaosocial": ["prefix:", "b:LocalManutencao", "c:RazaoSocial"],
            "ds_nomefantasia": ["prefix:", "b:LocalManutencao", "c:NomeFantasia"],
            "ds_grupo": ["prefix:", "b:LocalManutencao", "c:NomeFantasia"],
            "ds_email": ["prefix:", "b:LocalManutencao", "c:Email"],
            "ds_telefone1": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Telefone"],
            "ds_telefone2": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Telefone2"],
            "ds_endereco": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Logradouro"],
            "ds_cep": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:CEP"],
            "ds_latitude": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Latitude"],
            "ds_longitude": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Longitude"],
            "dt_nascfundacao": None,
            "ds_cidade": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_uf": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_pais": ["prefix:", "b:LocalManutencao", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "cd_motorista": ["prefix:", "b:Motorista", "c:Codigo"],
            "ds_nomemotorista": ["prefix:", "b:Motorista", "c:Nome"],
            "ds_cpf": ["prefix:", "b:Motorista", "c:CPF"],
            "ds_rg": ["prefix:", "b:Motorista", "c:RG"],
            "dt_nascimento": ["prefix:", "b:Motorista", "c:DataNascimento"],
            "ds_estadocivil": ["prefix:", "b:Motorista", "c:EstadoCivil"],
            "ds_enderecomotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Logradouro"],
            "ds_cidademotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_ufmotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_paismotorista": ["prefix:", "b:Motorista", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "cd_veiculo": ["prefix:", "b:Veiculo", "b:Codigo"],
            "ds_placa": ["prefix:", "b:Veiculo", "b:Placa"],
            "ds_nrfrota": ["prefix:", "b:Veiculo", "b:NumeroFrota"],
            "ds_chassi": ["prefix:", "b:Veiculo", "b:NumeroChassi"],
            "ds_renavam": ["prefix:", "b:Veiculo", "b:Renavam"],
            "nr_anofabricacao": ["prefix:", "b:Veiculo", "b:AnoFabricacao"],
            "nr_anomodelo": ["prefix:", "b:Veiculo", "b:AnoModelo"],
            "ds_marca": ["prefix:", "b:Veiculo", "b:Modelo", "b:Marca", "b:Descricao"],
            "ds_modelo": ["prefix:", "b:Veiculo", "b:Modelo", "b:Descricao"],
            "ds_tipoveiculo": ["prefix:", "b:Veiculo", "b:TipoVeiculo"],
            "ds_frota": ["prefix:", "b:Veiculo", "b:SegmentoVeiculo", "b:Descricao"],
            "nr_frota": ["prefix:", "b:Veiculo", "b:NumeroFrota"],
            "dt_aquisicao": ["prefix:", "b:Veiculo", "b:DataAquisicao"],
        },
        "flow_tabelapreco": {
            "cd_tabela": ["prefix:", "b:Codigo"],
            "dt_inicial": ["prefix:", "b:DataInicial"],
            "dt_final": ["prefix:", "b:DataFinal"],
            "nr_valor": ["prefix:", "b:ValorAte"],
            "cd_relacionado": ["prefix:FC", "b:Posto", "c:CodigoIntegracao"],
            "ds_cnpjcpf": ["prefix:", "b:Posto", "c:CPFCNPJ"],
            "ds_ierg": ["prefix:", "b:Posto", "c:RGIE"],
            "ds_nomerazaosocial": ["prefix:", "b:Posto", "c:RazaoSocial"],
            "ds_nomefantasia": ["prefix:", "b:Posto", "c:NomeFantasia"],
            "ds_grupo": ["prefix:", "b:Posto", "c:NomeFantasia"],
            "ds_email": ["prefix:", "b:Posto", "c:Email"],
            "ds_telefone1": ["prefix:", "b:Posto", "c:Endereco", "d:Telefone"],
            "ds_telefone2": ["prefix:", "b:Posto", "c:Endereco", "d:Telefone2"],
            "ds_endereco": ["prefix:", "b:Posto", "c:Endereco", "d:Logradouro"],
            "ds_cep": ["prefix:", "b:Posto", "c:Endereco", "d:CEP"],
            "ds_latitude": ["prefix:", "b:Posto", "c:Endereco", "d:Latitude"],
            "ds_longitude": ["prefix:", "b:Posto", "c:Endereco", "d:Longitude"],
            "dt_nascfundacao": None,
            "ds_cidade": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:Descricao"],
            "ds_uf": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:SiglaUF"],
            "ds_pais": ["prefix:", "b:Posto", "c:Endereco", "d:Cidade", "e:Pais", "d:NomePais"],
            "cd_produto": ["prefix:", "b:Produto", "c:Codigo"],
            "ds_produto": ["prefix:", "b:Produto", "c:Descricao"],
            "ds_ncm": ["prefix:", "b:Produto", "c:NCM"],
        }

    }