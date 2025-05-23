from setuptools import setup

with open("README.md", "r") as readme:
    README = readme.read()

version = "0.1.2"

setup(
    name="fastapi-pypendency",
    version=version,
    url="https://github.com/jdiazromeral/fastapi-pypendency",
    license="MIT License",
    author="Javier Díaz-Romeral Torralbo",
    author_email="javierdiazromeral@gmail.com",
    description="Pypendency integration with FastAPI",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["fastapi_pypendency"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["pypendency>=0.5.0", "fastapi>=0.115.5"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: FastAPI",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
    python_requires=">=3.13",
)
