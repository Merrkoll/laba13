from transitions import Machine
import telebot

TOKEN = '6506694540:AAFIcq7w4vbYJLCRa6tSf16SpEpLwc9LMXc'
bot = telebot.TeleBot(TOKEN)


class User(object):
    def init(self, name):
        self.name = name
        self.machine = Machine(model=self, states=['main_menu', 'women_single', 'men_single', 'next_men',
                                                   'next_women'], initial='main_menu')
        self.machine.add_transition(trigger='welcome', source='*', dest='main_menu')
        self.machine.add_transition(trigger='women_single', source='main_menu', dest='women_single')
        self.machine.add_transition(trigger='men_single', source='main_menu', dest='men_single')
        self.machine.add_transition(trigger='next_men', source='men_single', dest='next_men')
        self.machine.add_transition(trigger='next_women', source='women_single', dest='next_women')


@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Здравствуйте, я чат-бот помощник по баскетболу"
                              " Для взаимодействия со мной "
                              "используй следующие команды:\n"
                              "\n /NBA - результаты NBA\n"
                              "/VTB - результаты Единой Лиги ВТБ\n")


@bot.message_handler(commands=['VTB'])
def women_single(message):
    user_id = message.chat.id
    bot.send_message(user_id, " Результаты Единой Лиги ВТБ:\n\n1 место - Уникс\n"
                              "2 место - Локомотив-Кубань\n3 место - ЦСКА\n\n"
                              "/next_VTB - показать 4 и 5 место\n\n"
                              "Для возврата в главное меню используйте /start")


@bot.message_handler(commands=['next_VTB'])
def next_women(message):
    user_id = message.chat.id
    bot.send_message(user_id, "\n4 место - Зенит"
                              "\n5 место - Автодор"      
                              "\nДля возврата в главное меню используйте /start")


@bot.message_handler(commands=['NBA'])
def men_single(message):
    user_id = message.chat.id
    bot.send_message(user_id, " Результаты NBA:\n\n1 место - Милуоки Бакс\n"
                              "2 место - Бостон Селтикс\n3 место - Филадельфия Сиксерс\n\n"
                              "/next_NBA - показать 4 и 5 место\n\n"
                              "Для возврата в главное меню используйте /start")


@bot.message_handler(commands=['next_NBA'])
def next_men(message):
    user_id = message.chat.id
    bot.send_message(user_id, "\n4 место - Денвер Наггетс"                  
                              "\n5 место - Кливленд Кавальерс"                       
                              "\nДля возврата в главное меню используйте /start")


bot.polling(none_stop=True)
