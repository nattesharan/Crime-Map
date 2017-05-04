import pymysql
import dbconfig
class DBHelper:
    def connect(self, database = 'crimemap'):
        return pymysql.connect(host = 'localhost',
                               user = dbconfig.db_user,
                               passwd = dbconfig.db_password,
                               db = database)