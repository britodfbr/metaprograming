import docx
import pathlib
import tempfile

dout = pathlib.Path().resolve().joinpath('resultados')
fileinput = pathlib.Path(tempfile.NamedTemporaryFile(suffix='.docx').name)

fake_content = [
    '', '', '',
    'Epigrafe 1, de 9 de Abril de 2021', 'Ementa de modelo', 'O presidente em vigor, determina:',
    '', '', '', 'Paragrafo 1', 'Paragrafo 2', '', '', '', 'Paragrafo 3',
    'Brasília, 9 de Abril de 2021; 200º da Independência e 133º da República',
    '', '', '', 'Presidente', 'Ministro',]

document = docx.Document()
[document.add_paragraph(x) for x in fake_content]
document.save(fileinput) 
