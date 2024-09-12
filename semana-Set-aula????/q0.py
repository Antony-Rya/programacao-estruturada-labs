import os

os.mkdir('Projeto')
os.chdir('Projeto')
os.mkdir('dados')
os.mkdir('scripts')
os.mkdir('logs')
os.chdir('dados')
with open('clientes.txt', 'x') as arquivo:
    arquivo.write('Lista de Clientes')
with open('produtos.txt', 'x') as arquivo:
    arquivo.write('Lista de Produtos')

os.chdir('../scripts')

with open('principal.py', 'x') as arquivo:
    arquivo.write('#blablabla')
with open('utilidades.py', 'x') as arquivo:
    arquivo.write('#blablabla2')

os.chdir('../logs')

with open('app.log', 'x') as arquivo:
    arquivo.write('Arquivo de Log do Sistema')
