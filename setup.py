from setuptools import setup, find_packages

setup(
    name="nico-cfo",
    version="1.0.0",
    description="AI-powered personal and business finance command center",
    author="Nico Lundquist",
    author_email="nico@amplifyaisolutions.com",
    python_requires=">=3.11",
    install_requires=[
        "plaid-python>=29.0.0",
        "Flask>=3.1.0",
        "keyring>=25.6.0",
        "mcp>=1.26.0",
        "sqlcipher3>=0.6.0",
    ],
    extras_require={
        "dev": ["pytest>=8.0.0"],
    },
)
