"""
@Author: Jedore(https://github.com/jedore)
@Date: 17/08/2024
@brief: auto-build
"""

# 1. python auto_build.py
# 2. create docker container quay.mirrors.ustc.edu.cn/pypa/manylinux2014_x86_64:2023-10-22-409125c
# 3. export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<libxugusql.so path>
# 4. auditwheel repair -w . <linux x86_64 whl>
# linux arm64 whl same to upper, repaired on linux aarch64 or quay.io/pypa/manylinux2014_aarch64

# Same method not support for python 3.6/3.7

import time
import os
import shutil
from pathlib import Path
from src.xgcondb import __about__

driver_base = Path('driver')
platforms = ('win-x64', 'linux-x64', 'linux-arm64')
pythons = ('36', '37', '38', '39', '310', '311')
package_dir = Path('src/xgcondb')


def prepare(platform: str, python_version: str):
    files = ['__init__.py']
    if platform == 'win-x64':
        files.extend([
            'xugusql.dll',
            f'_pyxgdb{python_version}.pyd',
        ])
    elif platform == 'linux-x64':
        if python_version in ('36', '37'):
            python_version += 'm'
        files.extend([
            # 'libxugusql.so',
            '_pyxgdb.so',
            f'_pyxgdb.cpython-{python_version}-x86_64-linux-gnu.so',
        ])
    elif platform == 'linux-arm64':
        if python_version in ('36', '37'):
            python_version += 'm'
        files.extend([
            # 'libxugusql.so',
            '_pyxgdb.so',
            f'_pyxgdb.cpython-{python_version}-aarch64-linux-gnu.so',
        ])

    for file in files:
        shutil.copy(driver_base / platform / file, package_dir)


def clean():
    for file in os.listdir(package_dir):
        if file not in ('__about__.py', '__pycache__'):
            os.remove(package_dir / file)


def build():
    os.system('hatch build -t wheel')


def re_rag(platform: str, python_version: str):
    if platform == 'win-x64':
        plat = 'win_amd64'
    elif platform == 'linux-x64':
        plat = 'manylinux2014_x86_64.manylinux_2_17_x86_64'
    elif platform == 'linux-arm64':
        plat = 'manylinux2014_aarch64.manylinux_2_17_aarch64'

    if python_version in ('36', '37'):
        abi_tag = f'cp{python_version}m'
    else:
        abi_tag = f'cp{python_version}'

    cmd = (f'wheel tags --remove '
           f'--platform-tag {plat} '
           f'--abi-tag  {abi_tag} '
           f'--python-tag cp{python_version} '
           f'dist/xgcondb-{__about__.__version__}-py3-none-any.whl')
    os.system(cmd)


def main():
    t_start = time.time()
    print('Start auto build...')
    for platform in platforms:
        for py in pythons:
            if platform == 'linux-arm64' and py in ('310', '311'):
                continue

            print(f'> Platform {platform}, Python {py}')
            clean()
            prepare(platform, py)
            build()
            re_rag(platform, py)

    clean()

    print("Total time(s):", int((time.time() - t_start) / 1000))


if __name__ == '__main__':
    main()
