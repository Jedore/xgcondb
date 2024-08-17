from ._pyxgdb import _connect
from ._pyxgdb import version

def Connect(*args, **kwargs):
    # def_charset=""
    if kwargs is None:
        raise TypeError('Connection parameters are incorrect!')
    elif 'host' in kwargs and 'port' in kwargs and 'database' in kwargs and 'user' in kwargs and 'password' in kwargs:
        if kwargs['host'] is None or kwargs['port'] is None or kwargs['database'] is None or kwargs['user'] is None or \
                kwargs['password'] is None:
            raise TypeError('Connection parameters are incorrect!')
    if 'charset' not in kwargs:
        kwargs['charset'] = "utf8"
    if 'usessl' not in kwargs:
        kwargs['usessl'] = "off"
    #    else:
    #        def_charset=kwargs['charset']

    conn = _connect(host=kwargs['host'],
                            port=int(kwargs['port']),
                            database=kwargs['database'],
                            user=kwargs['user'],
                            password=kwargs['password'],
                            charset=kwargs['charset'],
                            usessl=kwargs['usessl'])
    # conn = Pyxgmodule._connect(*args, **kwargs)
    return conn


def reverse(*args, **kwargs):
    _reverse(*args)


connect = Connection = Connect

# version='v2.1.1'

XG_C_NULL = 0
XG_C_BOOL = 1
XG_C_CHAR = 2
XG_C_TINYINT = 3
XG_C_SHORT = 4
XG_C_INTEGER = 5
XG_C_BIGINT = 6
XG_C_FLOAT = 7
XG_C_DOUBLE = 8
XG_C_NUMERIC = 9
XG_C_DATE = 10
XG_C_TIME = 11
XG_C_TIME_TZ = 12
XG_C_DATETIME = 13
XG_C_DATETIME_TZ = 14
XG_C_BINARY = 15
XG_C_NVARBINARY = 18
XG_C_INTERVAL = 21
DATETIME_ASLONG = 23
XG_C_INTERVAL_YEAR_TO_MONTH = 28
XG_C_INTERVAL_DAY_TO_SECOND = 31
XG_C_TIMESTAMP = 13
XG_C_LOB = 40
XG_C_CLOB = 41
XG_C_BLOB = 42
XG_C_REFCUR = 58
XG_C_NCHAR = 62
XG_C_CHARN1 = 63
