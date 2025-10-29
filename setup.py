from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-jazzmin-customizations",
    version="1.0.0",
    author="Muhammad Inaam",
    author_email="your.email@example.com",
    description="The ultimate plug-and-play Django app for Jazzmin admin theme with RTL support, sidebar search, and custom menus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Muhammadinaam/django-jazzmin-customizations",
    packages=['jazzmin_customizations'],
    package_dir={'jazzmin_customizations': '.'},
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=3.2",
        "django-jazzmin>=2.0",
    ],
    keywords="django jazzmin admin rtl arabic urdu sidebar-search multilingual",
)

