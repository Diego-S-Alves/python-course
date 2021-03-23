larg = float(input('Insira a largura da parede: '))
alt = float(input('Insira a altura da parede: '))
tint = (larg * alt) / 2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {(larg*alt):.2f} metros quadrados.')
print(f'Necessários {tint} litros de tinta.')
