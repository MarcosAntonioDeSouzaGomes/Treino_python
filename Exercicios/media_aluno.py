print('Esse Programa Calcula a nota do Aluno! ')
l = []
for a in range(4):
  n = float(input('Informe A nota do aluno '))
  l.append(n)
lista = l
media = float(lista[0] + lista[1] + lista[2] + lista[3]) / 4
print(f'Notas: nota 1 = {lista[0]}, nota 2 = {lista[1]}, nota 3 = {lista[2]}, nota 4 = {lista[3]}')
print(f'Media {media}')
if media >= 50:
  print('Situação do aluno: Aprovado!')
else:
  print('Situação do aluno: Reprovado!')
