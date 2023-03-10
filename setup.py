import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fab-ad",                          # This is the name of the package
    version="0.0.7",                        # The initial release version
    author="Saket Joshi, Nikhil Nayak, Harsha Taneru, Nishtha Sardana, Kareema Batool,",
    description="Fab-AD is a Python package for automatic differentiation.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=["fab_ad"], #setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.8',                # Minimum version requirement of the package
    py_modules=["fab_ad"],             # Name of the python package
    package_dir={'':'src'},     # Directory of the source code of the package
    install_requires=["poetry-core>=1.0.0", "setuptools"],   # Install other dependencies if any
    # requires=["poetry-core>=1.0.0", "setuptools"],
    # build-backend="poetry.core.masonry.api"
)