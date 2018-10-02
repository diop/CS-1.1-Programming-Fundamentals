from logger import Logger
from person import Person
from virus import Virus
from simulation import Simulation
import pytest
import io
import sys
import os.path

# Test Logger Class

def test_create_file():
    # Test the creation of the text file on disk.
    file_name = 'log-test.txt'
    # assert not os.path.isfile(file_name)
    logger = Logger(file_name)
    assert os.path.isfile(file_name)

    # logger.write_metadata(logger.pop_size, logger.vacc_percentage, logger.virus_name, logger.mortality_rate, logger.basic_repro_num)


def test_write_metadata():
    pass

def test_log_interaction():
    pass

def test_log_infection_survival():
    pass

def test_log_time_step():
    pass
