import configparser

class DBPropertyUtil:
    @staticmethod
    def getPropertyString(filename):
        config = configparser.ConfigParser()
        config.read(filename)
        section = config['DB']
        host = section['host']
        dbname = section['dbname']

        # Print the connection details for debugging
        print(f"Trying to connect to: {host}, Database: {dbname}")

        # Construct the connection string (assuming default instance)
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host};DATABASE={dbname};Trusted_Connection=yes"
        
        return conn_str

