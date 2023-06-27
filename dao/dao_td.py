import os
import pymysql.cursors


class DaoTD:

    def __init__(self) -> None:
        self.host = os.environ.get('HOST_DB_TD')
        self.port = int(os.environ.get('PORT_DB_TD'))
        self.user = os.environ.get('USER_DB_TD')
        self.password = os.environ.get('PASSWORD_DB_TD')
        self.schema = os.environ.get('SCHEMA_DB_TD')
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.schema
        )

    def get_sensor_attrs(self, nom_sensor):
        query = f"SELECT S.ID_SENSOR, S.ID_EXTERNO, S.X, S.Y, S.Z, " \
                f"S.ID_PRESA, S.ID_SISTEMA, S.ID_SENSORGIS " \
                f"FROM SENSOR S JOIN PRESA P on S.ID_PRESA = P.ID_PRESA " \
                f"JOIN SISTEMA S2 on S.ID_SISTEMA = S2.ID_TIPO_SENSOR " \
                f"WHERE S.NOM_SENSOR = '{nom_sensor}';"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    def get_presa_attrs(self, id_presa):
        query = f"SELECT NOM_PRESA FROM PRESA WHERE ID_PRESA = '{id_presa}';"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    def get_sistema_attrs(self, id_sistema):
        query = f"SELECT NOM_TIPO_SENSOR FROM SISTEMA WHERE ID_TIPO_SENSOR = '{id_sistema}'"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    def get_referencias_from_id_sensor(self, id_sensor):
        query = f"SELECT FECHA_MEDIDA, LECTURA, MEDIDA " \
                f"FROM HISTORICO WHERE ID_SENSOR = '{id_sensor}' AND ESREFERENCIA = 1 " \
                f"ORDER BY FECHA_MEDIDA;"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    def get_medida_from_registro(self, id_sensor, fecha_registro):
        query = f"SELECT MEDIDA FROM HISTORICO WHERE ID_SENSOR = '{id_sensor}' AND FECHA_MEDIDA = '{fecha_registro}';"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    def get_eldest_fecha(self, id_sensor):
        query = f"SELECT MIN(FECHA_MEDIDA) FROM HISTORICO WHERE ID_SENSOR = '{id_sensor}' GROUP BY ID_SENSOR;"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    def get_l0(self, id_sensor, eldest_fecha):
        query = f"SELECT LECTURA FROM HISTORICO WHERE ID_SENSOR = '{id_sensor}' AND FECHA_MEDIDA = '{eldest_fecha}';"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()

    # TODO Revisar este método.
    def get_umbrales_from_id_sensor(self, id_sensor):
        query = f"SELECT N.ID_TIPO_ALERTA, N.ID_NIVEL_ALERTA, N.VALOR " \
                f"FROM NIVEL_TIPO_ALERTA_SENSOR N, SENSOR S " \
                f"WHERE S.ID_SENSOR = N.ID_SENSOR " \
                f"AND S.ID_SENSOR = '{id_sensor}' " \
                f"ORDER BY N.ID_NIVEL_ALERTA, N.ID_TIPO_ALERTA"
        with self.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query)
            return cursor.fetchone()


dao_td = DaoTD()
