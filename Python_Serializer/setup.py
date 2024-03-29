import setuptools

setuptools.setup(
    name='Python_Serializer',
    version='1.0',
    author='Artem Kozlovski',
    author_email='temshidze777@mail.ru',
    description='Python Serializer to or from json, yaml, toml, pickle',
    url='https://github.com/gitartema/Python4Sem',
    packages=setuptools.find_packages(include=['Converter','Converter.*']),
    entry_points={
      'console_scripts': [
        'myParser=Converter.main_converter:main',
      ],
    },  
    python_requires=">=3.8",
    install_requires=[
        'PyYAML==5.4.1',
        'toml==0.10.0'
    ],
)
