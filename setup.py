from setuptools import setup

setup(
    name="Manga Chapter Reminder",
    version="1.0.0",
    author="Kevin Lu",
    description="Tells what is the latest chapter of a particular manga.",
    long_description="",
    url="",
    python_requires=">=3.7, <4",
    install_requirement=["mysql-connector-python", "requests"],
    entry_points={}
)