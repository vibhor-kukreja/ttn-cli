import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ttncli",
    version="0.0.1",
    author="TTN",
    author_email="vibhor.kukreja@tothenew.com",
    description="Command line utility for TTN employers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vibhor-kukreja/ttn-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'ttn_cli=ttn_cli:main',
        ],
    },
    python_requires='>=3.6',
)
