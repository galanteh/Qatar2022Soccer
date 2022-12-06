import errno
import logging
import os
import sys
from configparser import ConfigParser
from logging import handlers
from dbmanager import DbManager


class WorldCupConfigurationMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class WorldCupConfiguration(metaclass=WorldCupConfigurationMeta):

    def __init__(self):
        self.logger = None
        self.verbose = False
        self.dstorePath = ''
        self.dstoreName = ''
        self.datastore_db_manager = None
        # If in the FIFA Ranking there is major difference of points between team, will win the best ranked.
        self.automatic_points_required_to_win = 100
        self._readConfigurationFrom('qwc.cfg')
        self.logger.info('Starting the Qatar World Cup App')

    def _get_datastore_db_path(self):
        return os.path.join(self.dstorePath, self.dstoreName)

    def _open_datastore_db(self):
        self._ensure_has_paths(self.dstorePath, is_filename=False)
        self.datastore_db_manager = DbManager(self.logger, self._get_datastore_db_path())

    def get_dbmanager(self):
        if self.datastore_db_manager is not None:
            return self.datastore_db_manager
        else:
            self._open_datastore_db()
        return self.datastore_db_manager

    def save(self, world_cup):
        self.get_dbmanager().save(world_cup)

    def _ensure_has_paths(self, new_path, is_filename=True):
        """
        Private method - Ensure that the path in the config file exits or create them.
        :return:
        """
        if is_filename:
            if not os.path.exists(os.path.dirname(new_path)):
                try:
                    if self.logger is not None:
                        self.logger.info("Creating path {0}".format(new_path))
                    os.makedirs(os.path.dirname(new_path))
                except OSError as exception:  # Guard against race condition
                    if exception.errno != errno.EEXIST:
                        raise exception
        else:
            if not os.path.isdir(new_path):
                if self.logger is not None:
                    self.logger.info("Creating path {0}".format(new_path))
                os.makedirs(new_path)

    def init_config_logger(self, logfile, maxBytes=5242880):
        """
        Setup the logger of the receiver.
        :param logfile: filename of the log
        :param maxBytes: max number of bytes per log file
        :return:
        """
        self._ensure_has_paths(logfile, is_filename=True)
        self.logger = logging.getLogger('QWC')
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.logger.setLevel(logging.INFO)
        # Console
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        # File
        fh = handlers.RotatingFileHandler(logfile, maxBytes=maxBytes, backupCount=7)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def _create_default_cfg_file(self, cfg_file):
        config = ConfigParser()
        config.add_section('Logs')
        config['Logs']['Filename'] = "./logs/application.log"
        config['Logs']['Verbose'] = "True"
        config['Logs']['MaxBytes'] = "5242880"
        config.add_section('Datastore')
        config['Datastore']['Path'] = "./datastore"
        config['Datastore']['Dbname'] = "datastore.db"
        config.add_section('Points')
        config['Points']['AutomaticPointsRequiredToWin'] = "100"
        with open(cfg_file, 'w') as f:
            config.write(f)

    def _readConfigurationFrom(self, cfg_file):
        """
        Read the configuration from the argument file
        :param cfgfile: filename
        :return: None
        """
        try:
            config = ConfigParser()
            confirmation = config.read(cfg_file)
            if len(confirmation) == 0:
                self._create_default_cfg_file(cfg_file)
            _logfile = config.has_option('Logs', 'Filename') and config.get('Logs',
                                                                            'Filename') or './logs/application.log'
            _logfile_max_bytes = int(
                config.has_option('Logs', 'MaxBytes') and config.get('Logs', 'MaxBytes') or 5242880)
            self.verbose = bool(config.has_option('Logs', 'Verbose') and config.get('Logs', 'Verbose') or False)
            self.init_config_logger(_logfile, _logfile_max_bytes)
            self.dstorePath = config.has_option('Datastore', 'Path') and config.get('Datastore',
                                                                                    'Path') or './datastore'
            self.dstoreName = config.has_option('Datastore', 'Dbname') and config.get('Datastore',
                                                                                      'Dbname') or 'datastore.db'
            self._open_datastore_db()
            self.automatic_points_required_to_win = int(
                config.has_option('Points', 'AutomaticPointsRequiredToWin') and config.get('Points',
                                                                                           'AutomaticPointsRequiredToWin') or 100)
        except Exception as e:
            self.logger.error("[QWC][ReadConfiguration] Exception {0}".format(e))
            sys.exit("[QWC][ReadConfiguration] Exception {0}".format(e))

