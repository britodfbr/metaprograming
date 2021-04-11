__author__ = '@britodfbr'

import docx
from bs4 import BeautifulSoup, Doctype
from .behaviors import (
    AlterarBodyIdBehavior, EstilizarStatusOkBehavior, FormatarBehavior, InserirMsgRevogBehavior, SanitizarBehavior, SalvarBehavior
)


class SanitizarDocx(SanitizarBehavior):
    def run(self, cls):
        document = docx.Document(cls.entrance)
        parags = [x.text for x in document.paragraphs if x.text]
        soup = BeautifulSoup('', 'html5lib')
        for parag in parags:
            tp = soup.new_tag('p')
            tp.string = parag
            soup.body.append(tp)
        cls.content = soup
        return True if cls.content else False


class FormatarBasicHTML(FormatarBehavior):
    def run(self, cls):
        try:
            soup = cls.content
            # to HTML5
            [item.extract() for item in soup.contents if isinstance(item, Doctype)]
            soup.insert(0, Doctype('html'))
            soup.html.attrs = {}
            soup.html['lang'] = 'pt-br'
            if not soup.head:
                soup.html.insert(0, soup.new_tag('head'))

            # HTML attrs
            soup.html.attrs = {}

            # Flagging epigrafe
            soup.select_one('p:nth-of-type(1)').attrs = {'class': 'epigrafe'}

            # Flagging ementa
            soup.select_one('p:nth-of-type(2)').attrs = {'class': 'ementa'}

            cls.content = soup
        except AttributeError:
            return False
        else:
            return True


class SalvarHTMLascii(SalvarBehavior):
    def run(self, cls):
        cls.filename_output.with_suffix('.html').write_text(cls.content.prettify(formatter='html'))
        return cls.filename_output.with_suffix('.html').is_file()


class AlterarBodyIdNoApply(AlterarBodyIdBehavior):
    def run(self, cls):
        print("Don't apply in this case")


class EstilizarStatusOkNoApply(EstilizarStatusOkBehavior):
    def run(self, cls):
        print("Don't apply in this case")


class InserirMsgRevogNoApply(InserirMsgRevogBehavior):
    def run(self, cls):
        print("Don't apply in this case")
