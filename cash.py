from time import sleep

nome = str(input('informe o seu nome: '))
fun = str(input('Sr(a) {} Informe a sua Profissão: '.format(nome)))
gh = float(input('Sr(a) {} Diga o valor que voce ganha por mes R$ '.format(nome)))
hm = float(input('Sr(a) {} Informe a quantidade de horas que o senhor trabalhou no mês : '.format(nome)))

st = (gh / hm) * hm
ipR = (11/100) * st
inss = (8/100) * ipR
sindi = (5/100) * inss
sal = st - (sindi + inss + ipR)

sleep(2)

print('sr {} o seu Salario liguido sera no valor de R$ {:.2f}'.format(nome, sal))
if sal == '1122.00':
    print('Voce sr {} recebe um salario minimo'.format(nome))
else:
    print('O seu salario sr(a){} é superior ao salario minimo.'.format(nome))
