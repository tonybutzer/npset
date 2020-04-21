import os
import json

class Breed():
    """ Breed holds the config file for the applications
        such as the cogbucket """
    def __init__(self):
        """ set up instance variables """
        home_folder = '.'
        config_file = home_folder + '/' + "config_cogxfer.json"
        if os.path.exists(config_file):
            # read json file
            with open(config_file) as data_file:
                data = json.load(data_file)
            self.in_bucket = data['in_bucket']
            self.out_bucket = data['out_bucket']
            self.in_prefix = data['in_prefix']
        else:
            print("No config config_cogxfer.json file -- Please -- create one as documented in the README.md!")
            exit(False)
