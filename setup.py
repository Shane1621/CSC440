from setuptools import setup, find_packages

setup(
    name='CSC440',
    description='Project for CSC-440 Fall 2020',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    
    ],
    entry_points={
        'console_scripts': [
            'csc-440=CSC-440:main',
            
        ],
    },
    
)
