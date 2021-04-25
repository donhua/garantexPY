#!/usr/bin/env python3
# coding: utf-8
from cx_Freeze import setup, Executable


executables = [Executable(script='main.py',
                          targetName='garantex.exe',
                          icon='ico.ico',
                          shortcut_name='gar'
                          )
               ]

# not include python modules
excludes = ['logging',
            'unittest',
            'email',
            ]

includes = ['requests']

# include python modules to zip
zip_include_packages = ['collections',
                        'encodings',
                        'importlib'
                        ]

# include Microsoft Visual C++ Redistributable
options = {
    'build_exe': {
        'include_msvcr': True,
        'includes': includes,
        'excludes': excludes,
        'zip_include_packages': zip_include_packages,
    }
}


setup(name='SmartGarantex',
      version='0.0.1',
      description='For Garantex.io',
      executables=executables)
