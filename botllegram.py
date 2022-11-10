import telebot

CHAVE_API = "Chave Bot"

bot = telebot.TeleBot(CHAVE_API)
@bot.message_handler(commands=["CRA"])
def Reclamacao(mensagem):
    texto = """
        (Clique em uma opção)
       /Matriculas para fazer matrículas 
       /Duvidas sobre a matrícula
       /Documentos para fazer matricula"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Matriculas"])
def Reclamacao(mensagem):
    texto = """
          •	CRA
            o	Matrículas: https://uniceplac.inscricao.crmeducacional.com/login/76
            Telefone: (61) 3035-3932
            
            o	Dúvidas sobre Matrícula
            Telefone: (61) 3035-3932

            o	Documentos para Matrícula: https://www.uniceplac.edu.br/graduacao/


•	Atendimento a comunidade;

(https://www.uniceplac.edu.br/comunidades/)"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Beneficios"])
def Reclamacao(mensagem):
    texto = """
       
            ● Benefícios 
            
            (Clique em uma opção)
                
            /Boletos para emissão de boletos   
            /Dividas para negociar as dívidas 

            o	Para informações sobre renovação dos benefícios (Novo Fies, Prouni, Posso).

            Contato
            Telefone: (61) 3035-1815
            E-mail: fies.prouni@uniceplac.edu.br

            o	Dúvidas
            Telefone: (61) 3035-1814
 """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["Boletos"])
def Reclamacao(mensagem):
    texto = """
         o	Para acessar os boletos clica no link abaixo
    
         https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/financeiro"""

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Dividas"])
def Reclamacao(mensagem):
    texto = """
    
        o  Para negociar dívidas clique no link abaixo 👇🏽
       
       Link para negociar dívidas:  https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/negociacao/introducao"""

    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["Duvidas"])
def Reclamacao(mensagem):
    texto = """
       Para sanar duvidas ligue no telefone:
        
        📞 (61) 3035-1814"""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Financeiro"])
def Reclamacao(mensagem):
    texto = """
       /Boletos para informação de boletos
       /Dividas para negociar as dividas
       /Duvidas para retirar as duvidas """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Declaracao"])
def Reclamacao(mensagem):
    texto = """ 
        Clique no link abaixo para obter a	declaração que você deseja. 
        
        https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/financeiro
    
   """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Documentos"])
def Reclamacao(mensagem):
    texto = """
        Para emissão de documentação clique no link abaixo: 
        
        https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/financeiro
         """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Carteirinha"])
def Reclamacao(mensagem):
    texto = """
    o	Para informações sobre a carteirinha ligue para o 
    Telefone: (61) 3035-3911 
    ou se preferir mande um e-mail para:
    
    📬E-mail: central.aluno@uniceplac.edu.br
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Calendario"])
def Reclamacao(mensagem):
    texto = """ 
    Para infomações sobre o	Calendário acadêmico acesse: 
    
    📆 https://www.uniceplac.edu.br/calendario-academico-2/
 """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Atividades"])
def Reclamacao(mensagem):
    texto = """ 
    Para atividades complementares acesse o link: 
    
    https://www.uniceplac.edu.br/atividades-complementares/
     """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["CAD"])
def Reclamacao(mensagem):
    texto = """
       /Boletos para informação de boletos
       /Documentos para emissão de documentos
       /Carteirinha para saber sobre a carteirinha 
       /Calendario para calendário acadêmicos 
       /Atividades para atividade complementares  
       /Declaracao para inforamção sobre declaroções"""
    bot.send_message(mensagem.chat.id, texto)

#opção3 do codigo de entrada
@bot.message_handler(commands=["Sim"])
def opcao1(mensagem):
    texto = """
    Olá tudo bem? Você gostaria de falar com qual setor? (⚠️Clique em uma opção)
    /Financeiro para falar com financeiro 
    /CAD para falar com o CAD
    /Beneficios para falar sobre os beneficios
    
     Para prosseguir com o atendimento é necessario que você clique em uma das opções 📢"""
    bot.send_message(mensagem.chat.id, texto)

#opção2 do codigo de entrada
@bot.message_handler(commands=["Nao"])
def opcao2(mensagem):
    texto = """
    Olá tudo bem? Você já conhece a nossa Universidade? (Clique em uma opção)
    /CRA
    /Atendimento a comunidade
    """
    bot.send_message(mensagem.chat.id, texto)
def verificar(mensagem):
    return True

#codigo de entrada
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Olá tudo bem? 
Eu me chamo ANNEBOT- sou a assistente virtual da UNICEPLAC.
 
Estou aqui para te auxíliar no atendimento incial.

    Você já é uma aluno(a) da Uniceplac?
    ( ⚠️Clique no item abaixo  ⚠️):
    
     /Sim,  sou aluno da Uniceplac
     /Nao,  gostaria de saber mais informações  
    
        
Para prosseguir com o atendimento é necessario que você clique em uma das opções 📢"""


    bot.reply_to(mensagem, texto)

bot.polling()
