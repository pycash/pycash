import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pycash',  
     version='0.0.1-b0',
     author="Patrick Phat Nguyen",
     author_email="me@patrickphat.com",
     description="PyCash: a general Python package for money-pulation",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/pycash/pycash",
     packages=setuptools.find_packages(exclude=['docs', 'tests', 'experiments']),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial",
         "Intended Audience :: Developers",
         "Intended Audience :: Financial and Insurance Industry",
         "License :: OSI Approved :: Apache Software License",
         "Programming Language :: Python :: 3"
     ],
     python_requires='>3.6',
     install_requires=[],
     extras_require={
         'dev': [
             'pytest',
             'coverage',
             ],
     }
 )
