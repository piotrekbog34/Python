
from setuptools import setup

def do_setup(args_dict):
    setup(**args_dict)

#######################################

from setuptools import setup

def do_setup(args_dict, requires):
    args_dict["install_requires"] = requires
    setup(**args_dict)

#######################################















