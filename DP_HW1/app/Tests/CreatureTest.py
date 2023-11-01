import random
from app.Constants import Constants
from app.Implementations.Predator import Predator
from app.Implementations.Prey import Prey
from app.Implementations.strategyImplementations import crawling_move_strategy, default_evolve_strategy_teeth, \
    default_evolve_strategy_legs, default_evolve_strategy_clas, default_evolve_strategy_wings, \
    default_damage_point_calculation_strategy, default_is_killed_strategy, default_health_points_calculator_strategy, \
    default_stamina_calculation_strategy, default_initial_prey_position_strategy


class CreatureInit:
    def create_creature(self, teeth=None, legs=None, claws=None, wings=None, stamina=None,
                        health=None, power=None, position=None, creature_name="prey"):
        c = None
        if creature_name == "predator":
            c = Predator(
                crawling_move_strategy,
                default_evolve_strategy_teeth,
                default_evolve_strategy_legs,
                default_evolve_strategy_clas,
                default_evolve_strategy_wings,
                default_damage_point_calculation_strategy,
                default_is_killed_strategy,
                default_health_points_calculator_strategy,
                default_stamina_calculation_strategy,
            )
        else:
            c = Prey(
                crawling_move_strategy,
                default_evolve_strategy_teeth,
                default_evolve_strategy_legs,
                default_evolve_strategy_clas,
                default_evolve_strategy_wings,
                default_damage_point_calculation_strategy,
                default_is_killed_strategy,
                default_health_points_calculator_strategy,
                default_initial_prey_position_strategy,
            )
        c.set_legs(legs)
        c.set_teeth_sharpness(teeth)
        c.set_stamina(stamina)
        c.set_wings(wings)
        c.set_health(health)
        c.set_power(power)
        c.set_position(position)
        c.set_claws_size(claws)
        return c


def test_move_crawl() -> None:
    for _ in range(100):
        position = random.randint(0, 100)
        st = stamina= random.randint(Constants.STAMINA_NEEDED_CRAWL + 1, Constants.STAMINA_NEEDED_HOPPING)
        test_creature = CreatureInit().create_creature(position = position,
                                                       stamina= st,
                                                       legs=0,
                                                       wings=0)
        test_creature.move()
        assert position + 1 == test_creature.get_position()
        assert stamina - 1 == test_creature.get_stamina()

def test_move_hop() -> None:
    for _ in range(100):
        position = random.randint(0, 100)
        st = stamina = random.randint(Constants.STAMINA_NEEDED_HOPPING + 1, Constants.STAMINA_NEEDED_WALKING)
        test_creature = CreatureInit().create_creature(position=position,
                                                       stamina=st,
                                                       legs=1,
                                                       wings=0)
        test_creature.move()
        assert position + 3 == test_creature.get_position()
        assert stamina - 2 == test_creature.get_stamina()

def test_move_walk() -> None:
    for _ in range(100):
        position = random.randint(0, 100)
        st = stamina = random.randint(Constants.STAMINA_NEEDED_WALKING + 1, Constants.STAMINA_NEEDED_RUNNING)
        test_creature = CreatureInit().create_creature(position=position,
                                                       stamina=st,
                                                       legs=2,
                                                       wings=0)
        test_creature.move()
        assert position + 4 == test_creature.get_position()
        assert stamina - 2 == test_creature.get_stamina()

def test_move_run() -> None:
    for _ in range(100):
        position = random.randint(0, 100)
        st = stamina = random.randint(Constants.STAMINA_NEEDED_RUNNING + 1, Constants.STAMINA_NEEDED_FLYING)
        test_creature = CreatureInit().create_creature(position=position,
                                                       stamina=st,
                                                       legs=2,
                                                       wings=0)
        test_creature.move()
        assert position + 6 == test_creature.get_position()
        assert stamina - 4 == test_creature.get_stamina()

