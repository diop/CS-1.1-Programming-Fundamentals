from person import Person
import pytest
import io
import sys
import random

# Test New Person

def test_person_instance():
    new_person = Person(100, False, False)
    assert new_person._id == 100
    assert new_person.is_alive
    assert not new_person.is_vaccinated
    assert not new_person.infected

# Test Instace methods

def test_did_survive_infection():
    # Find out about Mortality Rate
    mortality_rate = 0
    pass
