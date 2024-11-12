from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf8") as f:
    description = f.read()

setup(
    name="jumppng",
    version="0.2.1",
    packages=find_packages(),
    install_requires=["Pillow"],
    entry_points={
        "console_scripts": ["jumppng = jumppng:jump_png"],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)
