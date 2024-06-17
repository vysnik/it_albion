from setuptools import setup, find_packages

setup(
    name='m3_project',
    version='1.0.0',
    author='Никита Выскубов',
    author_email='vysnik@gmail.com',
    description='Тестовое задание',
    url='URL вашего проекта, если есть',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Operating System :: Ubuntu 22.04.4 LTS',
    ],
    install_requires=[
        'django==2.2.2',
        'm3-django-compat @ git+https://github.com/barsgroup/m3-django-compat.git#egg=m3-django-compat'
        'm3-objectpack==2.2.47',
    ],
    python_requires='==3.9',
)
