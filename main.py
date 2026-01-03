def aprov_escolar():
    while True:
        try:
            prova1 = float(input("Nota da primeira prova: "))
            prova2 = float(input("Nota da segunda prova: "))
            prova3 = float(input("Nota da terceira prova: "))
            frequencia = int(input("Frequencia do aluno: "))
            media_g1 = (prova1 + prova2 + prova3) /3
            
            if any (nota <0 or nota >10 for nota in [prova1, prova2, prova3]):
                print("Erro! Insira apenas valores de 1 a 10.")
                continue
            elif frequencia <0 or frequencia >100:
                print("Erro! A frequencia não pode ser menor que 0 ou maior que 100.")
                continue
            else:
                print(f"\nSua média G1 foi: {media_g1:.2f}")
                break
        except ValueError:
            print("Erro! Digite apenas números válidos.\n")
    
    if frequencia < 75:
        print("\nO aluno reprovou por faltas")
    elif frequencia >= 75 and media_g1 >=7:
        print("\nVocê foi aprovado em Grau 1")
    elif media_g1 < 4:
        print("\nVocê reprovou em Grau 1")
    else:
        print("\nVocê foi para recuperação G2")
        
        while True:
            try:
                provag2 = float(input("Nota da G2: "))
                if provag2 <0 or provag2 >10:
                    print("Erro! Insira apenas valores de 1 a 10.")
                    continue
                
                mediag2 = (media_g1 + provag2) / 2    
                if mediag2 >=5:
                    print(f"\nVocê foi aprovado em Grau 2: {mediag2:.2f}")
                else:
                    print("\nVocê foi reprovado em Grau 2: {mediag2:.2f}")
                break
            
            except ValueError:
                print("Entrada inválida para G2.")
            
aprov_escolar()
