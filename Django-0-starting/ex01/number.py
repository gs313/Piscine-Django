def read_numbers(filename="numbers.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
             content = f.read()
        if not content.strip():
             print(f"Warning: {filename} is empty.")
             return
        raw_values = content.split(',')

        for val in raw_values:
            clean_val = val.strip()
            if not clean_val:
                continue

            try:
                number = float(clean_val)
                print(number)
            except ValueError:
                print(f"Skipping invalid data: '{clean_val}' is not a number.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
	read_numbers()
