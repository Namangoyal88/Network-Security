'''
The setup.py file is used to define the package metadata and dependencies for the NetworkSecurity project.
It includes the package name, version, author, description, and the required packages for the project.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str)-> List[str]:
    '''
    This function reads the requirements file and returns a list of required packages.
    '''
    requirement_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines() #read lines from the file
            for line in lines: #Process each line
                requirement = line.strip()
                if requirement and requirement != '-e .': #ignore empty lines and -e .
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    
    return requirement_list

print(get_requirements('requirements.txt'))

setup(
    name = 'NetworkSecurity',
    version = '0.0.1',
    author = 'Naman Goyal',
    author_email = 'goyalnaman497@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)