def test_move_fly() -> None:
    for _ in range(100):
        position = random.randint(0, 100)
        st = stamina = random.randint(Constants.STAMINA_NEEDED_FLYING + 1, Constants.STAMINA_NEEDED_FLYING + 100)
        test_creature = CreatureInit().create_creature(position=position,
                                                       stamina=st,
                                                       legs=2,
                                                       wings=2)
        test_creature.move()
        assert position + 8 == test_creature.get_position()
        assert stamina - 4 == test_creature.get_stamina()

def test_evolve_teeth() -> None:
    for _ in range(100):
        test_creature = CreatureInit().create_creature(teeth=0)
        test_creature.evolve_teeth()
        new_teeth = test_creature.get_teeth_sharpness()
        assert Constants.TEETH_MIN <= new_teeth <= Constants.TEETH_MAX


def test_evolve_legs() -> None:
    for _ in range(100):
        test_creature = CreatureInit().create_creature(legs=0)
        test_creature.evolve_legs()
        new_legs = test_creature.get_legs()
        assert Constants.LEG_MIN <= new_legs <= Constants.LEG_MAX


def test_evolve_claws() -> None:
    for _ in range(100):
        test_creature = CreatureInit().create_creature(claws=0)
        test_creature.evolve_claws()
        new_claws = test_creature.get_claws_size()
        assert Constants.CLAW_MIN <= new_claws <= Constants.CLAW_MAX


def test_evolve_wings() -> None:
    for _ in range(100):
        test_creature = CreatureInit().create_creature(wings=0)
        test_creature.evolve_wings()
        new_wings = test_creature.get_wings()
        assert Constants.WING_MIN <= new_wings <= Constants.WING_MAX


def test_attack() -> None:
    test_creature_1 = CreatureInit().create_creature(
        power=1,
        claws=1,
        teeth=1,
    )

    test_creature_2 = CreatureInit().create_creature(
        power=1,
        claws=2,
        teeth=1,
    )

    test_creature_3 = CreatureInit().create_creature(
        power=1,
        claws=3,
        teeth=1,
    )

    test_creature_4 = CreatureInit().create_creature(
        power=1,
        claws=1,
        teeth=2,
    )

    test_creature_5 = CreatureInit().create_creature(
        power=1,
        claws=1,
        teeth=3,
    )

    test_creature_6 = CreatureInit().create_creature(
        power=1,
        claws=2,
        teeth=2,
    )

    test_creature_7 = CreatureInit().create_creature(
        power=1,
        claws=2,
        teeth=3,
    )

    test_creature_8 = CreatureInit().create_creature(
        power=1,
        claws=3,
        teeth=3,
    )

    test_creature_victim = CreatureInit().create_creature(
        health=100
    )

    test_creature_1.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 92

    test_creature_victim.set_health(100)
    test_creature_2.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 88

    test_creature_victim.set_health(100)
    test_creature_3.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 84

    test_creature_victim.set_health(100)
    test_creature_4.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 86

    test_creature_victim.set_health(100)
    test_creature_5.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 80

    test_creature_victim.set_health(100)
    test_creature_6.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 79

    test_creature_victim.set_health(100)
    test_creature_7.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 70

    test_creature_victim.set_health(100)
    test_creature_8.attack(test_creature_victim)
    assert test_creature_victim.get_health() == 60

def test_get_hit() -> None:
    for i in range(100):
        damage = random.randint(0,50)
        test_creature_victim = CreatureInit().create_creature(
            health=100
        )
        test_creature_victim.get_hit(damage)
        assert test_creature_victim.get_health() == 100 - damage


def test_is_dead() -> None:
    for i in range(1000):
        test_creature_1 = CreatureInit().create_creature(
            health=random.randint(1, 1000)
        )
        assert test_creature_1.is_dead() is False

        test_creature_2 = CreatureInit().create_creature(
            health=random.randint(-1000, 0)
        )
        assert test_creature_2.is_dead() is True
