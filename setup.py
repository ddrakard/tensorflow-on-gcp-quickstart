from setuptools import find_packages, setup

with open("README.md", 'r') as file:
    long_description = file.read()

setup(
    name='Tensorflow on GCP quickstart',
    version='0.1',
    description=(
        'A template to use as a base to quickly and easily get started running'
        + ' Tensorflow code on Google Cloud Platform interactively or on '
        + ' Vertex AI jobs, with GPU acceleration enabled.'
    ),
    long_description=long_description,
    url='',
    author='David Drakard',
    author_email='research@ddrakard.com',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
    ],
    zip_safe=False
)
