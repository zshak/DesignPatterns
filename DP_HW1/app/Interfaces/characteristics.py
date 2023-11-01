from typing import Protocol


class Movable(Protocol):
    def move(self) -> None:
        pass

    # get properties
    def get_position(self) -> int:
        pass

    def get_stamina(self) -> int:
        pass

    def get_legs(self) -> int:
        pass

    def get_wings(self) -> int:
        pass

    # set properties
    def set_position(self, position: int) -> None:
        pass

    def set_stamina(self, stamina: int) -> None:
        pass

    def set_legs(self, legs: int) -> None:
        pass

    def set_wings(self, wings: int) -> None:
        pass


class Evolvable(Protocol):
    def evolve_teeth(self):
        pass

    def evolve_legs(self) -> None:
        pass

    def evolve_claws(self) -> None:
        pass

    def evolve_wings(self) -> None:
        pass

    # get properties

    def get_legs(self) -> int:
        pass

    def get_claws_size(self) -> int:
        pass

    def get_teeth_sharpness(self) -> int:
        pass

    def get_wings(self) -> int:
        pass

    # set properties
    def set_claws_size(self, claws: int) -> None:
        pass

    def set_teeth_sharpness(self, teeth_sharpness: int) -> None:
        pass

    def set_legs(self, legs: int) -> None:
        pass

    def set_wings(self, wings: int) -> None:
        pass


class Fightable(Protocol):
    def attack(self, opponent: "Fightable") -> None:
        pass

    def get_hit(self, health_points) -> None:
        pass

    # get properties
    def get_power(self) -> int:
        pass

    def get_health(self) -> int:
        pass

    def get_teeth_sharpness(self) -> int:
        pass

    def get_claws_size(self) -> int:
        pass

    # set properties
    def set_power(self, power: int) -> None:
        pass

    def set_health(self, health: int) -> None:
        pass

    def set_teeth_sharpness(self, teeth_sharpness: int) -> None:
        pass

    def set_claws_size(self, claws: int) -> None:
        pass


class Killable(Protocol):
    def is_dead(self) -> bool:
        pass

    # get properties
    def get_health(self) -> int:
        pass

    # set properties

    def set_health(self, health: int) -> None:
        pass


class Energetic(Protocol):
    def has_stamina_left(self) -> bool:
        pass

    # get propertiess
    def get_stamina(self) -> int:
        pass

    # set propertiess
    def set_stamina(self, stamina: int) -> None:
        pass
