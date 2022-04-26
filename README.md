## Project title: Yonder Challenge
## Project Description: A python script to show the user the differences between two tags of a Docker Image

A Docker Image is a template that can be used to create/build a bunch of containers.Various images cand be pulled from the Docker Registry  https://hub.docker.com. Every image has tags, which represents the versions of that particular image.Each version has new features, and in this challenge I had to show what changed between two different tags of a single image.

The created python script can be used as follows:
``` 
python3 docker.py --image <image_name> --first-tag <version1> --second-tag <version2>

python3 docker.py --image alpine --first-tag 3.13 --second-tag 3.14
``` 

I made use of the **optparse** module, from which I used the OptionParser() class, respectively the add_option() and parse_args() functions.The documentation can be found here:
https://docs.python.org/3/library/optparse.html?highlight=optparse#module-optparse

This module is usefull for recognizing the user input and for parsing the result.
The **add_option function()** is useful for running the user input, displaying the help message and storing the values that the user enters.
```
"--image, --first-tag, --second-tag" -> the arguments
dest = "image" -> the name where the value of the image is going to be stored, this is how we are going to retreive the user input, it will be stored under [image]
--help -> a help section
```
The **parse_args()** function is useful for parsing the information introduced by the user.This function returns two values, an argument and an option.The option is the most important one, because it has the network interface's name and the new MAC address.
We can acces these by typing:
```
options.interface
options.tag1
options.tag2
```
I also made use of the subprocess module to execute system commands inside a python script.The documentation can be found here: https://docs.python.org/3/library/subprocess.html
I used the run() function within this module.

For comparing the two different tags of the particular image, I used the **container-diff** tool, the documentation can be found here:
https://github.com/GoogleContainerTools/container-diff




