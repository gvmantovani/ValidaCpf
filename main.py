"""
CPF  Valido = 168.995.350-09
Formula:
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
    297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

# Loop infinito
import re

print('\n insira um CPF completo (apenas números) \n')

ValorCPF = input('Digite o CPF: ')
entrada = re.findall("\d", ValorCPF)

if len(ValorCPF) > 14 or len(entrada) < 11 or len(entrada) > 11:
    print('CPF INVÁLIDO')

else:
    valid = 0
    for dig in range(0, 11):
        valid += int(entrada[dig])
        dig += 1
    if int(entrada[0]) == valid / 11:
        print("CPF INVÁLIDO")

    else:
        soma = 0
        count = 10
        for i in range(0, len(entrada)-2):
            soma = soma + (int(entrada[i])*count)
            i+=1
            count-=1
        dg1 = 11-(soma%11)
        if dg1 >= 10:
            dg1 = 0
        soma = 0
        count = 10
        for j in range(1, len(entrada)-1):
            soma = soma + (int(entrada[j])*count)
            j+=1
            count-=1
        dg2 = 11-(soma%11)
        if dg2 >= 10:
            dg2 = 0

        if int(entrada[9]) != dg1 or int(entrada[10]) != dg2:
            print("CPF INVÁLIDO")
        else:
            print(' CPF VÁLIDO ')
