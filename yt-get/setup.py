from distutils.core import setup

setup(
    # Application name:
    name="yt-get",
    
    # Version number (initial):
    version="0.1.0",
    
    # Application author details:
    author="hidden relic",
    author_email="the.true.hidden.relic@gmail.com",
    
    # Packages
    packages=[],
    
    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="http://pypi.python.org/pypi/yt-get_v010/",
    
    #
    license="LICENSE.txt",
    description="MIT",
    
    long_description=open("README.txt").read(),
    
    # Dependent packages (distributions)
    install_requires=[
        "re",
		"pytube",
		"validators",
		"time",
		"sys",
		"datetime",
		"configparser",
		"pathlib",
		"os",
    ],
)