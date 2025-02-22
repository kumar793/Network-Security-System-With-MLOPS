from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements:List[str]=[]
    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print("requirements file is not found")

    return requirements

setup(
name='MLOPS- Network Security',
version='0.0.1',
author='Kumar',
author_email='vnkumarvoleti@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)