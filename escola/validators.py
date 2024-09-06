import re
def nome_invalido(nome):
    return not nome.isalpha()

def num_celular_invalido(num_celular):
      modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
      response = re.findall(modelo, num_celular)
      return not response