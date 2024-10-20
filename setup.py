from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="document-password-remover",
    version="1.0.0",
    author="Tomás Bernal Zuluaga",
    author_email="tbernalz@eafit.edu.co",
    description="A Python tool to remove passwords from documents such as PDFs, Word, and Excel files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tbernalz/document-password-remover",
    project_urls={
        "Bug Tracker": "https://github.com/tbernalz/document-password-remover/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    py_modules=["main"],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "document-password-remover=main:main",
        ],
    },
)
