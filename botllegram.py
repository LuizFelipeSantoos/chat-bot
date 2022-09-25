import telebot

CHAVE_API = "Chave BOT"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["Matricula"])
def matricula(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde um momento iremos entrar em contato com você")


@bot.message_handler(commands=["Financeiro"])
def Financeiro(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde um momento iremos entrar em contato com você")


@bot.message_handler(commands=["Reclamacao"])
def Reclamacao(mensagem):
    bot.send_message(mensagem.chat.id, "Para reclamação clique em: /reclamacao")

#cursos que estão dentro de matrículas
@bot.message_handler(commands=["Cursos"])
def Reclamacao(mensagem):
    texto = """
       Em nossa Universidade temos os seguintes cursos (Clique em uma opção)
       /Sistema da informação para fazer matricula 
       /ADM para fazer matricula em administração
       /Medicina para fazer matricula"""
    bot.send_message(mensagem.chat.id, texto)

#opção3 do codigo de entrada
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Olá tudo bem? Você gostaria de falar com qual setor? (Clique em uma opção)
    /Financeiro para falar com financeiro 
    /Destrancar  para destrancar a matricula
    /Matricula para fazer matricula
    
    Para prosseguir com o atendimento é necessario que você clique em uma das opções"""
    bot.send_message(mensagem.chat.id, texto)

#opção2 do codigo de entrada
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    Olá tudo bem? Você já conhece a nossa Universidade? (Clique em uma opção)
    /Cursos para falar conhecer os cursos disponiveis 
    /Destrancar  para destrancar a matricula
    """
    bot.send_message(mensagem.chat.id, texto)

#opção3 do codigo de entrada
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Aguarde um instante que iremos entrar em contato com você")

#para iniciar com qualquer tipo de mensagem
def verificar(mensagem):
    return True

#codigo de entrada
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Olá tudo bem? Eu me chamo ANNEBOT- sou a assistente virtual da UNICEPLAC. 
Estou aqui para te auxíliar no atendimento incial.
    Você já é uma aluno(a) da Uniceplac? (Clique no item):
     /opcao1 Sim
     /opcao2 Não
     /opcao3 Gostaria de me matrícular 
     
     
Para prosseguir com o atendimento é necessario que você clique em uma das opções"""


    bot.reply_to(mensagem, texto)

bot.polling()
