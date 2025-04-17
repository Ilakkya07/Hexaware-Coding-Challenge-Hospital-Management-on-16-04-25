import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyodbc
from util.PropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def getConnection():
        conn_str = DBPropertyUtil.getPropertyString('resources/db.properties')
        print(f"Connection String: {conn_str}")
        try:
            conn = pyodbc.connect(conn_str)
            return conn
        except pyodbc.Error as e:
            print(f"Connection failed: {e}")
            return None