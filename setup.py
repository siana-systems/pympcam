import setuptools
import pympcam

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pympcam",
    version=pympcam.__version__,
    author=pympcam.__author__,
    author_email=pympcam.__email__,
    description="A Python library to manage Hardware on MPCam boards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/sianasystems/mpcam-pympcam",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
)