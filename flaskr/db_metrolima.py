import os
from sqlalchemy import create_engine
import pandas as pd
from flask import g

from queries import get_sensor_attrs_query


engine = create_engine(os.getenv("DATABASE_LIMA_URL"))


def get_sensor_attrs(nom_sensor):
    query = get_sensor_attrs_query
    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params=(nom_sensor,))
        return df
