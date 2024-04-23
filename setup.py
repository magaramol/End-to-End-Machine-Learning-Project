from setuptools import find_packages,setup



from typing import List


hyphn='-e .'


def get_requirements(file_path:str)->List[str]:


    """
    This function will return list of requirements
    
    """

    requirements=[]


    with open(file_path) as file_obj:

        requirements=file_obj.readlines()
        requirements= [req.replace('\n',' ') for req in requirements]


        if hyphn in requirements:
            requirements.remove(hyphn)
    return requirements




setup(


    name='Ml project',
    version='0.0.1',
    author='Amol Magar',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')



)