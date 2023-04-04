class Individual(object):

    def __init__(self):
        self.rank = None
        self.crowding_distance = 0
        self.domination_count = None # 被其他个体支配的数目
        self.dominated_solutions = None # 支配其他个体的解
        self.features = None
        self.objectives = None

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.features == other.features
        return False

    def dominates(self, other_individual):
        and_condition = True
        or_condition = False
        for first, second in zip(self.objectives, other_individual.objectives):
            and_condition = and_condition and first <= second
            or_condition = or_condition or first <= second
        return and_condition and or_condition

    def dominates_non(self, other_individual):
        for first, second in zip(self.objectives, other_individual.objectives):
            if first < second:
                return 1
        return 0
