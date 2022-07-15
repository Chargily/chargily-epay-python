import os

from setuptools import setup, find_packages


import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


sync_data = {
    "name": "chargily-epay-python",
    "exclude": ["chargily_lib.async_lib"],
    "install_requires": ["requests==2.27"],
}

async_data = {
    "name": "chargily-epay-Async",
    "exclude": ["chargily_lib.sync_lib"],
    "install_requires": ["aiohttp==3.8"],
}

build_arg = None

build_type = os.getenv("BUILD_TYPE", "sync")

if build_type == "sync":
    build_arg = sync_data
elif build_type == "async":
    build_arg = async_data
else:
    raise ValueError("build_type should be sync or async")


setup(
    name=build_arg["name"],  # Required
    version="0.0.2",  # Required
    description="Chargily ePay Gateway (Python Library)",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/Chargily/chargily-epay-python",  # Optional
    author="Chargily",  # Optional
    author_email="developers@chargily.com",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="e-pay, chargily, edahabia, cib",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src", exclude=build_arg["exclude"]),  # Required
    python_requires=">=3.7",
    install_requires=build_arg["install_requires"],  # Optional
    project_urls={  # Optional
        "Bug Reports": "https://github.com/Chargily/chargily-epay-python/issues",
        "Say Thanks!": "https://github.com/Chargily",
        "Source": "https://github.com/Chargily/chargily-epay-python/",
        "Website": "https://chargily.com/",
    },
)
