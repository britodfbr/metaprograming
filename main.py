import sys
from bicho import Bicho
from lex.interfaces import(
    AlterarBodyIdBehavior, EstilizarStatusOkBehavior, FormatarBehavior, InserirMsgRevogBehavior, SanitizarBehavior, SalvarBehavior,
    SanitizarDocx, FormatarBasicHTML, SalvarHTMLascii, AlterarBodyIdNoApply, 
    EstilizarStatusOkNoApply, InserirMsgRevogNoApply,
)
from lex.utils import fileinput, dout
from lex.fons_lex import FonsLexHOF15

fout = dout.joinpath(fileinput.with_suffix('.html').name)
fout.parent.mkdir(parents=True, exist_ok=True)

def metagrogramming1():
    print(fileinput.is_file(), fileinput)
    try:
        b = FonsLexHOF15(
            entrance=fileinput, 
            filename_output=fout,
            salvar_behavior=SalvarHTMLascii(), 
            sanitizar_behavior=SanitizarDocx(),
            formatar_behavior=FormatarBasicHTML(),
        )
        print(f"{b.entrance=}")
        print(f"{b.filename_output=}")
        print(f"{b.content=}")
        b.sanitizar()
        print(f"{b.content=}")
        b.formatar()
        print(f"{b.content=}")
        b.salvar()
    except (KeyError, RecursionError, TypeError):
        print(sys.exc_info())
        raise
    else:
        print(b)
        print(fout.is_file(), fout)

def metaprogramming0():
    b = Bicho()

    print(b.latir())
    print(b.grasnar())
    print(b.ladrar())


def run():
    metaprogramming0()
    print()
    metagrogramming1()


if __name__ == "__main__":
    run()
