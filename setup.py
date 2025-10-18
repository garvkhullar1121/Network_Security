from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements.

    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",'r') as files:
            lines = files.readlines()

            for line in lines:
                requirement = line.strip()
                # ignore empty line and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found")
    
    return requirement_lst
print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author = "Garv",
    author_email="gkhullar_be23@thapar.edu",
    packages = find_packages(),
    install_requires = get_requirements()
)
