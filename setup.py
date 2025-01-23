from setuptools import setup, find_packages

setup(
    name="geopytools",
    version="1.0.0",
    author="Your Name",
    author_email="youremail@example.com",
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
