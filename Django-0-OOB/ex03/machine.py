import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.served_drinks = 0
        self.is_broken = False

    class EmptyCup(HotBeverage):
        """A nested class representing a scam of a drink."""
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        """A nested exception with a predefined error message in its builder."""
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        """Repairs the machine and resets the counter."""
        self.is_broken = False
        self.served_drinks = 0
        print("\n--- 🔧 The mechanic fixed the coffee machine! ---\n")

    def serve(self, beverage_class):
        """Serves a hot drink or an empty cup, breaking after 10 uses."""
        if self.is_broken:
            raise CoffeeMachine.BrokenMachineException()

        self.served_drinks += 1
        if self.served_drinks >= 10:
            self.is_broken = True

        if random.choice([True, False]):
            return beverage_class()
        else:
            return CoffeeMachine.EmptyCup()


def test_machine():
    """Test function to keep the global scope clean."""
    machine = CoffeeMachine()
    menu = [Coffee, Tea, Chocolate, Cappuccino]

    print("--- ☕ Starting the Coffee Machine ---\n")

    # FIRST RUN
    try:
        for i in range(12):
            drink_choice = random.choice(menu)
            drink_served = machine.serve(drink_choice)
            print(f"Drink {i + 1}: Served a '{drink_served.name}'.")
    except CoffeeMachine.BrokenMachineException as e:
        print(f" MACHINE BROKE on attempt {i + 1} Error: {e}")

    # REPAIR THE MACHINE
    machine.repair()

    # SECOND RUN
    try:
        for i in range(12):
            drink_choice = random.choice(menu)
            drink_served = machine.serve(drink_choice)
            print(f"Drink {i + 1}: Served a '{drink_served.name}'.")
    except CoffeeMachine.BrokenMachineException as e:
        print(f" MACHINE BROKE AGAIN on attempt {i + 1} Error: {e}")


if __name__ == '__main__':
    try:
        test_machine()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
