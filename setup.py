import re
from setuptools import setup

def getLongDescription():
	"""
	This definition returns the Package long description.

	:return: Package long description. ( String )
	"""

	description = []
	with open("README.rst") as file:
		for line in file:
			if ".. code:: python" in line and len(description) >= 2:
				blockLine = description[-2]
				if re.search(r":$", blockLine) and not re.search(r"::$", blockLine):
					description[-2] = "::".join(blockLine.rsplit(":", 1))
				continue

			description.append(line)
	return str().join(description)

setup(name="Counter",
	version="1.0.0",
	author="Thomas Mansencal",
	author_email="thomas.mansencal@gmail.com",
	include_package_data=True,
	py_modules=["counter"],
	url="https://github.com/KelSolaar/Counter",
	license="MIT",
	description="Counter package defines the \"counter.Counter\" class similar to bags or multisets in other languages.",
	long_description=getLongDescription(),
	install_requires=[],
	classifiers=["Development Status :: 5 - Production/Stable",
				"Environment :: Console",
				"Intended Audience :: Developers",
				"License :: OSI Approved :: MIT License",
				"Natural Language :: English",
				"Operating System :: OS Independent",
				"Programming Language :: Python",
				"Topic :: Utilities"])
