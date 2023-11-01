import string
from dataclasses import dataclass
from typing import List, Protocol

from app.AbstractClasses.creature import Creature
from app.Constants import Constants
from app.Implementations.Predator import Predator
from app.Implementations.Prey import Prey
from app.Implementations.strategyImplementations import (
    crawling_move_strategy,
    default_damage_point_calculation_strategy,
    default_evolve_strategy_clas,
    default_evolve_strategy_legs,
    default_evolve_strategy_teeth,
    default_evolve_strategy_wings,
    default_health_points_calculator_strategy,
    default_initial_prey_position_strategy,
    default_is_killed_strategy,
    default_stamina_calculation_strategy,
    defualt_fight_strategy,
)


class GameSimulator:
    def __init__(self, num_predator: int, num_prey: int, prey= None, predator = None):
        self.preys = None
        self.predators = None
        self.__init_characters(num_predator, num_prey)

        if prey is not None:
            self.preys = prey

        if predator is not None:
            self.predators = predator

    def simulate(self) -> None:
        # self.__init_characters(num_predator, num_prey)
        CreatureEvolverLogger(CreatureEvolver()).evolve(self.preys, self.predators)
        while not self.__game_over():
            self.__simulate_turn()
            self.__log_turn()
        pass

    def __log_turn(self):
        sorted_preys = sorted(self.preys, key=lambda x: x.get_health())
        if sorted_preys[-1].is_dead():
            print("Some R Rated Things Have Happened")
            return

        for ind, predator in enumerate(self.predators):
            if not predator.has_stamina_left() or predator.is_dead():
                self.predators.pop(ind)

        for ind, prey in enumerate(self.preys):
            if prey.is_dead():
                self.preys.pop(ind)

        if (len(self.predators) == 0 and len(self.preys) != 0) or all(
            obj.get_position() > Constants.POSITION_MAX for obj in self.preys
        ):
            print("Prey Ran Into Infinity")

    def __simulate_turn(self):
        for predator in self.predators:
            self.__move_character(predator)
        for prey in self.preys:
            self.__move_character(prey)

        self.__simulate_fight()

    def __simulate_fight(self):
        # ar minda axla davwero bevri characteris shemtxvevashi ra logika iqneboda
        # listebad gamaqvs rom shemdegshi daextendebadi iyos
        for predator in self.predators:
            for prey in self.preys:
                if predator.get_position() >= prey.position:
                    self.__simulate_fight_between_characters(predator, prey)

    def __simulate_fight_between_characters(
        self, predator: Creature, prey: Creature, fight_strategy=defualt_fight_strategy
    ) -> None:
        fight_strategy().simulate_fight(predator, prey)

    def __move_character(self, character: Creature):
        character.move()

    def __game_over(self):
        var1 = all(obj.get_health() > 0 for obj in self.predators)
        var2 = all(obj.get_health() > 0 for obj in self.preys)
        var3 = all(obj.has_stamina_left() for obj in self.predators)
        var4 = all(obj.get_position() <= Constants.POSITION_MAX for obj in self.preys)
        var5 = len(self.preys) != 0 and len(self.predators) != 0
        return not (var1 and var2 and var3 and var4 and var5)

    def __init_characters(self, num_predators: int, num_prey: int) -> None:
        self.predators = [
            Predator(
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
        ] * num_predators
        self.preys = [
            Prey(
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
        ] * num_prey


class ICreaturesEvolver(Protocol):
    def evolve(self, preys: List[Prey], predators: List[Predator]):
        pass


class CreatureEvolver(ICreaturesEvolver):
    def evolve(self, preys: List[Prey], predators: List[Predator]):
        for predator in predators:
            self.__evolve_ch(predator)
        for prey in preys:
            self.__evolve_ch(prey)

    def __evolve_ch(self, creature: Creature) -> None:
        creature.evolve_legs()
        creature.evolve_claws()
        creature.evolve_teeth()
        creature.evolve_wings()


@dataclass
class CreatureEvolverDecorator:
    creature_evolver: ICreaturesEvolver

    def evolve(self, preys: List[Prey], predators: List[Predator]):
        self.creature_evolver.evolve(preys, predators)


class CreatureEvolverLogger(CreatureEvolverDecorator):
    def evolve(self, preys: List[Prey], predators: List[Predator]):
        super().evolve(preys, predators)
        for prey in preys:
            self.__print_creature(prey, "prey")
        for prey in predators:
            self.__print_creature(prey, "predator")

    def __print_creature(self, creature: Creature, name: string):
        print(f"{name}: ")
        print(f"position: {creature.get_position()}")
        print(f"legs: {creature.get_legs()}")
        print(f"wings: {creature.get_wings()}")
        print(f"teeth: {creature.get_teeth_sharpness()}")
        print(f"claws: {creature.get_claws_size()}")
