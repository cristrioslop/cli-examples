from setuptools import setup, find_packages

packages = find_packages()

setup(
    name="cli-test",
    version="0.0.1",
    description="Cli test",
    author="Cris",
    author_email="cristianleonardo.rioslopez@mercadolibre.com",
    url="git@github.com:mercadolibre/fury_python-bi-cluster-manager.git",
    packages=packages,
    entry_points={"console_scripts": ["cli=app.cli:main", "cli2=app.cli2:main"]},
    install_requires=[
        "click",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
)
