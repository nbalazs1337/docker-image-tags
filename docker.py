import subprocess
import optparse
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--image", dest="image", help="Docker Image name")
    parser.add_option("--first-tag", dest="tag1", help="First Tag")
    parser.add_option("--second-tag", dest="tag2", help="Second Tag")
    # options will contain the alpin and 3.15 etc
    # arguments will contain --image --first-tag and --second-tag
    (options, arguments) = parser.parse_args()
    # storing the user input values in two variables
    if not options.image:
        #code to handle error
        parser.error("[!!!] Please specify a Docker Image, use --help for info")
    elif not options.tag1:
        parser.error("[!!!] Please specify the first tag, use --help for info")
    elif not options.tag2:
        parser.error("[!!!] Please specify the second tag, use --help for info")
    return options

def get_differences_between_tags(image, tag1, tag2):
    subprocess.run("container-diff " + " diff " + " --type=file " + image+":"+tag1 +" "+ image+":"+tag2, shell=True)



options = get_arguments()
get_differences_between_tags(options.image, options.tag1, options.tag2)
