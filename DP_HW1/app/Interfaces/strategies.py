from typing import Protocol

from app.AbstractClasses.creature import Creature
from app.Interfaces.characteristics import (
    Energetic,
    Evolvable,
    Fightable,
    Killable,
    Movable,
)


class move_strategy(Protocol):
    def move(self, movable: Movable) -> None:
        pass


class evolve_strategy_teeth(Protocol):
    def evolve_teeth(self, evolvable: Evolvable) -> None:
        pass


class evolve_strategy_legs(Protocol):
    def evolve_legs(self, evolvable: Evolvable) -> None:
        pass


class evolve_strategy_clas(Protocol):
    def evolve_claws(self, evolvable: Evolvable) -> None:
        pass


class evolve_strategy_wings(Protocol):
    def evolve_wings(self, evolvable: Evolvable) -> None:
        pass


class damage_point_calculation_strategy(Protocol):
    def calculate_damage(self, fightable: Fightable) -> int:
        pass


class is_killed_strategy(Protocol):
    def is_killed(self, killable: Killable) -> bool:
        pass


class health_points_calculator_strategy(Protocol):
    def calculate_health(self, killable: Killable) -> int:
        pass


class stamina_calculation_strategy(Protocol):
    def calculate_stamina(self, energetic: Energetic) -> int:
        pass


class initial_prey_position_strategy(Protocol):
    def calculate_init_pos(self) -> int:
        pass


class fight_strategy(Protocol):
    def simulate_fight(self, creature1: Creature, creature2: Creature) -> None:
        pass
