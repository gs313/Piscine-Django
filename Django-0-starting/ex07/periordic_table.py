import sys

def parse_line(line):
    if not line.strip():
        return None

    name, attributes_str = line.strip().split(' = ')
    attributes_list = attributes_str.split(', ')

    element_data = {'name': name}
    for attr in attributes_list:
        key, value = attr.split(':')
        element_data[key.strip()] = value.strip()

    element_data['position'] = int(element_data['position'])
    return element_data

def generate_periodic_table():
    elements = []

    with open('periodic_table.txt', 'r') as file:
        for line in file:
            parsed_data = parse_line(line)
            if parsed_data:
                elements.append(parsed_data)

    html_content = [
        "<!DOCTYPE html>",
        "<html lang=\"en\">",
        "<head>",
        "  <meta charset=\"UTF-8\">",
        "  <title>Periodic Table of the Elements</title>",
        "  <style>",
        "    body { background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; margin: 0; }",
        "    h3 { color: #bb86fc; letter-spacing: 2px; text-align: center; }",
        "    /* Added a scrollable container wrapper */",
        "    .table-container { max-width: 100%; overflow-x: auto; padding: 10px 0; }",
        "    table { border-collapse: separate; border-spacing: 6px; margin: 0 auto; }",
        "    .element-box { background-color: #1e1e1e; border: 1px solid #333; border-radius: 8px; padding: 10px; width: 110px; height: 130px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); transition: all 0.2s ease-in-out; vertical-align: top; }",
        "    .element-box:hover { transform: scale(1.08); background-color: #2a2a2a; border-color: #bb86fc; box-shadow: 0 8px 12px rgba(187, 134, 252, 0.2); z-index: 10; cursor: default; }",
        "    h4 { margin: 0 0 8px 0; color: #03dac6; font-size: 1.1em; text-align: center; border-bottom: 1px solid #333; padding-bottom: 4px; }",
        "    ul { list-style-type: none; padding: 0; margin: 0; font-size: 0.75em; line-height: 1.4; color: #b0b0b0; }",
        "    li strong { color: #e0e0e0; }",
        "    .empty-box { border: none; background: transparent; box-shadow: none; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h3>PERIODIC TABLE</h3>",
        "  <div class=\"table-container\">",
        "    <table>",
        "      <tr>"
    ]

    current_position = 0

    for i, el in enumerate(elements):
        while current_position < el['position']:
            html_content.append("        <td class=\"empty-box\"></td>")
            current_position += 1

        html_content.append("        <td class=\"element-box\">")
        html_content.append(f"          <h4>{el['name']}</h4>")
        html_content.append("          <ul>")
        html_content.append(f"            <li><strong>No:</strong> {el['number']}</li>")
        html_content.append(f"            <li><strong>Sym:</strong> {el['small']}</li>")
        html_content.append(f"            <li><strong>Mass:</strong> {el['molar']}</li>")
        html_content.append(f"            <li><strong>e⁻:</strong> {el['electron']}</li>")
        html_content.append("          </ul>")
        html_content.append("        </td>")

        current_position += 1

        if current_position > 17:
            html_content.append("      </tr>")
            if i < len(elements) - 1:
                html_content.append("      <tr>")
            current_position = 0

    html_content.extend([
        "    </table>",
        "  </div>",
        "</body>",
        "</html>"
    ])

    with open('periodic_table.html', 'w') as output_file:
        output_file.write("\n".join(html_content))

if __name__ == '__main__':
    generate_periodic_table()
