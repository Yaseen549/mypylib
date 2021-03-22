import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pymywebweb",
	version="0.0.1",
	author="Mohamed Yaseen Sheriff S",
	author_email="fantasticyaseenshariff@gmail.com",
	description="A startup python webmaker kit",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Yaseen549/mypylib",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)