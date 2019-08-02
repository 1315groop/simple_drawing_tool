from setuptools import setup, find_packages

setup(
    name="draw_man",
    version="1.0",
    author="Pavel Karshakevich",
    author_email="pashakorsh@gmail.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["draw_man = draw_man.cli:main"]},
    description="dimle  drawing tool",
    py_modules=["draw_man"],
)
