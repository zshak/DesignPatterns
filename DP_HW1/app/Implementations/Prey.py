from app.AbstractClasses.creature import Creature


class Prey(Creature):
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
        initial_prey_position_strategy,
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
        self.position = initial_prey_position_strategy().calculate_init_pos()
        self.stamina = 100
        self.wing_count = 0
        self.leg_count = 0

        self.claw_type = 0
        self.teeth_sharpness = 0

        self.power = 0
        self.health = 100
