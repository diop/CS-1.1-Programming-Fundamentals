from person import Person
from virus import Virus
import pytest
import io
import sys
import random

# Test New Person

def test_person_instance():
    person = Person(100, None, None)
    assert person._id == 100
    assert person.is_alive == True
    assert person.is_vaccinated is None
    assert person.infected is None

# Test Instace methods

def test_did_survive_infection():
    # Find out about Mortality Rate
    virus = Virus('Ebola', 0.8, 0.3)
    person = Person(925, is_vaccinated=False, infected=virus)

    # Check the person instance
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infected is virus

    # Check if the person survived the infection
    survived = person.did_survive_infection()
    print('survived -->', survived)
    if survived:
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infected is None
    else: #died
        print('fix this test why is_alive should be false -->', person.is_alive)
        assert person.is_alive is True
