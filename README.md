# XuGu-Python-Driver

<a href="#"><img src="https://flat.badgen.net/badge/os/windows-x86_64/cyan?icon=windows" /></a>
<a href="#"><img src="https://img.shields.io/badge/os-linux_x86_64-white?style=flat-square&logo=linux&logoColor=white&color=rgb(35%2C189%2C204)" /></a>
<a href="#"><img src="https://flat.badgen.net/badge/python/3.6|3.7|3.8|3.9/blue" /></a>
<a href="#"><img src="https://flat.badgen.net/badge/pypi/v0.0.1/blue" /></a>
<a href="https://pepy.tech/project/xgcondb" ><img src="https://static.pepy.tech/badge/xgcondb" /></a>

虚谷数据库Python接口驱动包

### 安装

```bash
pip install xgcondb -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host=pypi.tuna.tsinghua.edu.cn
```

### 使用
```python
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
    except Exception as e:
        print('Failed!', e)


if __name__ == '__main__':
    connect()
```

具体使用参考官方链接 [Python标准接口开发指南](https://help.xugudb.com/documents/python-development-guide/program-guide-01)
