from elem import Elem, Text
from elements import *

class Page:
    def __init__(self, root):
        if not isinstance(root, Elem):
            raise TypeError("Root must be an Elem")
        self.root = root
        self.error_msg = ""

    # ---------- PUBLIC ----------

    def is_valid(self):
        self.error_msg = ""
        result = self._validate(self.root)
        if not result and not self.error_msg:
            self.error_msg = "Unknown validation error"
        return result

    def __str__(self):
        html = str(self.root)
        if isinstance(self.root, Html):
            return "<!DOCTYPE html>\n" + html
        return html

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


    def _validate(self, node):
        if isinstance(node, Text):
            return True

        if not isinstance(node, Elem):
            self.error_msg = "Node is not an Elem or Text"
            return False

        tag = node.tag
        content = node.content

        # ---------- Allowed tags ----------
        allowed_tags = {
            'html','head','body','title','meta','img',
            'table','th','tr','td',
            'ul','ol','li',
            'h1','h2','p','div','span','hr','br'
        }

        if tag not in allowed_tags:
            self.error_msg = f"Tag '{tag}' is not allowed"
            return False

        # ---------- html ----------
        if tag == 'html':
            if len(content) != 2:
                self.error_msg = "html must contain exactly 2 elements: head and body"
                return False
            if not isinstance(content[0], Head):
                self.error_msg = "html first child must be Head"
                return False
            if not isinstance(content[1], Body):
                self.error_msg = "html second child must be Body"
                return False
            return self._validate(content[0]) and self._validate(content[1])

        # ---------- head ----------
        if tag == 'head':
            titles = [c for c in content if isinstance(c, Title)]
            if len(titles) != 1:
                self.error_msg = "head must contain exactly one Title"
                return False
            for c in content:
                if not isinstance(c, Title):
                    self.error_msg = "head can only contain Title"
                    return False
                if not self._validate(c):
                    return False
            return True

        # ---------- body / div ----------
        if tag in ('body', 'div'):
            allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text)
            for c in content:
                if not isinstance(c, allowed):
                    self.error_msg = f"{tag} contains invalid child type: {type(c).__name__}"
                    return False
                if not self._validate(c):
                    return False
            return True

        # ---------- single Text only ----------
        if tag in ('title', 'h1', 'h2', 'li', 'th', 'td'):
            if len(content) != 1:
                self.error_msg = f"{tag} must contain exactly one Text"
                return False
            if not isinstance(content[0], Text):
                self.error_msg = f"{tag} must contain only Text"
                return False
            return True

        # ---------- p ----------
        if tag == 'p':
            if len(content) == 0:
                self.error_msg = "p must contain at least one Text"
                return False
            for c in content:
                if not isinstance(c, Text):
                    self.error_msg = "p can only contain Text"
                    return False
            return True

        # ---------- span ----------
        if tag == 'span':
            for c in content:
                if not isinstance(c, (Text, P)):
                    self.error_msg = "span can only contain Text or P"
                    return False
                if isinstance(c, P) and not self._validate(c):
                    return False
            return True

        # ---------- ul / ol ----------
        if tag in ('ul', 'ol'):
            if len(content) == 0:
                self.error_msg = f"{tag} must contain at least one li"
                return False
            for c in content:
                if not isinstance(c, Li):
                    self.error_msg = f"{tag} can only contain li"
                    return False
                if not self._validate(c):
                    return False
            return True

        # ---------- tr ----------
        if tag == 'tr':
            if len(content) == 0:
                self.error_msg = "tr must contain at least one th or td"
                return False

            all_th = all(isinstance(c, Th) for c in content)
            all_td = all(isinstance(c, Td) for c in content)

            if not (all_th or all_td):
                self.error_msg = "tr must contain only th OR only td (not mixed)"
                return False

            for c in content:
                if not self._validate(c):
                    return False
            return True

        # ---------- table ----------
        if tag == 'table':
            if len(content) == 0:
                self.error_msg = "table must contain at least one tr"
                return False
            for c in content:
                if not isinstance(c, Tr):
                    self.error_msg = "table can only contain tr"
                    return False
                if not self._validate(c):
                    return False
            return True

        # ---------- self-closing ----------
        if tag in ('meta', 'img', 'hr', 'br'):
            return True

        return True
