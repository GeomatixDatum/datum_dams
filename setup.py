from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in datum_dams/__init__.py
from datum_dams import __version__ as version

setup(
	name="datum_dams",
	version=version,
	description="a repository of Nigerian dams with basic profile features for each dam",
	author="Geomatix",
	author_email="info@geomatix.ng",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
