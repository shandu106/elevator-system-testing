from elevator import Elevator

def test_go_to_valid_floor():
    elevator = Elevator()

    result = elevator.go_to_floor(3)

    assert result == "Arrived at floor 3"
    assert elevator.current_floor == 3

def test_invalid_floor():
    elevator = Elevator()

    result = elevator.go_to_floor(999)

    assert result == "Invalid floor"
    assert elevator.current_floor == 1


def test_overload_prevents_movement():
    elevator = Elevator()

    elevator.add_weight(600)

    result = elevator.go_to_floor(5)

    assert result == "Overload! Cannot move"
    assert elevator.current_floor == 1
