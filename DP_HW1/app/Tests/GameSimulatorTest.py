import random

import pytest
import typing
from app.AbstractClasses.creature import Creature
from app.Constants import Constants
from app.Implementations.Predator import Predator
from app.Implementations.Prey import Prey
from app.Implementations.strategyImplementations import crawling_move_strategy, default_evolve_strategy_teeth, \
    default_evolve_strategy_legs, default_evolve_strategy_clas, default_evolve_strategy_wings, \
    default_damage_point_calculation_strategy, default_is_killed_strategy, default_health_points_calculator_strategy, \
    default_stamina_calculation_strategy, default_initial_prey_position_strategy
from app.Tests.CreatureTest import CreatureInit
from app.game_symulator import GameSimulator


def test__simulate_fight() -> None:
    game = GameSimulator(num_predator=1, num_prey=1)
    game.preys = [CreatureInit().create_creature(position=1, power = 1,health=2, stamina=100, teeth=1, claws=1, creature_name="prey")]

    game.predators = [CreatureInit().create_creature(position=1, power=3, teeth=1,claws=1, health = 3, stamina = 100, creature_name="predator")]
    game.simulate()
    assert game.preys[0].get_health()<=0

def test__simulate_escape() -> None:
    game = GameSimulator(num_predator=1, num_prey=1)
    game.preys = [CreatureInit().create_creature(position=random.randint(2,100), power = 1,health=2, stamina=100, teeth=1, claws=1, creature_name="prey")]

    game.predators = [CreatureInit().create_creature(position=1, power=3, teeth=1,claws=1, health = 3, stamina = 100, creature_name="predator")]
    game.simulate()
    assert game.preys[0].get_position()>=Constants.POSITION_MAX

def test__simulate_out_of_stamina() -> None:
    game = GameSimulator(num_predator=1, num_prey=1)
    game.preys = [CreatureInit().create_creature(position=random.randint(26,50), legs= 1, power = 1,health=2, stamina=100, teeth=1, claws=1, creature_name="prey")]

    game.predators = [CreatureInit().create_creature(position=random.randint(2,25), legs= 1, power=3, teeth=1,claws=1, health = 3, stamina = random.randint(1,5), creature_name="predator")]
    game.simulate()
    assert len(game.predators) == 0