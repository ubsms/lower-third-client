from setuptools import setup

setup(
    name='lowerthirdclient',
    version='0.1.0',    
    description='A lower third client for CasparCG',
    url='https://github.com/ubsms/lower-third-client',
    author='Richard Franks',
    author_email='richard@ubsms.org.uk',
    license='MIT',
    packages=['lowerthirdclient'],
    install_requires=['amcp-pylib>=0.2.2',
                      'wxpython',                    
                      ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications',
        'Intended Audience :: Religion',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
    ],
)