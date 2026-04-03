import sys

def main():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return

    state = sys.argv[1]

    if state in states:
        code = states[state]
        print(capital_cities[code])
    else:
        print("Unknown state")


if __name__ == '__main__':
    main()
