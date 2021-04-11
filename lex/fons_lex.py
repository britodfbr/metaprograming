__author__ = '@britodfbr'

from .interfaces import (
    AlterarBodyIdBehavior,
    EstilizarStatusOkBehavior,
    FormatarBehavior,
    InserirMsgRevogBehavior,
    SanitizarBehavior,
    SalvarBehavior,
    SanitizarDocx,
    FormatarBasicHTML,
    SalvarHTMLascii,
    AlterarBodyIdNoApply,
    EstilizarStatusOkNoApply,
    InserirMsgRevogNoApply,
)


class FonsLexHOF15:
    behaviors = [
        AlterarBodyIdBehavior, EstilizarStatusOkBehavior, FormatarBehavior,
        InserirMsgRevogBehavior, SanitizarBehavior, SalvarBehavior
    ]

    def __init__(self, entrance, **kwargs):
        self.entrance = entrance
        for k, v in kwargs.items():
            if k in ["entrance", "filename_output"]:
                setattr(self, k, v)
            elif not any([isinstance(v, x) for x in self.behaviors]):
                raise TypeError(
                    f'This "{k}" must be lex.interfaces behaviors type')
            setattr(self, k, v)

    def __getattr__(self, name):
        def wrap(*args, **kwargs):
            # return locals()[f"self.{name}_behavior"].run(self)       # FAIL run by name
            f = eval(f"self.{name}_behavior")
            # return getattr(self, 'f').run(self)  # FAIL run by name
            # return locals()['f'].run(self)       # run by name
            return getattr(f, 'run')(self)  # run by name

        return wrap

    @property
    def entrance(self):
        return self.__entrance

    @entrance.setter
    def entrance(self, value):
        self.__entrance = value

    def __str__(self):
        return f'{self.__class__.__name__}: {self.entrance}'
