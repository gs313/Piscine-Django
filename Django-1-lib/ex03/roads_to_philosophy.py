import sys
import requests
from bs4 import BeautifulSoup

def find_roads_to_philosophy():
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments. Please provide one search term.")
        return

    search_term = sys.argv[1]
    url = f"https://en.wikipedia.org/wiki/{search_term.replace(' ', '_')}"

    visited_pages = []
    headers = {
        "User-Agent": "42School_Philosophy_Bot/1.1 (Student Project)"
    }

    try:
        while True:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # 1. Get the current page title
            title_tag = soup.find(id="firstHeading")
            if not title_tag:
                print("Error: Could not find page title.")
                return

            current_title = title_tag.text

            # Check for infinite loops
            if current_title in visited_pages:
                print("It leads to an infinite loop !")
                return

            visited_pages.append(current_title)
            print(current_title)

            # Check for victory
            if current_title == "Philosophy":
                print(f"{len(visited_pages)} roads from {search_term} to philosophy !")
                return

            # 2. Find the content block
            content_div = soup.find(id="mw-content-text")
            parser_output = content_div.find(class_="mw-parser-output") or content_div

            first_valid_link = None

            # Wikipedia Namespaces that do NOT lead to standard articles
            invalid_namespaces = [
                '/wiki/Help:', '/wiki/File:', '/wiki/Wikipedia:',
                '/wiki/Category:', '/wiki/Special:', '/wiki/Talk:',
                '/wiki/Portal:', '/wiki/Template:', '/wiki/Draft:'
            ]

            # Iterate through all paragraphs in the content body
            for p in parser_output.find_all('p'):
                # Skip paragraphs that are trapped inside tables or side infoboxes
                if p.find_parent('table') or p.find_parent(class_='infobox'):
                    continue

                for link in p.find_all('a'):
                    href = link.get('href', '')

                    # - Must be an internal wiki link
                    # - Must not be a citation (starts with #)
                    if href.startswith('/wiki/') and not href.startswith('#'):

                        # - Must not be in the blacklist of system/help namespaces
                        is_valid_article = True
                        for ns in invalid_namespaces:
                            if href.startswith(ns):
                                is_valid_article = False
                                break

                        if is_valid_article:
                            first_valid_link = href
                            break # Found the first valid link in this paragraph!

                if first_valid_link:
                    break # Found the first valid link overall!

            # 3. Dead end check
            if not first_valid_link:
                print("It leads to a dead end !")
                return

            # Set the URL for the next hop
            url = f"https://en.wikipedia.org{first_valid_link}"

    except requests.exceptions.RequestException as e:
        print(f"Error: A network or server problem occurred -> {e}")
    except Exception as e:
        print(f"Error: An unexpected issue occurred -> {e}")

if __name__ == '__main__':
    find_roads_to_philosophy()
