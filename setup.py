from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='robot-kafka-library',
    version='0.1',
    description='for test message from kafka with robot framework',
    long_description=readme(),
    url='https://github.com/tarathep/robot-kafka-library',
    author='Tarathep',
    author_email='bokie.tarathep@gmail.com',
    license='Tarathep',
    install_requires=[
        'kafka-python'
    ],
    scripts=['bin/grandmasomsri-status'],
    keywords='robot-fafka-library',
    packages=['robot-kafka-library'],
    package_dir={'robot-kafka-library': 'src/robot-kafka-library'},
    package_data={'robot-kafka-library': ['graph/*.py']
    },
)