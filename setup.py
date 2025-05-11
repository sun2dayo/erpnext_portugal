from setuptools import setup, find_packages

setup(
    name='erpnext_portugal',
    version='0.0.1',
    description='Localização fiscal portuguesa para ERPNext',
    author='NovaDX - Octávio Daio',
    author_email='app@novadx.eu',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'frappe',
        'lxml',
        'jinja2'
    ]
)
