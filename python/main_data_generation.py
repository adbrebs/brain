__author__ = 'adeb'

import sys
import ConfigParser

from data_generation import Dataset

if __name__ == '__main__':
    if len(sys.argv) == 1:
        ini_file = "creation_training_data_1.ini"
    else:
        ini_file = str(sys.argv[1])

    # Load config
    config_ini = ConfigParser.ConfigParser()
    config_ini.read(ini_file)
    file_name = config_ini.get('generate_data', 'file_name')

    # Generate the dataset
    dc_training = Dataset()
    dc_training.generate(config_ini)
    dc_training.write(file_name)