cpf = '15853787551' # Inserir o cpf desejado 
cpf_9 = cpf[:9]

mult_num1 = 10
mult_num2 = 11

result_soma1 = 0
result_soma2 = 0

for num1 in cpf_9:
    num1_int = int(num1)
    result_soma1 += (num1_int * mult_num1)
    mult_num1 -= 1

resto_divisao1 = (result_soma1 * 10) % 11

digito_1 = resto_divisao1 if resto_divisao1 <= 9 else 0

cpf_10 = cpf[:9] + str(digito_1)

for num2 in cpf_10:
    num2_int = int(num2)
    result_soma2 += (num2_int * mult_num2)
    mult_num2 -= 1

resto_divisao2 = (result_soma2 * 10) % 11

digito_2 = resto_divisao2 if resto_divisao2 <= 9 else 0


validar_cpf = f'{cpf_9}{digito_1}{digito_2}'

if validar_cpf == cpf:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')