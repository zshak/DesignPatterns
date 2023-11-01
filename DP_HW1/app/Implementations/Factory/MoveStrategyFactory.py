from app.Constants import Constants
from app.Implementations.strategyImplementations import (
    crawling_move_strategy,
    flying_move_strategy,
    hopping_move_strategy,
    running_move_strategy,
    walking_move_strategy,
)
from app.Interfaces.characteristics import Movable
from app.Interfaces.Factory.IMoveStrategyFactory import IMoveStrategyFactory


class MoveStrategyFactory(IMoveStrategyFactory):
    def get_move_strategy_instance(self, movable: Movable):
        stamina = movable.get_stamina()
        legs = movable.get_legs()
        wings = movable.get_wings()

        if (
            stamina > Constants.STAMINA_NEEDED_FLYING
            and wings >= Constants.WINGS_NEEDED_FLY
        ):
            return flying_move_strategy()

        if (
            stamina > Constants.STAMINA_NEEDED_RUNNING
            and legs >= Constants.LEGS_NEEDED_RUN
        ):
            return running_move_strategy()

        if (
            stamina > Constants.STAMINA_NEEDED_WALKING
            and legs >= Constants.LEGS_NEEDED_WALK
        ):
            return walking_move_strategy()

        if (
            stamina > Constants.STAMINA_NEEDED_HOPPING
            and legs >= Constants.LEGS_NEEDED_HOP
        ):
            return hopping_move_strategy()

        if (
            stamina >= Constants.STAMINA_NEEDED_CRAWL
            and legs >= Constants.LEGS_NEEDED_CRAWL
        ):
            return crawling_move_strategy()
