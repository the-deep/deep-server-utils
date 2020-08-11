from setuptools import setup, find_namespace_packages

setup(
    name='deep_utils.deduplication',
    version='1.0.0',
    description='Document deduplication package for DEEP',
    author='Bibek Pandey',
    author_email='bibek.pandey@togglecorp.com',
    packages=find_namespace_packages(),
    license="MIT",
    long_description_content_type='text/markdown',
    long_description=open('./README.md').read(),
    url="https://github.com/the-deep/deep-server-utils",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
    ],
    install_requires=open('deep_utils/deduplication/requirements.txt').read().split(),
    zip_safe=False
)
