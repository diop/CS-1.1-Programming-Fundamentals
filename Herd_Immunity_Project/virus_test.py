from virus import Virus

def test_virus_instantiation():
    virus = Virus('HIV', 0.8, 0.3)
    assert virus.name == 'HIV'
    assert virus.mortality_rate == 0.8
    assert virus.repro_rate == 0.3
