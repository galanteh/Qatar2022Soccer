import sqlite3
from datetime import datetime


class DbManagerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DbManager(metaclass=DbManagerMeta):

    def __init__(self, logger, datastore_db_path):
        self.logger = logger
        self._init_connection(datastore_db_path)
        self._setup_tables()

    def __del__(self):
        if self._db_conn is not None:
            self._db_conn.close()

    def _init_connection(self, datastore_db_path):
        try:
            self._db_conn = sqlite3.connect(datastore_db_path)
        except Exception as e:
            self.logger.error(e)

    def get_connection(self):
        return self._db_conn

    def _setup_tables(self):
        try:
            self.get_connection().execute("CREATE TABLE IF NOT EXISTS simulation(id INTEGER PRIMARY KEY AUTOINCREMENT, time NUMERIC, first_place TEXT, second_place TEXT, third_place TEXT, fourth_place TEXT);")
            self.get_connection().commit()
        except Exception as e:
            self.logger.error(e)

    def save(self, world_cup):
        try:
            self.logger.info("Saving a Simulation")
            row = [datetime.now(), world_cup.get_first_place().country_name, world_cup.get_second_place().country_name,
                   world_cup.get_third_place().country_name, world_cup.get_fourth_place().country_name]
            self.get_connection().execute("INSERT INTO simulation (time, first_place, second_place, third_place, fourth_place) VALUES (?,?,?,?,?);", tuple(row))
            self.get_connection().commit()
        except Exception as e:
            self.logger.error(e)



