import os
from setuptools import setup, find_packages

def get_template_files():
    matches = []
    for root, dirnames, filenames in os.walk('faq/templates'):
        matches.extend([os.path.join(root, filename) for filename in filenames])
    print matches
    return matches

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-faq',
    version = '0.1.0',
    description = 'A simple FAQ application for Django sites.',
    long_description = read('README.rst'),
    
    author  ='Kevin Fricovsky',
    author_email = 'kfricovsky@gmail.com',
    url = 'http://github.com/howiworkdaily/django-faq',
    
    packages = find_packages(exclude=['example']),
    zip_safe = False,
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    
    install_requires = ['setuptools', 'Django >= 1.3'],
    test_suite = "faq._testrunner.runtests",
    data_files = [('faq/templates/faq', ['faq/templates/faq/faq_plugin.html'])]
)
