from setuptools import setup, find_packages
#from pip.req import parse_requirements
setup(
    name='paq',
    version='0.1.0',
    packages=find_packages(),
    description='Operaciones de Suma y Resta',
    author='Tonio',
    author_email='jlaville@ifc.unam.mx',
    url='https://github.com/jlaville/paq',
    install_requires=parse_requirements("requirements.txt",session='hack')      
    ,
)