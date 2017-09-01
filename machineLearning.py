from wit import Wit
import telebot
import config

bot = telebot.TeleBot(config.token)

client = Wit(access_token=config.accessTokenWIT)


def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']

    except:
        pass
    return value


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    responseText = wit_response(message.text)
    if responseText == None:
        responseText = 'Я не знаю, что и ответить...'
    bot.send_message(message.chat.id, responseText)


if __name__ == '__main__':
    bot.polling(none_stop=True)
