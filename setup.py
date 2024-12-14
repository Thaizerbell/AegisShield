from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="aegis-shield",
    version="1.0.0",
    author="Aegis Shield Team",
    author_email="support@aegisshield.com",
    description="A comprehensive security system for enterprise applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aegisshield/aegis-shield",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "aegis=aegis_shield.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "aegis_shield": ["config/*.json"],
    },
)
