from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Hoori pathplanning'
LONG_DESCRIPTION = 'Hoori pathplanning'

# Setting up
setup(
       # the name must match the folder name
        name="pathplanning",
        version=VERSION,
        author="Hoori",
        author_email="<justine.fricou@epitech.eu>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'pathplanning']
)