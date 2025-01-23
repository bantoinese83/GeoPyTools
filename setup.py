from setuptools import setup, find_packages

setup(
    name="geotools",
    version="1.0.0",
    author="Bryan Antoine",
    author_email="b.antoine.se@gmail.com",
    description="A Python package for geospatial tools",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
