class Intern:
    """A class representing an intern."""
    class Coffee:
        """A simple class representing a cup of coffee."""
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return Intern.Coffee()

if __name__ == '__main__':
    nameless_intern = Intern()
    mark = Intern("Mark")

    print(nameless_intern)
    print(mark)

    marks_coffee = mark.make_coffee()
    print(marks_coffee)

    try:
        nameless_intern.work()
    except Exception as e:
        print(f"Exception caught: {e}")
