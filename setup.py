import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        subprocess.call('scripts/post_install.sh')
        install.run(self)


package_name = 'ropa'
version = '1.1.5'

packages = find_packages()

install_requires = ['filebytes>=0.9.12', 'capstone==3.0.5rc2',
                    'keystone-engine', 'ropper==1.11.2', 'pyvex',
                    'pyperclip>=1.6.0']

setup(
    name=package_name,
    version=version,
    packages=packages,
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'gui_scripts': [
            'ropa = ropa.__main__:main'
        ]
    },
    cmdclass={
        'install': PostInstallCommand,
    },

    author="Daniel Lim, Jeff Sieu, Owen Leong",
    description='GUI tool to create ROP chains using the ropper API',
    license='GNU General Public License v3.0',
    classifiers=[
        'Topic :: Security',
        'Environment :: X11 Applications :: Qt',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Intended Audience :: Education'
    ],
)
