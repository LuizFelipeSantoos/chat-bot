import telebot
import os

CHAVE_API = os.environ['keybot']

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["CRA"])
def Reclamacao(mensagem):
    texto = """
        Clique na opção desejada para prosseguir com atendimento 👇🏽
        
       /Matriculas para se matricular
       /Duvidas sobre a matrícula
      """
    bot.send_message(mensagem.chat.id, texto)



@bot.message_handler(commands=["Matriculas"])
def Reclamacao(mensagem):
    texto = """
            ● Matrículas

          •	CRA Centro de atendimento do aluno
          
            o	Matrículas: https://uniceplac.inscricao.crmeducacional.com/login/76
            📞 Telefone: (61) 3035-3932
            
            o	Dúvidas sobre Matrícula
            📞 Telefone: (61) 3035-3932

            o	Documentos para Matrícula: https://apps.uniceplac.edu.br/matricula-on-line"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Beneficios"])
def Reclamacao(mensagem):
    texto = """
       
            ● Benefícios 
            
            (⚠️ Clique em uma opção ⚠️)
          
            ●	Para informações sobre renovação dos benefícios (Novo Fies, Prouni, Posso).

            ●   Contato
            Telefone: (61) 3035-1815
            E-mail: fies.prouni@uniceplac.edu.br

            ●	Dúvidas
            Telefone: (61) 3035-1814
 """
    bot.send_message(mensagem.chat.id, texto)
    
@bot.message_handler(commands=["Atendimento"])
def Reclamacao(mensagem):
    texto = """ acesse o link abaixo para atendimento a comunidade 👇🏽
https://www.uniceplac.edu.br/comunidades/
 """
    bot.send_message(mensagem.chat.id, texto)    

@bot.message_handler(commands=["Boletos"])
def Reclamacao(mensagem):
    texto = """
         Para acessar os boletos, clique no link abaixo 👇🏽
    
         https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/financeiro"""

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Dividas"])
def Reclamacao(mensagem):
    texto = """
    
        Para negociar dívidas, clique no link abaixo 👇🏽
       
       Link para negociar dívidas:  https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/negociacao/introducao"""

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Duvidas"])
def Reclamacao(mensagem):
    texto = """
       Se ainda restou alguma dúvida ligue no telefone abaixo 👇🏽. 
        
        📞 (61) 3035-1814"""

    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Financeiro"])
def Reclamacao(mensagem):
    texto = """ 
        Clique na opção desejada 👇🏽
        
      /Dividas para negociar as dívidas
      /Duvidas  para retirar as dúvidas
      /Boletos para informações sobre boletos
    
   """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Declaracao"])
def Reclamacao(mensagem):
    texto = """ 
        Clique no link abaixo para obter a declaração que você deseja. 
        
        https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/financeiro
    
   """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Documentos"])
def Reclamacao(mensagem):
    texto = """
        Para emissão de documentação clique no link abaixo 👇🏽: 
        
        
        https://portal2.uniceplac.edu.br/FrameHTML/web/app/edu/PortalEducacional/#/requerimentos
         """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Carteirinha"])
def Reclamacao(mensagem):
    texto = """
    o	Para informações sobre a carteirinha ligue para o 
   📞 Telefone: (61) 3035-3911 
    
    ou se preferir mande um e-mail para:
    📬 E-mail:  central.aluno@uniceplac.edu.br
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
    Para atividades complementares acesse o link 👇🏽: 
    
    https://www.uniceplac.edu.br/atividades-complementares/
     """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["CAD"])
def Reclamacao(mensagem):
    texto = """
        Clique na opção desejada 👇🏽
        
       /Documentos para emissão de requerimentos de documentos
       
       /Carteirinha para saber sobre a carteirinha
        
       /Calendario para calendário acadêmico 
       
       /Atividades para atividades complementares 
        
       /Declaracao para informação sobre declarações"""
    bot.send_message(mensagem.chat.id, texto)

# opção3 do codigo de entrada


@bot.message_handler(commands=["Sim"])
def opcao1(mensagem):
    texto = """
    Olá tudo bem? Você gostaria de falar com qual setor?
    Clique na opção abaixo 👇🏽
    
    /Financeiro para falar com financeiro 
    /CAD para falar com a central de atendimento ao aluno
    /Beneficios para falar sobre os beneficios
    
     Para prosseguir com o atendimento é necessario que você clique em uma das opções 📢"""
    bot.send_message(mensagem.chat.id, texto)

# opção2 do codigo de entrada


@bot.message_handler(commands=["Nao"])
def opcao2(mensagem):
    texto = """
    Olá tudo bem? Você já conhece a nossa universidade? 
    (⚠️ Clique em uma opção ⚠️)
    
    /CRA para falar na central de atendimento do aluno 
    
    /Atendimento comunitário
    """
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True

# codigo de entrada


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
