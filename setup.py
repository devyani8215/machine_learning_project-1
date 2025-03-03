from setuptools import setup
from typing import List


#Declaring variables for setup functions.
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Devyaniba Chudasama"
DESCRIPTION="This is a first Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of
    requirements mentioned in requirements.txt file

    return: This func is going to return a list which contain
    name of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(

    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())