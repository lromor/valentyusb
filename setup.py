
from setuptools import find_namespace_packages, setup

setup(
    name='valentyusb',
    version='0.1',
    packages=find_namespace_packages(include=['valentyusb.*']),
    description='Litex/migen usb implementation.',
)
