import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='render_browser',  
     version='0.5',
     author="Dhruv Ramani",
     author_email="dhruvramani98@gmail.com",
     description="Render gym environments to a web browser.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/dhruvramani/gym-render-browser",
     packages=setuptools.find_packages(),
     include_package_data = True,
     install_requires=[
        'Flask',
        'opencv-python',
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
