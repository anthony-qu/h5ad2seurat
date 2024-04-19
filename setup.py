from setuptools import setup, find_packages

setup(
    name='h5ad2seurat',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'h5ad2seurat=h5ad2seurat.h5ad2seurat:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        'scanpy',       # Scanpy is required for handling h5ad files.
        'scipy',        # SciPy may be required indirectly by Scanpy for some operations.
        # 'scanpy>=1.4',  # Ensures a minimum version of Scanpy if required
        # 'scipy>=1.4',   # Ensures a minimum version of SciPy if required
    ]
)