import json
import os

from gtts import gTTS
from nltk.chat.util import Chat, reflections
from pydub import AudioSegment
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dialog import conversation_pairs, command_pairs

"""
NLTK
"""

nltk_chat = Chat(conversation_pairs, reflections)
command_chat = Chat(command_pairs, reflections)

"""
Google TTS
"""


def generate_ogg_file(text):
    file_path_mp3 = '../data/tts.mp3'
    file_path_ogg = '../data/tts.ogg'
    tts = gTTS(text)
    tts.save(file_path_mp3)
    t = AudioSegment.from_mp3(file_path_mp3)
    t.export(file_path_ogg, format="ogg")
    return file_path_ogg


"""
Telegram
"""

token = '714756239:AAHbPt0pF2S0Yggc0dvHn9cTdOVZaAIcC2o'


def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def stop_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Goodbye!")
    shutdown_telegram_client()


def respond_command(bot, update):
    response = nltk_chat.respond(update.message.text)
    # Save data, if any
    data = command_chat.respond(update.message.text)
    if data:
        update_user_data(update.message.chat.id, data)
    # Check what type of respond
    path = '../data/data_' + str(update.message.chat.id) + '.json'
    user_data = read_json(path)
    if 'voice' in user_data and user_data['voice']:
        ogg_path = generate_ogg_file(response)
        bot.send_voice(chat_id=update.message.chat_id, voice=open(ogg_path, 'rb'))
    else:
        bot.send_message(chat_id=update.message.chat_id, text=response)


def voice_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I will now talk to you!")
    update_user_data(update.message.chat.id, '{"voice": true}')


def text_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I will now write to you!")
    update_user_data(update.message.chat.id, '{"voice": false}')


def shutdown_telegram_client():
    updater.stop()
    updater.is_idle = False


def update_user_data(user_id, data):
    json_data = json.loads(data)
    path = '../data/data_' + str(user_id) + '.json'
    create_json_file_if_not_exists(path)
    user_data = read_json(path)
    # Add new data
    for key, value in json_data.items():
        user_data[key] = value
    # Write to data file
    with open(path, 'w+') as json_file:
        json.dump(user_data, json_file, ensure_ascii=False)


def create_json_file_if_not_exists(path):
    exists = os.path.isfile(path)
    if not exists:
        with open(path, 'w+') as json_file:
            json.dump({}, json_file, ensure_ascii=False)


def read_json(path):
    create_json_file_if_not_exists(path)
    with open(path, 'r') as json_file:
        return json.load(json_file)


# Create Updater object and attach dispatcher to it
updater = Updater(token)
dispatcher = updater.dispatcher

# Add command handler to dispatcher
dispatcher.add_handler(CommandHandler('start', start_command))
dispatcher.add_handler(MessageHandler(Filters.text, respond_command))
dispatcher.add_handler(CommandHandler('stop', stop_command))
dispatcher.add_handler(CommandHandler('text', text_command))
dispatcher.add_handler(CommandHandler('voice', voice_command))

updater.start_polling()
updater.idle()
