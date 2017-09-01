import os
import random

import telebot

import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handleStart(message):
    userMarkup = telebot.types.ReplyKeyboardMarkup(True)
    userMarkup.row('/start', '/stop')
    userMarkup.row('Фото', 'Аудио', 'Стикер')
    userMarkup.row('Видео', 'Голос', 'Локация')
    helloText = 'Доброе пожаловать, <b>' + message.from_user.first_name + ' ' + message.from_user.last_name + '</b>\n' \
                                                                                                              '<i>Спасибо что решили воспользоваться нашим ботом.</i>'
    bot.send_message(message.from_user.id, helloText, reply_markup=userMarkup, parse_mode='HTML')


@bot.message_handler(commands=['stop'])
def handleStop(message):
    hideMarkup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'До новых встреч!', reply_markup=hideMarkup)


@bot.message_handler(content_types=['text'])
def hadleText(message):
    path = '/Users/marinalebedeva/PycharmProjects/telegramBotEcho/files'
    userID = message.from_user.id

    if message.text == 'Фото':
        directory = path + '/images'
        allFilesInDirectory = os.listdir(directory)
        randomFile = random.choice(allFilesInDirectory)
        img = open(directory + '/' + randomFile, 'rb')
        bot.send_chat_action(userID, 'upload_photo')
        bot.send_photo(userID, img)
        img.close()

    elif message.text == 'Аудио':
        directory = path + '/audio'
        allFilesInDirectory = os.listdir(directory)
        randomFile = random.choice(allFilesInDirectory)
        audio = open(directory + '/' + randomFile, 'rb')
        bot.send_chat_action(userID, 'upload_audio')
        bot.send_audio(userID, audio)
        audio.close()

    elif message.text == 'Стикер':
        stickerArray = [
            'CAADAgADCAADa-18CjWBoH9uCkN_Ag',
            'CAADAgADCgADa-18CmXAHK6c0PtMAg',
            'CAADAgADDAADa-18CttyX5zrgxa6Ag',
            'CAADAgADEAADa-18Co7vmgzcTYOdAg',
            'CAADAgADFgADa-18CgcoBnIvq3DlAg',
            'CAADAgADGwADa-18CrkXEinIu91YAg',
            'CAADAgADHwADa-18CnJ6NnqU84-1Ag',
            'CAADAgADLgADa-18CgqvqjvoHnoDAg',
            'CAADAgADMAADa-18CnXej_fJiU9RAg',
            'CAADAgADMgADa-18Cibgrl0_E1ViAg',
            'CAADAgADNAADa-18CruWnFstMHFVAg',
            'CAADAgADNgADa-18CihERAcO-l5GAg',
            'CAADAgADRAADa-18Cs96SavCm2JLAg',
            'CAADAgADRgADa-18CsI9MDuEoDOOAg',
            'CAADAgADSgADa-18Csp7U5uN1xWGAg',
            'CAADAgADTwADa-18Cmv8QYC4cQt0Ag',
            'CAADAgADUQADa-18Co7xKzBn162VAg',
            'CAADAgADVQADa-18CuIUrpQFH8HWAg',
            'CAADAgADVwADa-18CgZCLdOOrNquAg',
            'CAADAgADWQADa-18CgiQVRdA4XuHAg',
            'CAADAgADXAADa-18ChlQo8vUwd7fAg',
            'CAADAgADXwADa-18CsbNEOUBjdksAg',
            'CAADAgADYQADa-18ChWPwyBXGnRwAg',
            'CAADAgADZQADa-18Chd-_EkU8axWAg',
            'CAADAgADZwADa-18ClP5Ksum72DWAg',
            'CAADAgADZwADa-18ClP5Ksum72DWAg'
        ]
        randomStiker = random.choice(stickerArray)
        bot.send_sticker(userID, randomStiker)

    elif message.text == 'Локация':
        bot.send_chat_action(userID, 'find_location')
        bot.send_location(userID, 49.990493, 36.2344409)

    elif message.text == 'Голос':
        directory = path + '/voice'
        allFilesInDirectory = os.listdir(directory)
        randomFile = random.choice(allFilesInDirectory)
        voice = open(directory + '/' + randomFile, 'rb')
        bot.send_chat_action(userID, 'record_audio')
        bot.send_audio(userID, voice)
        voice.close()

    elif message.text == 'Видео':
        directory = path + '/video'
        allFilesInDirectory = os.listdir(directory)
        randomFile = random.choice(allFilesInDirectory)
        video = open(directory + '/' + randomFile, 'rb')
        bot.send_chat_action(userID, 'upload_video')
        bot.send_video(userID, video)
        video.close()

    else:
        text = 'Я не понимаю, какая это команда.\nПопробуй еще раз.'
        bot.send_message(message.from_user.id, text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
