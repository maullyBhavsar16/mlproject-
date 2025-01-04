from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirments(file_path: str) -> List[str]:
    """
    This function will return a list of requirements from the given file.
    """
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            # Strip newlines and extra spaces
            requirements = [req.strip() for req in requirements]
            # Remove editable install entry
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Maully',
    author_email='bhavsarmaully@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt'),
)
