import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygmc300e",
    version="0.0.1",
    author="Sebastian Heppner",
    description="A python serial interface to a GMC 300E Plus Geiger Counter",
    long_description=long_description,
    long_description_context_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.8"
)
