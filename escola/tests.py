from django.test import TestCase

def validate_num_celular(num_celular):
    lista_num = list(num_celular)
    for i in lista_num:
            if not i.isdigit():
                print('Número de celular deve conter somente digitos.')
                return False
    if len(num_celular) != 11:
            print('Número de celular deve ter 11 digitos!')
    lista_num.insert(2, ' ')
    lista_num.insert(8, '-')
    return ''.join(lista_num)
print(validate_num_celular('1234567894a'))