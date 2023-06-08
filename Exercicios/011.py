lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
a = lar * alt
t = a / 2
print('Para pintar uma parede com área {:.2f}m² é necessário {:.2f} litros de tinta.'.format(a, t))
