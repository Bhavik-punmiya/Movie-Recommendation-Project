from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path : str):
    # this function will read the requirements file and return the list of requirements
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()  # Corrected here
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

        


setup(
name = 'movie-recommendation system',
version='0.0.1',
author='Bhavik Punmiya',
author_email='Bhavikpunmiya@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)