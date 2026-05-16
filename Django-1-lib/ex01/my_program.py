import sys

sys.path.insert(0, './local_lib')

try:
    from path import Path
except ImportError:
    print("Error: Could not import 'path' from local_lib.")
    sys.exit(1)

def file_operations():
    folder = Path('test_directory')
    file_path = folder / 'test_file.txt'

    try:
        folder.mkdir_p()

        file_path.write_text('Hello, 42! The path library is working perfectly.')

        content = file_path.read_text()

        print(content)

    except Exception as e:
        print(f"An error occurred during file operations: {e}")

if __name__ == '__main__':
    file_operations()
