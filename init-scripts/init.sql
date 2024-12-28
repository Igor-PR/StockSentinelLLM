CREATE DATABASE analytics;
\connect analytics;
CREATE SCHEMA raw_layer;
CREATE TABLE raw_layer.stock_segments (
	segmentid int4 NULL,
	segmentname varchar NULL,
	segmentname_eng varchar NULL
);

CREATE TABLE raw_layer.stock_sectors (
	sectorid int4 NULL,
	sectorname varchar NULL,
	sectorname_eng varchar NULL
);

CREATE TABLE raw_layer.stock_subsectors (
	subsectorid int4 NULL,
	subsectorname varchar NULL,
	subsectorname_eng varchar NULL
);

INSERT INTO raw_layer.stock_subsectors (subsectorid, subsectorname, subsectorname_eng)
VALUES
    (1, 'Comércio', 'Commerce'),
    (2, 'Construção e Engenharia', 'Construction and Engineering'),
    (3, 'Máquinas e Equipamentos', 'Machinery and Equipment'),
    (4, 'Material de Transporte', 'Transportation Material'),
    (5, 'Serviços', 'Services'),
    (6, 'Transporte', 'Transportation'),
    (7, 'Automóveis e Motocicletas', 'Automobiles and Motorcycles'),
    (8, 'Comércio', 'Commerce'),
    (9, 'Construção Civil', 'Civil Construction'),
    (10, 'Diversos', 'Miscellaneous'),
    (11, 'Hoteis e Restaurantes', 'Hotels and Restaurants'),
    (12, 'Mídia', 'Media'),
    (13, 'Tecidos. Vestuário e Calçados', 'Fabrics, Clothing, and Footwear'),
    (14, 'Utilidades Domésticas', 'Household Utilities'),
    (15, 'Viagens e Lazer', 'Travel and Leisure'),
    (16, 'Agropecuária', 'Agriculture and Livestock'),
    (17, 'Alimentos Processados', 'Processed Foods'),
    (18, 'Bebidas', 'Beverages'),
    (19, 'Comércio e Distribuição', 'Commerce and Distribution'),
    (20, 'Diversos', 'Miscellaneous'),
    (21, 'Produtos de Uso Pessoal e de Limpeza', 'Personal Use and Cleaning Products'),
    (22, 'Exploração de Imóveis', 'Real Estate Exploration'),
    (23, 'Holdings Diversificadas', 'Diversified Holdings'),
    (24, 'Intermediários Financeiros', 'Financial Intermediaries'),
    (25, 'Outros', 'Others'),
    (26, 'Previdência e Seguros', 'Pension and Insurance'),
    (28, 'Serviços Financeiros Diversos', 'Miscellaneous Financial Services'),
    (29, 'Embalagens', 'Packaging'),
    (30, 'Madeira e Papel', 'Wood and Paper'),
    (31, 'Materiais Diversos', 'Miscellaneous Materials'),
    (32, 'Mineração', 'Mining'),
    (33, 'Químicos', 'Chemicals'),
    (34, 'Siderurgia e Metalurgia', 'Steelmaking and Metallurgy'),
    (35, 'Petróleo. Gás e Biocombustíveis', 'Oil, Gas, and Biofuels'),
    (36, 'Comércio e Distribuição', 'Commerce and Distribution'),
    (37, 'Equipamentos', 'Equipment'),
    (38, 'Medicamentos e Outros Produtos', 'Medicines and Other Products'),
    (39, 'Serv.Méd.Hospit..Análises e Diagnósticos', 'Medical, Hospital Services, Analysis, and Diagnostics'),
    (40, 'Computadores e Equipamentos', 'Computers and Equipment'),
    (41, 'Programas e Serviços', 'Programs and Services'),
    (42, 'Telecomunicações', 'Telecommunications'),
    (43, 'Água e Saneamento', 'Water and Sanitation'),
    (44, 'Energia Elétrica', 'Electric Power'),
    (45, 'Gás', 'Gas'),
    (58, 'Mídia', 'Media'),
    (59, 'Biotecnologia', 'Biotechnology');

