from elem import Elem, Text

# ---------- Helpers ----------

def normalize(content):
    if content is None:
        return None

    if isinstance(content, str):
        return Text(content)

    if isinstance(content, list):
        new = []
        for c in content:
            if isinstance(c, str):
                new.append(Text(c))
            else:
                new.append(c)
        return new

    return content


# ---------- Core ----------

class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('html', attr or {}, normalize(content))


class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('head', attr or {}, normalize(content))


class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('body', attr or {}, normalize(content))


# ---------- Basic ----------

class Title(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('title', attr or {}, normalize(content))


class H1(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h1', attr or {}, normalize(content))


class H2(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h2', attr or {}, normalize(content))


class P(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('p', attr or {}, normalize(content))


class Div(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('div', attr or {}, normalize(content))


class Span(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('span', attr or {}, normalize(content))


# ---------- Lists ----------

class Ul(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ul', attr or {}, normalize(content))


class Ol(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ol', attr or {}, normalize(content))


class Li(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('li', attr or {}, normalize(content))


# ---------- Tables ----------

class Table(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('table', attr or {}, normalize(content))


class Tr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('tr', attr or {}, normalize(content))


class Th(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('th', attr or {}, normalize(content))


class Td(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('td', attr or {}, normalize(content))


# ---------- Self-closing ----------

class Img(Elem):
    def __init__(self, attr=None):
        super().__init__('img', attr or {}, tag_type='simple')


class Meta(Elem):
    def __init__(self, attr=None):
        super().__init__('meta', attr or {}, tag_type='simple')


class Hr(Elem):
    def __init__(self, attr=None):
        super().__init__('hr', attr or {}, tag_type='simple')


class Br(Elem):
    def __init__(self, attr=None):
        super().__init__('br', attr or {}, tag_type='simple')

if __name__ == '__main__':
    html = Html(content=[
        Head([
            Title('"Hello ground!"')
        ]),
        Body([
            H1('"Oh no, not again!"'),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])

    print(html)

