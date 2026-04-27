class Elevator:
    def __init__(self, max_floor=10, weight_limit=500):
        self.current_floor = 1
        self.max_floor = max_floor
        self.weight_limit = weight_limit
        self.current_weight = 0

    def go_to_floor(self, floor):
        if floor < 1 or floor > self.max_floor:
            return "Invalid floor"

        if self.is_overloaded():
            return "Overload! Cannot move"

        self.current_floor = floor
        return f"Arrived at floor {floor}"

    def add_weight(self, weight):
        self.current_weight += weight

    def remove_weight(self, weight):
        self.current_weight -= weight

    def is_overloaded(self):
        return self.current_weight > self.weight_limit

