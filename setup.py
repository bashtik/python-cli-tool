from setuptools import setup, find_packages

setup(
    name="cli_tool",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'greet=cli_tool.main:main',
        ],
    },
)
