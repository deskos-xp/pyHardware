import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='phw',  
     version='0.1',
     #packages=['hw'],
     author="Karl Josef Wisdom",
     author_email="k.j.hirner.wisdom@gmail.com",
     description="A lspci/lscpu/dmidecode cmd parser to get hardware info",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/deskos-xp/pyHardware",
     packages=setuptools.find_packages(),
     package_data={'hw':['hw/etc/commands.json']},
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: POSIX :: Linux",
     ],
 )
