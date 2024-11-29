from setuptools import setup, find_packages

# Function to read requirements from requirements.txt
def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

setup(
    name='paq',  # Name of your package
    version='0.1',  # Version of your package
    author='Juan',  # Your name
    author_email='jlaville@ifc.unam.mx',  # Your email
    description='Paquete de operaciones',  # Short description
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=read_requirements('requirements.txt'),  # Read from requirements.txt
    classifiers=[  # Optional: Classifiers to categorize your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)