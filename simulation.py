print("SIMULATION STARTED")

from elevator import Elevator

e = Elevator()

print("Start floor:", e.current_floor)

print(e.go_to_floor(3))
print("Current floor:", e.current_floor)

print(e.go_to_floor(7))
print("Current floor:", e.current_floor)

print(e.go_to_floor(999))  # invalid test


e = Elevator()

e.add_weight(600)

print(e.go_to_floor(5)) #expecting overload