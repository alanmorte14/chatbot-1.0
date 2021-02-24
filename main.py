import os

def start():
    # Apresentar o Chatbot
    print("Oi, eu sou seu chatbot ,tenho algumas perguntas pré programadas, que posso lhe respoder! ")
    
    # Pedir o nome
    nome = input("Digite seu nome: ")

    # Pedir o email
    email = input("Digite o seu email: ")

    while True:
     # Oferecer o menu de opções
        resposta = input(f"O que você quer saber hoje?{os.linesep} [1] - Como é Estudar no IFAL? {os.linesep} [2] - Qual curso você faz? {os.linesep} [3] - já que você cursa informatica tem como voce formatar o meu computador?{os.linesep} [4] - Oque você aprende no seu curso?{os.linesep} ")
   
     # PROCESSAR a resposta enviada
        processar_resposta(resposta,nome)

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f"{os.linesep}{nome}, Na maioria do tempo, é super cansativo, mas, é muito gratificante quando você consegue fazer algo que nunca pensou em fazer, por exemplo: Fazer seu próprio jogo da cobrinha, um site, etc;{os.linesep}")
   
    elif resposta == '2':
        print(f"{os.linesep}{nome}, Eu Curso, o Ensino Médio Técnico, para, Desenvolvimento de Sistemas!{os.linesep}")
   
    elif resposta == '3':
        print(f"{os.linesep}{nome}, Sim! Cobro 50 reais, mas, não são todos os estudantes de TI (Tecnologia da informação) que sabem formatar um computador. Caso queira entre em contato pelo Instagram: @alan_santos_360{os.linesep}")
    
    elif resposta == '4':
        print(f"{os.linesep}{nome}, No curso é ensinado Programação de diferentes especialidades, como: Programação web, Programação Orientada a Objetos, etc; {os.linesep}")
  
    else:
        print(f"{os.linesep}Digite apenas 1, 2, 3 ou 4{os.linesep}")



if __name__ == '__main__':
    start()
