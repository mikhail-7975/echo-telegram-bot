from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.update import Update

import config


class TelegramBot:
    def __init__(self, bot_url: str,):
        self.updater = Updater(bot_url, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        self.updater.dispatcher.add_handler(CommandHandler('help', self.help))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, self.text_message_handler))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))

    def start(self, update: Update, context: CallbackContext):
        update.message.reply_text(
            "Привет! Это телеграм-бот `@merch_generator_bot`, генерирующий мерч "
            "(а именно футболку) с рисунком по текстовому описанию"
        )
        update.message.reply_text("Для генерация футболки с рисунком:\n"
                                  "1) Введите текстовое описание футболки, указав\n"
                                  "   - Название бренда, логотип которого вы хотите видеть на футболке\n"
                                  "   - Основной цвет футболки\n"
                                  "  - Для какого мероприятия предназначена футболка\n"
                                  "2) Дождитесь, пока бот сгенерирует изображение:)")


    def help(self, update: Update, context: CallbackContext):
        update.message.reply_text("Для генерация футболки с рисунком:\n"
                                  "1) Введите текстовое описание футболки, указав\n"
                                  "   - Название бренда, логотип которого вы хотите видеть на футболке\n"
                                  "   - Основной цвет футболки\n"
                                  "  - Для какого мероприятия предназначена футболка\n"                                
                                  "2) Дождитесь, пока бот сгенерирует изображение:)")

    def unknown(self, update: Update, context: CallbackContext):
        update.message.reply_text(
            "Sorry '%s' is not a valid command" % update.message.text)

    def text_message_handler(self, update: Update, context: CallbackContext):
        update.message.reply_text("text message handler")

    def run(self):
        self.updater.start_polling()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = TelegramBot(bot_url='https://test-echo-telegram-bot.herokuapp.com/5238183931:AAEUAMyLxWrMfekuJzfM1DKpdiimZqmxG3Q')
    app.run()