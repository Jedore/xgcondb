# SPDX-FileCopyrightText: 2024-present Jedore <jedorefight@gmail.com>
#
# SPDX-License-Identifier: MIT

import xgcondb as xg


def connect():
    try:
        conn = xg.connect(host='127.0.0.1',
                   port=5138,
                   database='SYSTEM',
                   user='SYSDBA',
                   password='SYSDBA')
        conn.close()
        print('Succeeded!')
        return True
    except Exception as e:
        print('Failed!', e)
        return False


if __name__ == '__main__':
    connect()
