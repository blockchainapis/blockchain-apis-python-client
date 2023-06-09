from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name = "blockchain-apis",
    version = "0.1.2",
    author = "Clarensia",
    author_email = "contact@blockchainapis.io",
    description = "Fastest and easiest way to access decentralized finance data",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://www.blockchainapis.io",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Natural Language :: English',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Office/Business',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='blockchain crypto cryptocurrency api arbitrage trading ethereum financial-data financial-analysis sdk python defi dex',
    project_urls = {
        'Documentation': 'https://api.blockchainapis.io/docs',
        'Source': 'https://github.com/blockchainapis/blockchain-apis-python-client',
        'Tracker': 'https://github.com/blockchainapis/blockchain-apis-python-client/issues',
        'Discord': 'https://discord.gg/GphRMJXmS5'
    },
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    install_requires = [
        'aiohttp',
        'requests'
    ],
    python_requires = '>=3.10'
)
