import sys

def all_in():
    if len(sys.argv) != 2:
        return

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

    lower_states = {key.lower(): key for key in states.keys()}

    lower_cities = {value.lower(): value for value in capital_cities.values()}

    abbrev_to_state = {value: key for key, value in states.items()}

    city_to_abbrev = {value: key for key, value in capital_cities.items()}

    arg_str = sys.argv[1]

    expressions = arg_str.split(',')

    for expr in expressions:
        cleaned_expr = expr.strip()

        if not cleaned_expr:
            continue

        search_term = ' '.join(cleaned_expr.split()).lower()

        if search_term in lower_states:
            correct_state_name = lower_states[search_term]
            abbrev = states[correct_state_name]
            capital = capital_cities[abbrev]
            print(f"{capital} is the capital of {correct_state_name}")

        elif search_term in lower_cities:
            correct_city_name = lower_cities[search_term]
            abbrev = city_to_abbrev[correct_city_name]
            correct_state_name = abbrev_to_state[abbrev]
            print(f"{correct_city_name} is the capital of {correct_state_name}")

        else:
            print(f"{cleaned_expr} is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()
