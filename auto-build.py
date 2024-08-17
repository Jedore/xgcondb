"""
@Author: jedor(https://github.com/jedore)
@Date: 17/08/2024
@brief: auto-build
"""

import time
import os
import shutil
from pathlib import Path
from src.xgcondb import __about__

driver_base = Path('driver')
platforms = ('win-x64', 'linux-x64', 'linux-arm64')
pythons = ('36', '37', '38', '39')
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
            'libxugusql.so',
            '_pyxgdb.so',
            f'_pyxgdb.cpython-{python_version}-x86_64-linux-gnu.so',
        ])
    elif platform == 'linux-arm64':
        if python_version in ('36', '37'):
            python_version += 'm'
        files.extend([
            'libxugusql.so',
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

    cmd = (f'wheel tags --remove '
           f'--platform-tag {plat} '
           f'--abi-tag cp{python_version} '
           f'--python-tag cp{python_version} '
           f'dist/xgcondb-{__about__.__version__}-py3-none-any.whl')
    os.system(cmd)


def main():
    t_start = time.time()
    print('Start auto build...')
    for platform in platforms:
        for py in pythons:
            print(f'> Platform {platform}, Python {py}')
            clean()
            prepare(platform, py)
            build()
            re_rag(platform, py)

    clean()

    print("Total time(s):", int((time.time() - t_start) / 1000))


if __name__ == '__main__':
    main()
