import random

from app.AbstractClasses.creature import Creature
from app.Constants import Constants
from app.Interfaces.characteristics import (
    Energetic,
    Evolvable,
    Fightable,
    Killable,
    Movable,
)
from app.Interfaces.strategies import (
    damage_point_calculation_strategy,
    evolve_strategy_clas,
    evolve_strategy_legs,
    evolve_strategy_teeth,
    evolve_strategy_wings,
    fight_strategy,
    health_points_calculator_strategy,
    initial_prey_position_strategy,
    is_killed_strategy,
    move_strategy,
    stamina_calculation_strategy,
)


class crawling_move_strategy(move_strategy):
    def move(self, movable: Movable) -> None:
        stamina = movable.get_stamina()
        position = movable.get_position()
        movable.set_stamina(stamina - 1)
        movable.set_position(position + 1)


class hopping_move_strategy(move_strategy):
    def move(self, movable: Movable) -> None:
        stamina = movable.get_stamina()
        position = movable.get_position()
        movable.set_stamina(stamina - 2)
        movable.set_position(position + 3)


class walking_move_strategy(move_strategy):
    def move(self, movable: Movable) -> None:
        stamina = movable.get_stamina()
        position = movable.get_position()
        movable.set_stamina(stamina - 2)
        movable.set_position(position + 4)


class running_move_strategy(move_strategy):
    def move(self, movable: Movable) -> None:
        stamina = movable.get_stamina()
        position = movable.get_position()
        movable.set_stamina(stamina - 4)
        movable.set_position(position + 6)


class flying_move_strategy(move_strategy):
    def move(self, movable: Movable) -> None:
        stamina = movable.get_stamina()
        position = movable.get_position()
        movable.set_stamina(stamina - 4)
        movable.set_position(position + 8)


class default_evolve_strategy_teeth(evolve_strategy_teeth):
    def evolve_teeth(self, evolvable: Evolvable) -> None:
        evolved_teeth = random.randint(Constants.TEETH_MIN, Constants.TEETH_MAX)
        evolvable.set_teeth_sharpness(evolved_teeth)


class default_evolve_strategy_legs(evolve_strategy_legs):
    def evolve_legs(self, evolvable: Evolvable) -> None:
        evolved_legs = random.randint(Constants.LEG_MIN, Constants.LEG_MAX)
        evolvable.set_legs(evolved_legs)


class default_evolve_strategy_wings(evolve_strategy_wings):
    def evolve_wings(self, evolvable: Evolvable) -> None:
        evolved_wings = random.randint(Constants.WING_MIN, Constants.WING_MAX)
        evolvable.set_wings(evolved_wings)


class default_evolve_strategy_clas(evolve_strategy_clas):
    def evolve_claws(self, evolvable: Evolvable) -> None:
        evolved_claws = random.randint(Constants.CLAW_MIN, Constants.CLAW_MAX)
        evolvable.set_claws_size(evolved_claws)


class default_damage_point_calculation_strategy(damage_point_calculation_strategy):
    def calculate_damage(self, fightable: Fightable) -> int:
        power = fightable.get_power()
        teeth = fightable.get_teeth_sharpness()
        claw = fightable.get_claws_size()
        return (power + teeth * 3) * (claw + 1)


class default_is_killed_strategy(is_killed_strategy):
    def is_killed(self, killable: Killable) -> bool:
        return killable.get_health() <= 0


class default_health_points_calculator_strategy(health_points_calculator_strategy):
    def calculate_health(self, killable: Killable) -> int:
        return killable.get_health()


class default_stamina_calculation_strategy(stamina_calculation_strategy):
    def calculate_stamina(self, energetic: Energetic) -> int:
        return energetic.get_stamina()


class default_initial_prey_position_strategy(initial_prey_position_strategy):
    def calculate_init_pos(self) -> int:
        return random.randint(Constants.POSITION_MIN, Constants.POSITION_MAX)


class defualt_fight_strategy(fight_strategy):
    def simulate_fight(self, creature1: Creature, creature2: Creature) -> None:
        while creature1.get_health() > 0 and creature2.get_health() > 0:
            creature1.attack(creature2)
            creature2.attack(creature1)
