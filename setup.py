import setuptools

setuptools.setup(
    name="twitbot-tih",
    author="@syncomo",
    version="1.0.0",
    description="A Twitter bot that tweets today-in-history events",
    install_requires=[
        "wikipedia>=39.0.1",
        "twython>=3.7.0",
        "pyOpenSSL>=19.0.0",
        "ndg-httpsclient>=0.5.1",
        "pyasn1>=0.4.5",
    ]
)
