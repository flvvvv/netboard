DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '192.168.1.1'
PORT = '3306'
DATABASE = 'test'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "123456"

'''
 
'''