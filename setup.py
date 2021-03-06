import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="leaguelosestreakmeter-fhodun",
    version="0.0.1",
    author='Filip Hodun',
    author_email='filiphodun@gmail.com',
    license='GPL-3.0',
    description='Lose streak meter for League of legends',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/fhodun/leaguelosestreakmeter',
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    requires= "riotwatcher",
    install_requires=["riotwatcher"],
)
