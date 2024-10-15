from setuptools import setup, find_packages

setup(
    name='youtube-transcriber',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client==2.86.0',
        'google-auth-oauthlib==1.0.0',
        'youtube-transcript-api==0.6.0',
        'python-dotenv==1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'youtube-transcriber=cli:main',
        ],
    },
)
