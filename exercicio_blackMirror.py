# DESENVOLVA UM PROGRAMA EM QUE O USUÁRIO IRÁ INFORMAR UMA
# PERGUNTA (UTILIZANDO EXATAMENTE AS PERGUNTAS DO QUESTIONÁRIO
# ANTERIOR) E O SISTEMA DEVERÁ APRESENTAR A RESPOSTA.
# Referente ao 1º episódio da 6ª temporada de Black Mirror.



# Escopo global
# mensagem = input("Escolha uma das opções: ")
pergunta = -1

# Escopo Local
while (pergunta != 0):            # != significa "diferente"  # Int = Indica que é um número inteiro, ou seja, não tem a vírgula ou ponto.
	pergunta = int(input(f''' 
================================================================================================
                            
                            ESCOLHA UMA PERGUNTA PARA VER A RESPOSTA:
          

[ 1 ] = QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?
          
[ 2 ] = QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?
          
[ 3 ] = QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?
          
[ 4 ] = COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?
          
[ 5 ] = QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?
          
[ 6 ] = QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?
          
[ 7 ] = O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.
					  
[ 0 ] = PARAR
          
================================================================================================
: '''))
	
	if(pergunta == 1):
		print(f'''
		
Joan (a atriz que faz a Joana na série é a Selma Hayleke).
		
		''')

	elif(pergunta == 2):
		print(f'''
		
Mona Javadi.
		
		''')

	elif(pergunta == 3):
		print(f'''
		
Streamberry.
		
		''')

	elif(pergunta == 4):
		print(f'''

Ao procurar algo para assistir junto com o namorado dela no Streamberry.
		
		''')

	elif(pergunta == 5):
		print(f'''

Ficou assustada, muito desesperada, não conseguia respirar devido ao desespero.
Tentou contactar a advogada e descobriu que eles podem fazer isso tudo porque a Joana aceitou os termos.
Fez algo pra deixa a atriz constrangida, só pra ver se a imagem da atriz seria manchada.
		
		''')

	elif(pergunta == 6):
		print(f'''

Aceitar termos e condições sem saber das consequências, o celular capta informações nossas conforme usamos.
A atriz que faz a Joan na série não é ela mesmo, é uma projeção digital que criaram porque ela também autorizou o uso de sua imagem. Deep Fake.
		
		''')

	elif(pergunta == 7):
		print(f'''
		
Era uma realidade inversa, era como uma outra vida, todas as personagens que achávamos serem as reais, eram uma relidade criada pelo computador da vida de cada uma real.
		
		''')

	elif(pergunta == 0):
		print(f'''
		
O B R I G A D O,   V O L T E   S E M P R E!
		
		
		''')
		break

	else:
		print(f'''
		

		 !!!  O P Ç Ã O   I N V Á L I D A !!!

		!!!  T E N T E   N O V A M E N T E !!!
		    
		    ESCOLHA UMA DAS OPÇÕES ACIMA!
		
		
		''')
