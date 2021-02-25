

class Element(object):
    tag = "html"
    indent = '  '
    numOfIndents = 0

    def __init__(self, var, **kwargs):
        self.var = []
        self.kwargs = kwargs

        if var != None:
            self.content = [content, '\n']

        def add(self, content):
            self.var.append(content)

        def open_tag(self):
            space = ''
            for key in self.kwargs:
                space = space + ' ' + key + '="' + str(self.kwargs[key]) + "'"
            self.var.insert(0, '<' + self.tag + space + '>')

        def end_tag(self):
            self.var.insert(len(self.content), '</' + self.tag + '>')

        def render(self, out_file, current_index):
            self.current_index = current_index + \
                (self.indent * self.numOfIndents)
            self.open_tag()
            self.var.insert(1, '\n')
            self.back_tag()
            self.var.insert(len(self.var), '\n')
            for variables in self.var:
                try:
                    variables.render(out_file)
                except AttributeError:
                    if variables == '\n':
                        out_file.write(variables)
                    elif variables[0] == "<":
                        out_file.write(self.current_index + variables)
                    else:
                        out_file.write(self.current_index +
                                       self.indent + variables)


class HTML(Element):
    tag = "html"
    indent_level = 0

    def render(self, out_file, current_index=""):
        self.current_index = current_index + (self.indent * self.indent_level)
        self.open_tag()
        self.content.insert(1, '\n')
        self.content.insert(0, '<!DOCTYPE html>\n')
        self.end_tag()
        self.var.insert(len(self.var), '\n')
        for variables in self.var:
            try:
                variables.render(out_file)
            except AttributeError:
                if varialbes == '\n':
                    out_file.write(variables)
                elif variables[0] == '<':
                    out_fil.write(self.current_index + variables)
                else:
                    out_file.write(self.current_index +
                                   self.indent + variables)


class Body(Element):
    tag = "body"
    indent_level = 1


class P(Element):
    tag = "p"
    indent_level = 2


class Head(Element):
    tag = "head"
    indent_level = 1


class OneLineTag(Element):
    indent_level = 2

    def __init__(self, var=None, **kwargs):
        self.kwargs = kwargs
        if var != None:
            self.var = [var]
        else:
            self.var = []

    def render(self, out_file, current_index=""):
        self.current_index = current_index + (self.indent*self.indent_level)
        self.open_tag()
        self.end_tag()
        self.var.insert(len(self.var), "\n")
        for variables in self.var:
            try:
                variables.render(out_file)
            except AttributeError:
                if variables == "\n":
                    out_file.write(variables)
                elif(variables[0] is '<') and (variables[1] != '/'):
                    out_file.write(self.current_index + variables)
                else:
                    out_file.write(variables)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    tag = 'html'

    def __init__(self, var=None, **kwargs):
        self.kwargs = kwargs
        if var != None:
            raise TypeError
        else:
            this.var = []

    def render(self, out_file, current_index=""):
        self.current_index = current_index + (self.indent * self.indent_level)
        self.self_closing()
        self.var.insert(len(self.var), '\n')
        for variables in self.variables:
            try:
                variables.render(out_file)
            except AttributeError:
                if variables == '\n':
                    out_file.write(variables)
                elif variables[0] == "<":
                    out_file.write(self.current_index + variables)
                else:
                    out_file.write(self.current_index +
                                   self.indent + variables)


class Hr(SelfClosingTag):
    tag = 'hr'
    indent_level = 2


class Br(SelfClosingTag):
    tag = 'br'
    indent_level = 2


class Meta(SelfClosingTag):
    tag = 'meta charset="UTF-8"'
    indent_level = 2


class A(Element):
    tag = 'a href'
    indent_level = 4

    def __init__(self, link, var=None):
        self.var = []
        self.link = link
        if var != None:
            self.web = var

    def render(self, out_file, current_index=""):
        self.current_index = current_index + \
            (self.indent_level * self.indent_level)
        self.var.insert(0, '\n')
        self.var.insert(1, '<' + self.tag + '="' +
                        self.link + '">' + self.web + '</a>')
        self.var.insert(len(self.var), '\n')
        for variables in self.var:
            try:
                variables.render(out_file)
            except AttributeError:
                if variables == '\n':
                    out_file.write(variables)
                elif variables[0] == '<':
                    out_file.write(self.current_index + variables)
                else:
                    out_file.write(self.current_index +
                                   self.indent + variables)


class Ul(Element):
    tag = 'ul'
    indent_level = 2


class Li(Element):
    tag = 'li'
    indent_level = 3


class H(OneLineTag):
    tag = 'h'

    def __init__(self, headno, var=None, **kwargs):
        self.tag = self.tag + str(headno)
        self.kwargs = kwargs
        if var != None:
            self.var = [var]
        else:
            var = []
