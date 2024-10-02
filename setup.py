from setuptools import setup, find_packages

setup(
    name="ia_simples",
    version="0.1",
    packages=find_packages(),
    install_requires=["openai"],
    author="Josyel Buenos",
    author_email="josyelbuenos",
    description="Uma biblioteca simples para integrar a OpenAI com Python em português, de forma totalmente simplificada.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/josyelbuenos/ia_simples",  # Repositório opcional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
