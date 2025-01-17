from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='pyntcloud',
    version=version,
    description='Python library for working with 3D point clouds.',
    url='https://github.com/daavoo/pyntcloud',
    author='David de la Iglesia Castro',
    author_email='daviddelaiglesiacastro@gmail.com',
    license='The MIT License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
    ],
     extras_require={
        'LAS':  ["laspy"],
        'PLOT': ["ipython", "matplotlib", "pyvista"],
        'NUMBA': ["numba"]
    }
)
