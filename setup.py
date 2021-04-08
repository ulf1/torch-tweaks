from setuptools import setup
import pypandoc


setup(name='torch-tweaks',
      version='0.1.0',
      description='Utility functions for PyTorch.',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/torch-tweaks',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['torch_tweaks'],
      install_requires=[
          'setuptools>=40.0.0',
          'torch>=1.0.0'],
      python_requires='>=3.6',
      zip_safe=True)
