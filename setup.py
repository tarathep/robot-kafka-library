from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="robot-kafka-library",
    version="0.0.3",
    author="tarathep",
    author_email="bokie.tarathep@gmail.com",
    description="robotframework exetension lib for test kafka",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tarathep/robot-kafka-library",
    license="MIT",
    packages=find_packages(),
    package_dir={'robotKafkaLibrary': 'RobotKafkaLibrary'},
    install_requires=[
        'kafka-python'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)