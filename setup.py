from setuptools import setup, find_packages


setup(
    name='slurm-snap-manager',
    packages=find_packages(include=['slurm_snap_manager']),
    version='0.0.1',
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[],
)
