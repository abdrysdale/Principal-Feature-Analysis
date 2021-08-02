import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="principal-feature-analysis",
    version="0.0.1",
    author="Tim Breitenbach & Lauritz Rasbach",
    author_email="tim.breitenbach@mathematik.uni-wuerzburg.de, rasbachlauritz@googlemail.com",
    description="The first package for Principal Feature Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
