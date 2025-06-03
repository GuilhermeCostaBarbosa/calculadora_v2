tempoExperiencia = 3

if tempoExperiencia < 2:
    print('Nível de conhecimento júnior')
#Imposta a comparação >= 2 devido ao fato de que, quando deixamos apenas temperaturaExperiencia > 2 e damos o valor dois para a váriavel, ele entra no "else" e imprime 'Nível de conhecimento sênior'
elif tempoExperiencia >= 2 and tempoExperiencia < 5:
    print('Nível de conhecimento pleno')
else:
    print('Nível de conhecimento sênior')