from setuptools import setup, find_packages

setup(
    name="text_preprocessor",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A Python module for preprocessing text for NLP tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/text_preprocessor",
    packages=find_packages(),
    install_requires=[
        "textblob>=0.15.3",
        "nltk>=3.7"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
