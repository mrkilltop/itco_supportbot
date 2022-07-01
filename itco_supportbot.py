import telebot
from telebot import types
import time
bot = telebot.TeleBot("There was a token ¯\_(ツ)_/¯")

@bot.message_handler(commands=['start'])
def select_specialization(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    employer = types.KeyboardButton('👩‍🔬 Работодатель')
    employee = types.KeyboardButton('👩‍💼 Работник')
    markup.add(employer, employee)

    bot.send_message(message.chat.id, 'Выберите,  кто вы?', reply_markup = markup) 

@bot.message_handler(content_types = ['text'])
def employee(message):
    if message.text == '👩‍🔬 Работодатель':
        employer_bulletpoints(message)

    elif message.text == '👩‍💼 Работник':
        employee_bulletpoints(message)

# пункты для работодателя
    elif message.text == '💰 Льготные налоги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        another_bulletpoints = types.KeyboardButton('🔙  Другие пункты')
        markup.add(another_bulletpoints)

        bot.send_message(message.chat.id, 'До 31 декабря 2024 года 0% налог на прибыль при операциях в любой валюте.\n\n*Страхование*\nСтраховые взносы за работников - 7,6%\nОМС - 0.1%\nОбязательное социальное страхование - 1,5%\nПенсионное страхование - 6%\nСтрахование на случай временной нетрудоспособности и в связи с материнством - 1,5%.', parse_mode= 'Markdown', reply_markup = markup)

    elif message.text == '🤺 Помочь сотруднику по отсрочке от армии':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        another_bulletpoints = types.KeyboardButton('🔙  Другие пункты')
        markup.add(another_bulletpoints)

        bot.send_message(message.chat.id, 'Сотрудник должен иметь высшее образование и работать в аккретованных организациях > 1 года.\n\nТакже распространяется на специалистов со стажем менее 1 года, но при условии, что они окончили ВУЗ за год до момента своего назначения на должность.\n\nКомпании должны формировать и направлять через [Госуслуги](https://www.gosuslugi.ru) в Минцифры России списки работников, претендующих на отсрочку более чем за 50 дней до начала призывной компании.', parse_mode= 'Markdown', reply_markup = markup)

    elif message.text == '💳 Льготы по кредитам':
        credit_business_type(message)

    elif message.text == '➕ Остальные льготы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        another_bulletpoints = types.KeyboardButton('🔙  Другие пункты')
        markup.add(another_bulletpoints)

        bot.send_message(message.chat.id, 'Все представители бизнеса могут получить до 6 месяцев кредитных каникул, либо уменьшение размера платежей до 31 декабря 2024 года.\n\nПлановые проверки не проводятся до 31 декабря 2024 года.\n\n[Грантовая поддержка перспективных разработок](https://ит-гранты.рф).', parse_mode= 'Markdown', reply_markup = markup)

    elif message.text == '🔙  Другие пункты':
        employer_bulletpoints(message)

    elif message.text == '▪️ Малый бизнес и самозанятые':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        another_bulletpoints = types.KeyboardButton('🔙  Другие пункты')
        markup.add(another_bulletpoints)

        bot.send_message(message.chat.id, '*Программы\nПСК «Инвестиционная»*\nКредит (или рефинансировать его) на сумму 3 млн - 2 млрд рублей на срок до 3 лет по ставке до 15%.\nСредства могут быть направлены на создание, приобретение основных средств производства, в том числе для модернизации и технического перевооружения, а также для строительства, реконструкции, модернизации объектов капитального строительства.\n\n*ПСК «Оборотная»*\nКредит (или рефинансировать его) на сумму до 300 млн рублей\nНа срок до 1 года (можно больше, но далее применяется коммерческая ставка банка).\nЦелью может являться что угодно, кроме многоквартирного жилищного строительства.\n\n[«ФОТ 3.0»](http://government.ru/support_measures/measure/150/)\nДля покрытия расходов по зарплате сотрудникам, обслуживания других кредитов доступна программа с суммой кредита до 500 млн рублей по ставке 3%.\nУсловие - сохранение численности 90% сотрудников.\n\n[Список участвующих в программе банков](https://corpmsp.ru/bankam/programma_stimulir/).\nПрограммы действуют до конца 2022 года.\nЗаёмщик не должен входить в группу с компаниями-представителями крупного бизнеса и должен быть внесён в реестр субъектов МСП.', parse_mode= 'Markdown', reply_markup = markup)

    elif message.text == '◾️ Средний бизнес':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        another_bulletpoints = types.KeyboardButton('🔙  Другие пункты')
        markup.add(another_bulletpoints)

        bot.send_message(message.chat.id, '*Программы\nПСК «Инвестиционная»*\nКредит (или рефинансировать его) на сумму 3 млн - 2 млрд рублей на срок до 3 лет по ставке до 13,5%.\nСредства могут быть направлены на создание, приобретение основных средств производства, в том числе для модернизации и технического перевооружения, а также для строительства, реконструкции, модернизации объектов капитального строительства.\n\n*ПСК «Оборотная»*\nКредит (или рефинансировать его) на сумму до 1 млрд рублей\nНа срок до 1 года (можно больше, но далее применяется коммерческая ставка банка).\nЦелью может являться что угодно, кроме многоквартирного жилищного строительства.\n\n[«ФОТ 3.0»](http://government.ru/support_measures/measure/150/)\nДля покрытия расходов по зарплате сотрудникам, обслуживания других кредитов доступна программа с суммой кредита до 300 млн рублей по ставке 3%.\nУсловие - сохранение численности 90% сотрудников.\n\n[Список участвующих в программе банков](https://corpmsp.ru/bankam/programma_stimulir/).\nПрограммы действуют до конца 2022 года.\nЗаёмщик не должен входить в группу с компаниями-представителями крупного бизнеса и должен быть внесён в реестр субъектов МСП.', parse_mode= 'Markdown', reply_markup = markup)

# пункты для работника
# Где написано 🔙 Другиe пункты в первом слове на конце английская e, чтобы пункты работодателя не отображались
    elif message.text == '🤺 Справка по отсрочке от армии':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        another_bulletpoints = types.KeyboardButton('🔙 Другиe пункты')
        markup.add(another_bulletpoints)

        bot.send_message(message.chat.id, 'Сотрудник должен иметь высшее образование и работать в аккретованных организациях > 1 года.\n\nТакже распространяется на специалистов со стажем менее 1 года, но при условии, что они окончили ВУЗ за год до момента своего назначения на должность.\n\nКомпании должны формировать и направлять через [Госуслуги](https://www.gosuslugi.ru) в Минцифры России списки работников, претендующих на отсрочку более чем за 50 дней до начала призывной компании.', parse_mode= 'Markdown' , reply_markup = markup)

    elif message.text == '💶 Получить льготную ипотеку':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
        item_1 = types.KeyboardButton('Более 1 млн. человек')
        item_2 = types.KeyboardButton('Менее 1 млн. человек')
        markup.add(item_1, item_2)

        bot.send_message(message.chat.id, '*Есть требования*:\nЗарплата должна быть выше 100 или 150 тыс. руб/месяц до вычета подоходного налога (порог зависит от населения города).\nВозраст - от 22 до 45 лет\n[Специалист работает в компании более 1 налогового периода](https://www.consultant.ru/document/cons_doc_LAW_19671/3fff7bb3e65ba62b2eb130a0c94e707c5996e4d1/)\n\nКакое население у вашего города?', parse_mode= 'Markdown', reply_markup = markup)

    elif message.text == 'Более 1 млн. человек': 
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
        if_fired = types.KeyboardButton('🗑 Если уволен?')
        another_bulletpoints = types.KeyboardButton('🔙 Другиe пункты')
        markup.add(if_fired, another_bulletpoints)

        bot.send_message(message.chat.id, 'Тогда требование по зарплате - 150 тыс. руб/мес и выше.\nЕсли это так, доступна сумма ипотеки до 18 млн. рублей\nСтавка - до 5% годовых.\nПервоначальный взнос - от 15% (можно включить мат. капитал).\nСрок - до 30 лет.\nМожно оформить до 31 декабря 2024 года.\n\n[Список участвующих в программе банков](https://www.banki.ru/products/hypothec/catalogue/ipoteka_dlya_it/).\n\n*На что можно взять ипотеку?*\nКвартиру в строящемся доме, в том числе по договору долевого участия\nГотовую квартиру от застройщика в новостройке\nЖилой дом от застройщика\nCтроительство жилого дома по договору подряда\nПокупку участка под строительство жилого дома по договору подряда.', parse_mode= 'Markdown', reply_markup = markup)

    elif message.text == 'Менее 1 млн. человек': 
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
        if_fired = types.KeyboardButton('🗑 Если уволен?')
        another_bulletpoints = types.KeyboardButton('🔙 Другиe пункты')
        markup.add(if_fired, another_bulletpoints)

        bot.send_message(message.chat.id, 'Тогда требование по зарплате - 100 тыс. руб/мес и выше.\nЕсли это так, доступна сумма ипотеки до 9 млн. рублей\nСтавка - до 5% годовых.\nПервоначальный взнос - от 15% (можно включить мат. капитал).\nСрок - до 30 лет.\nМожно оформить до 31 декабря 2024 года.\n\n[Список участвующих в программе банков](https://www.banki.ru/products/hypothec/catalogue/ipoteka_dlya_it/).\n\n*На что можно взять ипотеку?*\nКвартиру в строящемся доме, в том числе по договору долевого участия\nГотовую квартиру от застройщика в новостройке\nЖилой дом от застройщика\nCтроительство жилого дома по договору подряда\nПокупку участка под строительство жилого дома по договору подряда.', parse_mode= 'Markdown', reply_markup = markup)


    elif message.text == '🗑 Если уволен?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        another_bulletpoints = types.KeyboardButton('🔙 Другиe пункты')
        markup.add(another_bulletpoints)

        bot.send_message(message.chat.id, 'Ставка сохранится, если в течение 3 месяцев найти работу в другой IT-компании. Иначе ставка будет ключевой на день заключения договора + 2,5%, например, в июне 2022 ключевая ставка от ЦБ 11%, для уволившихся будет 13,5% (11+2,5).', reply_markup = markup)

    elif message.text == '🔙 Другиe пункты':
        employee_bulletpoints(message)

# общий
    elif message.text == '🔙 Назад':
        select_specialization(message)

    elif message.text == '🔙 Перевыбрать специализацию':
        back_to_select_specialization(message)

def employee_bulletpoints(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    item_1 = types.KeyboardButton('🤺Справка по отсрочке от армии')
    item_2 = types.KeyboardButton('💶 Получить льготную ипотеку')
    back_to_select_specialization = types.KeyboardButton('🔙 Перевыбрать специализацию')
    markup.add(item_1, item_2, back_to_select_specialization)

    bot.send_message(message.chat.id, 'Справку по какому пункту вы хотите получить?', reply_markup = markup)

def employer_bulletpoints(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    item_1 = types.KeyboardButton('💰 Льготные налоги')
    item_2 = types.KeyboardButton('🤺 Помочь сотруднику по отсрочке от армии')
    item_3 = types.KeyboardButton('💳 Льготы по кредитам')
    item_4 = types.KeyboardButton('➕ Остальные льготы')
    back_to_select_specialization = types.KeyboardButton('🔙 Перевыбрать специализацию')
    markup.add(item_1, item_2, item_3, item_4, back_to_select_specialization)

    bot.send_message(message.chat.id, 'Справку по какому пункту вы хотите получить?', reply_markup = markup)

# выбор размера бизнеса в пункте работодателя
def credit_business_type(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    item_1 = types.KeyboardButton('▪️ Малый бизнес и самозанятые')
    item_2 = types.KeyboardButton('◾️ Средний бизнес')
    markup.add(item_1, item_2)

    bot.send_message(message.chat.id, 'Какой у вас бизнес?', reply_markup = markup)

def back_to_select_specialization(message):
    if message.text == '🔙 Перевыбрать специализацию':
        bot.delete_message(message.chat.id, message.message_id - 3)
        bot.delete_message(message.chat.id, message.message_id - 2)
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        select_specialization(message)

def none_stop():
    bot.polling(none_stop = True)

while True:
    try:
        none_stop()
    except:
        time.sleep(60)
