from setuptools import setup, find_packages

setup(
    name="datafaker",
    version="1.0.0",
    description="CLI tool to generate fake data for testing and prototyping",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jerrytriple8",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "datafaker=datafaker.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
