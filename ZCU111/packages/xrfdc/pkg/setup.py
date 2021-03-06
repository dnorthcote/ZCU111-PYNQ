from setuptools import find_packages, setup

setup(
   name = "xrfdc",
   version = '0.2',
   url = 'https://github.com/Xilinx/ZCU111-PYNQ/tree/master/ZCU111/packages/xrfdc',
   license = 'All rights reserved.',
   author = "Craig Ramsay",
   author_email = "cramsay01@gmail.com",
   packages = find_packages(),
   package_data = {
   '' : ['*.py','*.so','*.c'],
   },
   install_requires=[
       'pynq',
       'wurlitzer',
   ],
   description = "Driver for the RFSoC RF Data Converter IP"
)
