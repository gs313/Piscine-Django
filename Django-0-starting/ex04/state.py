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

    city = sys.argv[1]

    found_state = "Unknown state"

    for abbrev, cap in capital_cities.items():
        if cap == city:
            for full_name, code in states.items():
                if code == abbrev:
                    found_state = full_name
                    break

    print(found_state)


if __name__ == '__main__':
    main()
