from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    # package name in pypi
    name='lightning',
    # extract version from module.
    version=__version__,
    description="",
    long_description="",
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
        'Django==1.9.3',
    ],
)
