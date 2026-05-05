import sys
import os
import re

def load_settings():
    """Reads settings.py without using an import statement."""
    settings_dict = {}
    if not os.path.exists("settings.py"):
        raise FileNotFoundError("settings.py does not exist in the current directory.")

    with open("settings.py", "r") as f:
        exec(f.read(), globals(), settings_dict)

    return settings_dict

def render_template(template_path):
    """Processes the template and writes the HTML output."""
    if not template_path.endswith('.template'):
        raise ValueError("Wrong file extension. Expected a .template file.")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"The file '{template_path}' does not exist.")

    settings_dict = load_settings()
    with open(template_path, "r") as f:
        template_content = f.read()

    try:
        html_content = template_content.format(**settings_dict)
    except KeyError as e:
        raise KeyError(f"Missing setting for template variable: {e}")
    except ValueError as e:
        raise ValueError(f"Template formatting error (check your curly braces): {e}")

    # Generate output filename and write
    output_file = template_path.replace('.template', '.html')
    with open(output_file, "w") as f:
        f.write(html_content)

def main():
    # Check argument count
    if len(sys.argv) != 2:
        raise ValueError("Wrong number of arguments. Usage: python3 render.py <file.template>")

    template_path = sys.argv[1]
    render_template(template_path)

if __name__ == '__main__':
    # Catch ALL exceptions to satisfy the strict error handling requirement
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
