import sys
from elements import *
from Page import Page


# ---------- Colors ----------

class C:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RESET = '\033[0m'


def cprint(text, color):
    print(f"{color}{text}{C.RESET}")


# ---------- Tester ----------

class PageTester:

    def __init__(self, verbose=True, show_code=False):
        self.verbose = verbose
        self.show_code = show_code
        self.total = 0
        self.passed = 0

    def run(self):
        self.section("HTML", self.test_html())
        self.section("HEAD", self.test_head())
        self.section("BODY/DIV", self.test_body_div())
        self.section("SPAN", self.test_span())
        self.section("UL/OL", self.test_ul_ol())
        self.section("TR", self.test_tr())
        self.section("TABLE", self.test_table())
        self.section("TEXT RULE", self.test_single_text())
        self.section("P", self.test_p())

        print("\n" + "=" * 40)
        cprint(f"RESULT: {self.passed}/{self.total} passed", C.BLUE)

    # ---------- Core runner ----------

    def check(self, name, page, expected):
        self.total += 1
        result = page.is_valid()

        if result == expected:
            self.passed += 1
            cprint(f"[OK] {name}", C.GREEN)
        else:
            cprint(f"[FAIL] {name}", C.RED)
            cprint(f"  expected={expected}, got={result}", C.YELLOW)
            if page.error_msg:
                cprint(f"  error: {page.error_msg}", C.YELLOW)

        if self.show_code:
            print(page, "\n")

    def section(self, name, tests):
        print(f"\n{'='*15} {name} {'='*15}")
        for name, page, expected in tests:
            self.check(name, page, expected)

    # ---------- Tests ----------

    def test_html(self):
        return [
            ("Missing body", Page(Html([Head()])), False),
            ("Missing head", Page(Html([Body()])), False),
            ("Wrong order", Page(Html([Body(), Head(Title(Text("x")))])), False),
            ("Valid html", Page(Html([Head(Title(Text("x"))), Body()])), True),
        ]

    def test_head(self):
        return [
            ("Empty head", Page(Head()), False),
            ("Wrong child", Page(Head(H1(Text("x")))), False),
            ("Valid head", Page(Head(Title(Text("x")))), True),
        ]

    def test_body_div(self):
        return [
            ("Body with Title", Page(Body(Title(Text("x")))), False),
            ("Body with H1", Page(Body(H1(Text("x")))), True),
        ]

    def test_span(self):
        return [
            ("Span with Title", Page(Span(Title(Text("x")))), False),
            ("Span with P", Page(Span(P(Text("x")))), True),
        ]

    def test_ul_ol(self):
        return [
            ("Ul wrong child", Page(Ul(Title(Text("x")))), False),
            ("Ol mixed children", Page(Ol([Li(Text("x")), Ul(Text("x"))])), False),
            ("Ol valid", Page(Ol(Li(Text("x")))), True),
        ]

    def test_tr(self):
        return [
            ("Tr wrong child", Page(Tr(Li(Text("x")))), False),
            ("Tr mixed td/th", Page(Tr([Td(Text("x")), Th(Text("x"))])), False),
            ("Tr valid td", Page(Tr([Td(Text("x")), Td(Text("x"))])), True),
        ]

    def test_table(self):
        return [
            ("Table wrong child", Page(Table(Li(Text("x")))), False),
            ("Table mixed", Page(Table([Tr(Td(Text("x"))), Td(Text("x"))])), False),
            ("Table valid", Page(Table([Tr(Td(Text("x"))), Tr(Td(Text("x")))])), True),
        ]

    def test_single_text(self):
        return [
            ("H1 empty", Page(Html([
                Head(Title(Text("ok"))),
                Body([H1()])
            ])), False),
        ]

    def test_p(self):
        return [
            ("P multiple text", Page(P([Text("a"), Text("b")])), True),
            ("P empty", Page(P()), False),
            ("P with element", Page(P(H2())), False),
        ]


# ---------- Run ----------

if __name__ == "__main__":
    tester = PageTester(verbose=True, show_code=False)
    tester.run()
    print("\n" + "=" * 40)
    print("test print\n")
    print(Page(Html([Head(Title(Text("x"))), Body()])))
    Page(Html([Head(Title(Text("x"))), Body()])).write_to_file("test.html")
