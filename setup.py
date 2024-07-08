from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='python-test',  # Replace with your project name
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'myapp=app:main',  # Adjust this if you have a specific entry point
        ],
    },
    include_package_data=True,
    python_requires='>=3.6',
)
