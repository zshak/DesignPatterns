from typing import Protocol

from app.Interfaces.characteristics import Movable


class IMoveStrategyFactory(Protocol):
    def get_move_strategy_instance(self, movable: Movable):
        pass
