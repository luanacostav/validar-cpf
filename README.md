Olá, esse projeto ensina a validar um CPF!
Hi, this project teaches you how to validate a CPF (Brazilian individual taxpayer registry) number!

O exemplo abaixo demonstra como é feita a validação.
[The example below demonstrates how the validation is done]

CÁLCULO DO PRIMEIRO DÍGITO DO CPF (7)
[Calculation of the first digit of the CPF (7)]

CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando do 10.
[To calculate the sum of the first nine digits of the CPF by multiplying each digit by a decreasing sequence of numbers from 10 to 2]

Ex: 74682489070
  10  9  8  7  6  5  4  3  2
*  7  4  6  8  2  4  8  9  0
   70 36 48 56 12 20 32 27 0

Somar todos os resultados:
[Sum all the results:]

70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

Multiplicar  o resultado anterior por 10
[Multiply the previous result by 10]

301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
[Obtain the remainder of the previous result when divided by 11]

3010 % 11 = 7
Se o resultado anterior for maior que 9: [If the previous result is greater than 9]
    resultado é 0 [result = 0]
contrário disso: [opposite of that]
    resultado é o valor da conta [result = remainder]

O primeiro dígito do CPF é 7
[First digit = 7]

CALCULAR O SEGUNDO DÍGITO DO CPF (0)
[Calculation of the second digit of the CPF (0)]

Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando do 11
[To calculate the sum of the first nine digits of the CPF, + the first digit, by multiplying each digit by a decreasing sequence of numbers from 11 to 2]

Ex: 74682489070
 (11) 10 9  8  7  6  5  4  3  2
*  7  4  6  8  2  4  8  9  0 (7)
   77 40 54 64 14 24 40 36 0  14

Somar todos os resultados:
[Sum all the results:]

77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363

Multiplicar  o resultado anterior por 10
[Multiply the previous result by 10]

363 * 10 = 3630

Obter o resto da divisão da conta anterior por 11
[Obtain the remainder of the previous result when divided by 11]

3630 % 11 = 0

Se o resultado anterior for maior que 9: [If the previous result is greater than 9]
    resultado é 0 [result = 0]
contrário disso: [opposite of that]
    resultado é o valor da conta [result = remainder]