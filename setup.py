import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyWeCom",
    version="0.0.1",
    author="alex",
    author_email="liu_zhao_feng_alex@163.com",
    description="WeCom SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Matrix-King-Studio/PyWeCom",
    project_urls={
        "Bug Tracker": "https://github.com/Matrix-King-Studio/PyWeCom/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
