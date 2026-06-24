# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# 收集 Scripts 目录下所有 .py 文件
scripts_dir = os.path.join('Scripts')
scripts_py = [os.path.join('Scripts', f) for f in os.listdir(scripts_dir) if f.endswith('.py')]

# 收集 datasets 目录下所有文件
datasets_dir = os.path.join('Scripts', 'datasets')
datasets_files = collect_data_files(datasets_dir)

# 收集 Scripts 目录下所有非 py 文件
scripts_data = collect_data_files('Scripts')

# 主程序入口
main_script = 'SimpleKaruzi.py'

a = Analysis(
    [main_script] + scripts_py,
    pathex=[],
    binaries=[],
    datas=scripts_data + datasets_files,
    hiddenimports=collect_submodules('Scripts'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='SimpleKaruzi',
    console=False,
    icon=None,
)
