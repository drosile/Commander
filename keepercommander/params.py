#  _  __  
# | |/ /___ ___ _ __  ___ _ _ ®
# | ' </ -_) -_) '_ \/ -_) '_|
# |_|\_\___\___| .__/\___|_|
#              |_|            
#
# Keeper Commander 
# Contact: ops@keepersecurity.com
#


from urllib.parse import urlparse, urlunparse


class RestApiContext:
    def __init__(self, server='https://keepersecurity.com/api/v2/', locale='en_US', device_id=None):
        self.server_base = server
        self.transmission_key = None
        self.__server_key_id = 1
        self.locale = locale
        self.__device_id = device_id
        self.__store_server_key = False

    def __get_server_base(self):
        return self.__server_base

    def __set_server_base(self, value):
        p = urlparse(value)
        self.__server_base = urlunparse((p.scheme, p.netloc, '/api/rest/', None, None, None))

    def __get_server_key_id(self):
        return self.__server_key_id

    def __set_server_key_id(self, key_id):
        self.__server_key_id = key_id
        self.__store_server_key = True

    def __get_device_id(self):
        return self.__device_id

    def __set_device_id(self, device_id):
        self.__device_id = device_id
        self.__store_server_key = True

    def __get_store_server_key(self):
        return self.__store_server_key

    server_base = property(__get_server_base, __set_server_base)
    device_id = property(__get_device_id, __set_device_id)
    server_key_id = property(__get_server_key_id, __set_server_key_id)
    store_server_key = property(__get_store_server_key)


class KeeperParams:
    """ Global storage of data during the session """

    def __init__(self, config_filename='', config=None, server='https://keepersecurity.com/api/v2/', device_id=None):
        self.config_filename = config_filename
        self.config = config or {}
        self.auth_verifier = None
        self.__server = server
        self.user = ''
        self.password = ''
        self.mfa_token = ''
        self.mfa_type = 'device_token'
        self.commands = []
        self.plugins = []
        self.session_token = None
        self.salt = None
        self.iterations = 0
        self.data_key = None
        self.rsa_key = None
        self.revision = 0
        self.record_cache = {}
        self.meta_data_cache = {}
        self.shared_folder_cache = {}
        self.team_cache = {}
        self.subfolder_cache = {}
        self.subfolder_record_cache = {}
        self.root_folder = None
        self.current_folder = None
        self.folder_cache = {}
        self.debug = False
        self.timedelay = 0
        self.sync_data = True
        self.license = None
        self.settings = None
        self.enforcements = None
        self.enterprise = None
        self.prepare_commands = False
        self.batch_mode = False
        self.__rest_context = RestApiContext(server=server, device_id=device_id)
        self.pending_share_requests = set()

    def clear_session(self):
        self.auth_verifier = ''
        self.user = ''
        self.password = ''
        self.mfa_type = 'device_token'
        self.mfa_token = ''
        self.commands.clear()
        self.session_token = None
        self.salt = None
        self.iterations = 0
        self.data_key = None
        self.rsa_key = None
        self.revision = 0
        self.record_cache.clear()
        self.meta_data_cache.clear()
        self.shared_folder_cache.clear()
        self.team_cache.clear()
        self.subfolder_cache .clear()
        self.subfolder_record_cache.clear()
        if self.folder_cache:
            self.folder_cache.clear()

        self.root_folder = None
        self.current_folder = None
        self.sync_data = True
        self.license = None
        self.settings = None
        self.enforcements = None
        self.enterprise = None
        self.prepare_commands = True
        self.batch_mode = False
        self.pending_share_requests.clear()

    def __get_rest_context(self):
        return self.__rest_context

    def __get_server(self):
        return self.__server

    def __set_server(self, value):
        self.__server = value
        self.__rest_context.server_base = value

    server = property(__get_server, __set_server)
    rest_context = property(__get_rest_context)
