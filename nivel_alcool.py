cerv = int(input('Informe a quantidade de copos de bebida alcoólica ingerida: '))
agua = int(input('Você tomou quantos copos de água? '))

if cerv <= agua:
    print('O nível de álcool ingerido está baixo! Não está embriagado...')
    if cerv == 0:
        print('Ainda não começou as biritas!')
        
else:
    print('!')
    print('Estás ficando bêbado nesse ritmo:', ' '+str(cerv)+ ' ','copos de bebida alcoólica')

    
