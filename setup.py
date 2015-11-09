from setuptools import setup, find_packages

setup(
    name='porticus',
    version=__import__('porticus').__version__,
    description=__import__('porticus').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='dthenon@emencia.com',
    url='http://pypi.python.org/pypi/porticus',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        "Framework :: Django :: 1.7",
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Django>=1.7',
        'django-filebrowser-no-grappelli>=3.5.6',
        'django-mptt>=0.6.1',
        'django-tagging>=0.3.2',
    ],
    include_package_data=True,
    zip_safe=False
)
