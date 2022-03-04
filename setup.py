from setuptools import setup

setup(
    name='docker_api',
    version='0.1.0',
    description='a python tools .',
    # long_description=open('README.rst').read(),
    author='zhengzongwei',
    author_email='zhengzongwei@foxmail.com',
    packages=['docker_api'],
    install_requires=['docker>=4.2.2']
)
