DROP TABLE IF EXISTS obra;
DROP TABLE IF EXISTS referencia;
DROP TABLE IF EXISTS registro;
DROP TABLE IF EXISTS sensor;
DROP TABLE IF EXISTS sistema;
DROP TABLE IF EXISTS umbrales;
DROP TABLE IF EXISTS parametros;

CREATE TABLE sistema (
    id_sistema INTEGER PRIMARY KEY,
    nom_tipo_sensor TEXT NOT NULL UNIQUE
);

CREATE TABLE obra (
    id_obra INTEGER PRIMARY KEY,
    nom_obra TEXT NOT NULL,
    tramo TEXT NOT NULL
);

CREATE TABLE sensor (
    id_sensor INTEGER PRIMARY KEY,
    nom_sensor TEXT NOT NULL UNIQUE,
    id_externo TEXT NOT NULL UNIQUE,
    x REAL,
    y REAL,
    z REAL,
    obra_sensor REFERENCES obra (id_obra),
    sistema_sensor REFERENCES sistema (id_sistema), 
    id_sensor_gis TEXT,
    numero_serie TEXT
);

CREATE TABLE referencia (
    fecha_referencia TEXT,
    lectura_referencia REAL,
    medida_referencia REAL,
    id_sensor_referencia REFERENCES sensor (id_sensor),
    PRIMARY KEY (fecha_referencia, lectura_referencia, medida_referencia, id_sensor_referencia)
);

CREATE TABLE umbrales (
    id_tipo_alerta INTEGER,
    id_nivel_alerta INTEGER,
    valor_umbral REAL,
    id_sensor_umbral REFERENCES sensor (id_sensor),
    PRIMARY KEY (id_tipo_alerta, id_nivel_alerta, valor_umbral, id_sensor_umbral)
);

CREATE TABLE registro (
    fecha_registro TEXT,
    id_sensor_registro REFERENCES sensor (id_sensor),
    lectura_registro REAL NOT NULL,
    medida_registro REAL NOT NULL,
    PRIMARY KEY (fecha_registro, id_sensor_registro)
);

CREATE TABLE parametros (
    par_a REAL,
    par_b REAL,
    par_c REAL,
    par_d REAL,
    par_g REAL,
    par_k REAL,
    id_sensor_parametros REFERENCES sensor (id_sensor)
);