INSERT INTO raw_layer.stock_sectors (sectorid, sectorname, sectorname_eng)
VALUES
    (1, 'Bens Industriais', 'Industrial Goods'),
    (2, 'Consumo Cíclico', 'Cyclical Consumption'),
    (3, 'Consumo não Cíclico', 'Non-Cyclical Consumption'),
    (4, 'Financeiro e Outros', 'Financials and Others'),
    (5, 'Materiais Básicos', 'Basic Materials'),
    (6, 'Petróleo. Gás e Biocombustíveis', 'Oil, Gas, and Biofuels'),
    (7, 'Saúde', 'Health'),
    (8, 'Tecnologia da Informação', 'Information Technology'),
    (9, 'Comunicações', 'Communications'),
    (10, 'Utilidade Pública', 'Public Utilities');

INSERT INTO raw_layer.stock_subsectors (subsectorid, subsectorname, subsectorname_eng)
VALUES
    (1, 'Comércio', 'Commerce'),
    (2, 'Construção e Engenharia', 'Construction and Engineering'),
    (3, 'Máquinas e Equipamentos', 'Machinery and Equipment'),
    (4, 'Material de Transporte', 'Transportation Material'),
    (5, 'Serviços', 'Services'),
    (6, 'Transporte', 'Transportation'),
    (7, 'Automóveis e Motocicletas', 'Automobiles and Motorcycles'),
    (8, 'Comércio', 'Commerce'),
    (9, 'Construção Civil', 'Civil Construction'),
    (10, 'Diversos', 'Miscellaneous'),
    (11, 'Hoteis e Restaurantes', 'Hotels and Restaurants'),
    (12, 'Mídia', 'Media'),
    (13, 'Tecidos. Vestuário e Calçados', 'Fabrics, Clothing, and Footwear'),
    (14, 'Utilidades Domésticas', 'Household Utilities'),
    (15, 'Viagens e Lazer', 'Travel and Leisure'),
    (16, 'Agropecuária', 'Agriculture and Livestock'),
    (17, 'Alimentos Processados', 'Processed Foods'),
    (18, 'Bebidas', 'Beverages'),
    (19, 'Comércio e Distribuição', 'Commerce and Distribution'),
    (20, 'Diversos', 'Miscellaneous'),
    (21, 'Produtos de Uso Pessoal e de Limpeza', 'Personal Use and Cleaning Products'),
    (22, 'Exploração de Imóveis', 'Real Estate Exploration'),
    (23, 'Holdings Diversificadas', 'Diversified Holdings'),
    (24, 'Intermediários Financeiros', 'Financial Intermediaries'),
    (25, 'Outros', 'Others'),
    (26, 'Previdência e Seguros', 'Pension and Insurance'),
    (28, 'Serviços Financeiros Diversos', 'Miscellaneous Financial Services'),
    (29, 'Embalagens', 'Packaging'),
    (30, 'Madeira e Papel', 'Wood and Paper'),
    (31, 'Materiais Diversos', 'Miscellaneous Materials'),
    (32, 'Mineração', 'Mining'),
    (33, 'Químicos', 'Chemicals'),
    (34, 'Siderurgia e Metalurgia', 'Steelmaking and Metallurgy'),
    (35, 'Petróleo. Gás e Biocombustíveis', 'Oil, Gas, and Biofuels'),
    (36, 'Comércio e Distribuição', 'Commerce and Distribution'),
    (37, 'Equipamentos', 'Equipment'),
    (38, 'Medicamentos e Outros Produtos', 'Medicines and Other Products'),
    (39, 'Serv.Méd.Hospit..Análises e Diagnósticos', 'Medical, Hospital Services, Analysis, and Diagnostics'),
    (40, 'Computadores e Equipamentos', 'Computers and Equipment'),
    (41, 'Programas e Serviços', 'Programs and Services'),
    (42, 'Telecomunicações', 'Telecommunications'),
    (43, 'Água e Saneamento', 'Water and Sanitation'),
    (44, 'Energia Elétrica', 'Electric Power'),
    (45, 'Gás', 'Gas'),
    (58, 'Mídia', 'Media'),
    (59, 'Biotecnologia', 'Biotechnology');
