
class DatabaseConn:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(DatabaseConn, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.connection = self.connect()

    def connect(self):
        print('Database connected')
        return 'Conexion establecida'

    def get_connection(self):
        return self.connection
    
