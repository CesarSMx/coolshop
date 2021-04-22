from setuptools import setup


setup(
name='cs',
version='0.1',
py_module=['cs'],
install_requires=[
    'Click',
],
entry_points='''
    [console_scripts]
    cs=cs:cli
    '''
)