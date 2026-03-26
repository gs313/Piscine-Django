def get_people():
    """Returns the list of couples as provided."""
    return [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939'),
        ('Amy', '1939')
    ]

def build_year_dict(data):
    result = {}
    for name, year in data:
        #set each year to pair with a list in case there are many name in the same year
        result.setdefault(year, []).append(name)
    return result

def display_dict(data_dict):
    for year, names in data_dict.items():
        print(f"{year} : {' '.join(names)}")

def main():
    data = get_people()
    guitar_dict = build_year_dict(data)
    display_dict(guitar_dict)

if __name__ == '__main__':
    main()
