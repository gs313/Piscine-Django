import sys
import json
import requests
import dewiki

def fetch_wikipedia_article():
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments. Please provide exactly one search term.")
        return

    search_term = sys.argv[1]
    api_url = "https://en.wikipedia.org/w/api.php"


    custom_headers = {
        "User-Agent": "scharuka_django/1.0 (Student Project)"
    }

    try:
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": search_term,
            "format": "json"
        }

        search_response = requests.get(url=api_url, params=search_params, headers=custom_headers)
        search_response.raise_for_status()
        search_data = search_response.json()

        if not search_data.get("query", {}).get("search"):
            print("Error: No information found for the given request.")
            return

        exact_pageid = search_data["query"]["search"][0]["pageid"]
        print(search_data)

        parse_params = {
            "action": "parse",
            "pageid": exact_pageid,
            "prop": "wikitext",
            "format": "json"
        }

        parse_response = requests.get(url=api_url, params=parse_params, headers=custom_headers)
        parse_response.raise_for_status()
        parse_data = parse_response.json()

        if "error" in parse_data:
            print(f"Error: {parse_data['error'].get('info', 'Information not found.')}")
            return

        raw_wikitext = parse_data["parse"]["wikitext"]["*"]
        clean_text = dewiki.from_string(raw_wikitext)

        filename = search_term.replace(" ", "_") + ".wiki"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(clean_text)

    except requests.exceptions.RequestException as e:
        print(f"Error: A network or server problem occurred -> {e}")
    except json.JSONDecodeError:
        print("Error: Failed to parse the Wikipedia API JSON response.")
    except Exception as e:
        print(f"Error: An unexpected issue occurred -> {e}")

if __name__ == '__main__':
    fetch_wikipedia_article()
