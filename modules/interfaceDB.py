#!/usr/python3.5
import json
import psycopg2
import psycopg2.extras
from abc import ABC, abstractmethod

class DBInterface (ABC):# {{{
    def __init__ (self, host, database, user, password, port):
        self.__user = user
        self.__host = host
        self.__port = port
        self.__database = database
        self.__password = password
        self.connection = self.connect()

    def __del__ (self):
        self.disconnect()

    def __repr__ (self):
        return "host: %s\nport: %s\ndatabase: %s\nuser: %s\npassowrd: %s" % (self.__host, self.__port, self.__database, self.__user, self.password)

# {{{ PROPERTYS-----------------------------------------------------------------

    @property
    def host (self):
        return self.__host

    @property
    def user (self):
        return self.__user

    @property
    def port (self):
        return self.__port

    @property
    def database (self):
        return self.__database

    @property
    def password (self):
        return self.__password
# }}}
# {{{ ABSTRACTMETHODS-----------------------------------------------------------
    @abstractmethod
    def connect (self):
        '''To implement the connection of a particular database'''
        pass

    @abstractmethod
    def disconnect (self):
        pass

    @abstractmethod
    def consult (self, query):
        pass

    @abstractmethod
    def standardize (self, rows):
        pass
# }}}
# }}}
class dbiPostgresql (DBInterface):# {{{
    def __init__ (self, host, database, user, password, port):
        DBInterface.__init__(self, host, database, user, password, port)

    def __repr__ (self):
        tmp = DBInterface.__repr__(self)
        return "----------\nPostgresql\n%s\n----------" % tmp

    def connect (self):
        return psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)

    def disconnect (self):
        if self.connection:
            self.connection.close()

    def consult (self, query):
        cursor = self.connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        return self.standardize(cursor.fetchall())

    def standardize (self, rows):
        final = {}
        if rows:
            final['keys'] = [i for i in rows[0]]
            final['values'] = rows
        return final
# }}}
class dbiMysql (DBInterface):# {{{
    def __init__ (self, ):
        DBInterface.__init__(self, '1', '2', '3', '4', '5')

    def __repr__ (self):
        tmp = DBInterface.__repr__(self)
        return "----------\nMysql\n%s\n----------" % tmp

    def connect (self):
        print('connectando...')
        return True

    def disconnect (self):
        print('disconnectando...')

    def consult (self, query):
        print('consultando... ', query)
        return self.standardize('resultados da consulta')

    def standardize (self, rows):
        print('padronizando %s' % rows)
        return {"keys":[], "values":[]}
# }}}

def load_config ():# {{{
    connection_setup = {}
    file_name = "conf.json"
    try:
        json_file = open(file_name, "r")
        connection_setup = json.load(json_file)

    except:
        json_file = open(file_name, "w")
        json.dump(model_config(), json_file)

    finally:
        json_file.close()

    return connection_setup
# }}}
def model_config ():# {{{
    return {"dbms":"", "host":"", "port":"", "database":"", "user":"", "password":""}
# }}}

def easyDBInterface(query):# {{{
    config = load_config()
    dbms_supported = ["postgresql", "mysql"]
    db_interface = None

    if not config:
        raise ValueError("\n\nfile confi.json not fold\n\n")

    if config["dbms"] == dbms_supported[0]: # postgresql
        db_interface = dbiPostgresql(
                host = config["host"],
                port = config["port"],
                database = config["database"],
                user = config["user"],
                password = config["password"]
        )

    elif config["dbms"] == dbms_supported[1]: # mysql
        db_interface = dbiMysql()

    # ...in future more options

    else:
        raise ValueError("\n\n%s is an unknown dbms. values supported in confi.json: %s\n\n" % (config['dbms'], str(dbms_supported)))

    #print(db_interface)
    return db_interface.consult(query)
# }}}

if __name__ == "__main__": easyDBInterface("select * from actor limit 2;")
