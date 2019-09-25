import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="regex_engine",
    version="1.1.0",
    author="Raj Kiran P",
    author_email="rajkiranjp@gmail.com",
    description="Generate regex using python that can fit your needs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raj-kiran-p/regex_engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
