from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements from the given file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != '']
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name='ML Project',
    version='0.01',
    author='Sradha',
    author_email='sradharam2474@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
