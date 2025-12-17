from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements
REPO_NAME = "ML Based Books Recommender System"
AUTHOR_USER_NAME = "mohdamaan9897"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small local package for ML Based Books Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohdamaan9897/End-to-End-Books-Recommender-System",
    author_email="khanamaan44696@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)