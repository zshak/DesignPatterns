from app.AbstractClasses.creature import Creature
from app.Interfaces.characteristics import Energetic


class Predator(Creature, Energetic):
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
        stamina_calculation_strategy,
    ):
        super().__init__(
            move_strategy,
            evolve_strategy_teeth,
            evolve_strategy_legs,
            evolve_strategy_clas,
            evolve_strategy_wings,
            damage_point_calculation_strategy,
            is_killed_strategy,
            health_points_calculator_strategy,
        )
        self.position = 0
        self.stamina = 100
        self.wing_count = 0
        self.leg_count = 0

        self.claw_type = 0
        self.teeth_sharpness = 0

        self.power = 0
        self.health = 100
        self.stamina_calculation_strategy = stamina_calculation_strategy

    def has_stamina_left(self) -> bool:
        return self.stamina_calculation_strategy().calculate_stamina(self) >= 0

    # get propertiess
    def get_stamina(self) -> int:
        return self.stamina

    # set propertiess
    def set_stamina(self, stamina: int) -> None:
        self.stamina = stamina
