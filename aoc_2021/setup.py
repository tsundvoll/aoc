from setuptools import find_packages, setup

setup(
    name="aoc_2021",
    description="Solutions for Advent of Code 2021",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="0.1.0",
    author="Thomas Sundvoll",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib",
        "networkx",
        "numpy",
        "opencv-python",
        "pyperclip",
        "pytest",
        "python-dotenv",
        "requests",
        "tqdm",
    ],
    setup_requires = [
        "setuptools",
    ],
    entry_points = {
        'console_scripts': [
            'solve = solve:main'
        ]
    }
)
