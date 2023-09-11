import sys
import configparser
from common import copy_file
from data import data_pattern
from control import control_pattern
from ack import ack_pattern

config = configparser.ConfigParser()
config.read('config.ini')

dnb = config.get('Data', 'num_of_bits')
dnp = config.get('Data', 'num_of_ports')
dpn = config.get('Data', 'port_names')
cnb = config.get('Control', 'num_of_bits')
cnp = config.get('Control', 'num_of_ports')
cpn = config.get('Control', 'port_names')


if __name__ == "__main__":
    # Get the input file name and output file name from command line arguments
    input_file = "venv/include/common_pattern.txt"
    output_file = "output.txt"
    copy_file(input_file, output_file)
    data_pattern(dnb, dnp, dpn, output_file)
    control_pattern(cnb, cnp, cpn, output_file)
    ack_pattern(dnp, dpn, output_file)
