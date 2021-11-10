from setuptools import setup, find_packages

setup(
    name='slack',
    version='1.0.0',
    install_requires=[
        'requests'
    ],
    description='Slack module for Python',
    url='git@github.com:yumaeda/slack.git',
    author='Yukitaka Maeda',
    author_email='yumaeda@gmail.com',
    license='GNU General Public License v3.0',
    packages=find_packages(),
    zip_safe=False
)

