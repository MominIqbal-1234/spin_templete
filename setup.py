from setuptools import setup, find_packages



VERSION = '0.5'
DESCRIPTION = "spin templete is the layer of Spin-python-sdk for render html"


# Setting up
setup(
    name="webraft",
    version=VERSION,
    author="mominiqbal1234",
    author_email="<mominiqbal1214@gmail.com>",
    description=DESCRIPTION,
    long_description="""
    # WebRaft

    spin templete is the layer of Spin-python-sdk for render html

    # How to install spin_templete

    ```python
    pip install spin_templete
    ```
    #



    Check Our Site : https://mefiz.com/about </br>
    Developed by : Momin Iqbal

    """,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["django","djangorestframework","PyJWT","fastapi","flask","bottle",'cryptography',"user-agents","django-user-agents"],
    keywords=['webraft','WebRaft''python', 'django', 'jwt', 'jwt for django','create api key','read api key','create token','read token','user agent django','ip info python','user agent python','jwt flask','jwt bottle','jwt fastapi'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
