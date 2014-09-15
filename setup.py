from setuptools import setup

setup(
    name="ftpbench",
    version="1.0",
    packages=["ftpbench"],
    url="http://github.com/selectel/ftpbench",
    license="MIT",
    author="Konstantin Enchant",
    author_email="sirkonst@gmail.com",
    description="Benchmark for ftp servers",
    long_description=open("README").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Framebuffer",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Topic :: System :: Benchmark",
        "Topic :: Utilities",
    ],
    install_requires=[
        "setuptools", "gevent", "dnspython", "Timecard", "docopt"
    ],
    entry_points={
        "console_scripts": ["ftpbench = ftpbench.ftpbench:main"]
    }
)
