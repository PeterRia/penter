import os
import sys
from setuptools import setup, find_packages

setup(
    name="demo",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'demo = demo.hello:hello'
        ],
    },
    package_data={
        'demo': ['*.txt']
    },
    author="the5fire",
    author_email='kingreatwill@qq.com',
    url="http://www.kingreatwill.com",
    description='a demo for setuptools',
)
