from abc import ABC

from app.Interfaces.characteristics import Evolvable, Fightable, Killable, Movable


class Creature(Fightable, Evolvable, Movable, Killable, ABC):
    position: int
    stamina: int
    wing_count: int
    leg_count: int

    claw_type: int
    teeth_sharpness: int

    power: int
    health: int

    # strategies

    def __init__(
        self,
        move_strategy,
        evolve_strategy_teeth,
        evolve_strategy_legs,
        evolve_strategy_clas,
        evolve_strategy_wings,
        damage_point_calculation_strategy,
        is_killed_strategy,
        health_points_calculator_strategy,
    ):
        self.move_strategy = move_strategy
        self.evolve_strategy_teeth = evolve_strategy_teeth
        self.evolve_strategy_legs = evolve_strategy_legs
        self.evolve_strategy_clas = evolve_strategy_clas
        self.evolve_strategy_wings = evolve_strategy_wings
        self.damage_point_calculation_strategy = damage_point_calculation_strategy
        self.is_killed_strategy = is_killed_strategy
        self.health_points_calculator_strategy = health_points_calculator_strategy

    def move(self) -> None:
        from app.Implementations.Factory.MoveStrategyFactory import MoveStrategyFactory

        a = MoveStrategyFactory().get_move_strategy_instance(self)
        a.move(self)

    def evolve_teeth(self):
        self.evolve_strategy_teeth().evolve_teeth(self)

    def evolve_legs(self) -> None:
        self.evolve_strategy_legs().evolve_legs(self)

    def evolve_claws(self) -> None:
        self.evolve_strategy_clas().evolve_claws(self)

    def evolve_wings(self) -> None:
        self.evolve_strategy_wings().evolve_wings(self)

    def attack(self, opponent: "Fightable") -> None:
        attack_damage = self.damage_point_calculation_strategy().calculate_damage(self)
        opponent.get_hit(attack_damage)
        pass

    def get_hit(self, health_points: int) -> None:
        self.set_health(self.health - health_points)
        pass

    def is_dead(self) -> bool:
        return self.get_health() <= 0

    # get properties
    def get_health(self) -> int:
        return self.health

    # get properties
    def get_power(self) -> int:
        return self.power

    def get_teeth_sharpness(self) -> int:
        return self.teeth_sharpness

    def get_legs(self) -> int:
        return self.leg_count

    def get_claws_size(self) -> int:
        return self.claw_type

    def get_position(self) -> int:
        return self.position

    def get_wings(self) -> int:
        return self.wing_count

    def get_stamina(self) -> int:
        return self.stamina

    # set properties
    def set_position(self, position: int) -> None:
        self.position = position

    def set_stamina(self, stamina: int) -> None:
        self.stamina = stamina

    def set_legs(self, legs: int) -> None:
        self.leg_count = legs

    def set_wings(self, wings: int) -> None:
        self.wing_count = wings

    def set_claws_size(self, claws: int) -> None:
        self.claw_type = claws

    def set_teeth_sharpness(self, teeth_sharpness: int) -> None:
        self.teeth_sharpness = teeth_sharpness

    def set_power(self, power: int) -> None:
        self.power = power

    def set_health(self, health: int) -> None:
        self.health = health
