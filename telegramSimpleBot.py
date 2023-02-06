"""
t.me/edson001_bot
Key-API 6023517900:AAEhgKFV_QDN-iMcunaS2wOQRBmBxf9uaJ0
"""
import telebot

API_KEY = "6023517900:AAEhgKFV_QDN-iMcunaS2wOQRBmBxf9uaJ0"
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, "Enviar Reclamação para...")


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Enviar Reclamação para...")


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    print(mensagem)
    bot.reply_to(mensagem, "Edson Agradece os elogios")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
        Escolha uma opção para continuar (Clique no item)
            /opcao1 Fazer um pedido
            /opcao2 Reclamar de um pedido
            /opcao3 Elogiar o programador
    """
    bot.reply_to(mensagem, texto)


bot.polling()
