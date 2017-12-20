from setuptools import setup, find_packages

package_name = 'ropa'
version = '1.0'

packages = find_packages()

install_requires = ['filebytes>=0.9.12', 'capstone==3.0.4',
                    'keystone-engine', 'ropper==1.11.2', 'pyvex']

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

    author="Daniel Lim, Jeff Sieu, Owen Leong",
    description='ropa is a Ropper-based GUI that streamlines'
                'crafting ROP chains.',
    license='GNU General Public License v3.0',
    url='https://orppra.github.io/ropa/',
)
