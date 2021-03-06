import os

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()


token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)
questions_offline = {
        1:[
            'Как перевестись на другое направление',
            'Обратиться на факультет, в который планируется перевод, написать заявление на перевод, далее уточнить у куратора'
            ],
        2:[
            'Как получить справку об обучении?',
            'Обратиться в деканат, срок подготовки 3 рабочих дня'
            ],
        3:[
            'Как получить ведомость на пересдачу (очное обучение)?',
            'Договориться с преподавателем в день пересдачи, затем взять ведомость в деканате'
            ],
        4:[
            'Как оплатит обучение/где получить квитанцию?',
            'В финансовом отделе, адрес: Измайловский вал, дом 2, кабинет на лестнице между 4 и 5 этажом'
            ],
        5:[
            'Где смотреть расписание занятий/расписание преподавателей?',
            'На сайте synergy.ru, раздел Студентам, Расписние, ввести свою группу или переключив на преподавателя, ввести ФИО преподавателя.'
            ],
        6:[
            'Где находится мой деканат?',
            'Деканат Факультета Информационных технологий расположен в корпусе Семёновская, 402 кабинет'
            ],
        7:[
            'Как я могу отчислиться?',
            'Прийти в деканат и написать заявление на отчисление у куратора'
            ],
        8:[
            'Как записаться на пересдачу преподавателю через личный кабинет?',
            'Нажать кнопку запросить пересдачу в личном кабинете'
            ],
        9:[
            'Сколько попыток дается для пересдачи?',
            'Пересдать дисциплину можно не более 3-х раз.'
            ],
        10:[
            'Как происходит назначение научного руководителя диплома?',
            ('Узнать, сможет ли он Вас принять (есть ограничения по количеству студентов); \n'
            'Подойти к нему с концепцией темы диплома, после согласования написать заявление об утверждении темы.')
            ],
        11:[
            'Что нужно для получения справки-приложения № 2 для предоставления отсрочки и где ее можно получить?',
            ('Справку-приложение № 2 Вы можете получить в военно-учетном отделе на Соколе по адресу: \n'
            'м. Сокол, Ленинградский пр-т, дом 80 корп. Е, 3 этаж, каб. 304е (график: пн.-чт с 10:00 до 17:00).\n \nДля оформления справки необходимо предоставить копии документов: \n'
            '1. Документ о предыдущем образовании; \n2. Приписное удостоверение; \n3. Паспорт (Титульная страница с общей информацией + регистрация)')
            ],
        12:[
            'Как восстановиться на защиту диплома и в течение какого времени это возможно? ',
            'Если Вы освоили полностью учебный план, но не смогли пройти процедуру защиты ВКР, то Вы можете восстановиться на защиту ВКР через год с момента отчисления и не позднее 5-ти лет после отчисления, обратившись в приёмную комиссию.'
            ],
        }

questions_online = {
        1:[
            'Где находится деканат?',
            'Деканат Факультета Информационных технологий расположен в корпусе Семёновская, 402 кабинет'
            ],
        2:[
            'Обязательна ли идентификация при прохождении тестирования если нет веб-камеры?',
            'Идентификация с помощью камеры обязательна, зачесть предмет возможно только при её прохождении.'
            ],
        3:[
            'Я не понимаю как учиться',
            'Вы можете ознакомиться с инструкцией в личном кабинете. Для этого нажмите на свои ФИО в правом верхнем углу - Инструкция. Так же Вы можете обратиться к своему куратору во вкладке "Обратиться в деканат"'
            ],
        4:[
            'Как мне связаться с куратором?',
            'В личном кабинете, нажав кнопку обратиться в деканат. Куратор ответит Вам в течение 3 рабочих дней'
            ],
        5:[
            'Я обновил контактные данные (поменял номер телефона, паспорт, место прописки и пр.), как мне оповестить деканат?',
            'В личном кабинете, с помощью кнопки обратиться в деканат Вы пишите письмо и указываете контакты'
            ],
        6:[
            'Я не сдал экзамены, меня отчислят?',
            'В течение 1 месяца после образования академической задолженности её необходимо ликвидировать, далее на усмотрение деканата возможно изменение срока во избежание отчисления'
            ],
        7:[
            'Как открыть пересдачу?',
            'Вам необходимо зайти в дисциплину, которую планируете пересдавать и нажать на кнопку "Запросить пересдачу", которая находится под итоговым мероприятием(внизу страницы)'
            ],
        8:[
            'Как получить справку об обучении/ студенческий билет?',
            'В личном кабинете, нажав кнопку обратиться в деканат. Для справки необходимо название организации (по требованию справки не выдаются), для студенческого необходимо предоставить фото 3х4 в деканат'
            ],
        9:[
            'Как можно получить экземпляр договора об обучении?',
            'В личном кабинете, нажав "Обратиться в деканат", указав полный адрес для отправки.'
            ],
        10:[
            'Я хочу забрать документ о предыдущем образовании,как это сделать?',
            'Написать своему куратору в личном кабинете, он закажет данный документ в архиве. Дальнейшие действия будут пояснены исходя из способа получения документа'
            ],
        11:[
            'Предоставляет ли Университет места для прохождения практик?',
            'Нет, организацию для прохождения практики студент ищет самостоятельно, так же можно пройти практику по месту работы, если оно соответствует направлению, на котором Вы обучаетесь.'
            ],
        12:[
            'Как узнать сколько платить за обучение в новом семестре?',
            'Отправить запрос на электронную почту do@synergy.ru с пометкой "в Финансовый отдел"  (не куратор) или по телефону 8-495-280-12-66'
            ],
        13:[
            'Где мне выбрать тему дипломной работы?',
            'В личном кабинете, в предсеместровом семестре. Предмет "Информация по выпуску"'
            ],
        14:[
            'Как долго отвечает научный руководитель?',
            '5-7 рабочих дней, при отсутствии ответа, пишете в личном кабинете куратору (обратиться в деканат)'
            ],
        15:[
            'В течение какого времени готовится диплом об окончании Университета Синергия?',
            'Диплом готовится в течение 1.5 месяцев, по готовности Вам придёт оповещение '
            ],
        16:[
            'Как я могу оформить академический отпуск и на какой срок?',
            'В личном кабинете, нажав кнопку обратиться в деканат, куратор вышлем Вам необходимый бланк заявления. Срок академического отпуска 1 год'
            ],
        17:[
            'Можно ли продлить Академический отпуск?',
            'Да. Академический отпуск может быть продлён, нажав кнопку обратиться в деканат, Вы получите от куратора бланк заявления'
            ],
        18:[
            'Можно ли продлить Академический отпуск?',
            'Написав заявление, нажав кнопку обратиться в деканат'
            ],
        19:[
            'Можно ли сдавать дисциплины, находясь в Академическом отпуске?',
            'Нет. Доступ к обучению будет приостановлен.'
            ],
        20:[
            'Что нужно для того, чтобы отчислиться из ВУЗа, находясь в Академическом отпуске?',
            'Написать заявление об отчислении по собственному желанию с указанием причины отчисления, воспользовавшись кнопкной "обратиться в деканат"'
            ],
        21:[
            'Сохранятся ли сданные академические дисциплины после выхода из академического отпуска?',
            'Да, сданные предметы сохранятся. Но возможны изменения, уточняйте у куратора'
            ],
        22:[
            'Из Академического отпуска я выйду на тот же семестр?',
            'Да'
            ],
        }

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard_start = types.ReplyKeyboardMarkup()
    button_ofline = types.KeyboardButton('Оффлайн обучение')
    button_online = types.KeyboardButton('Онлайн обучение')
    keyboard_start.row(button_ofline)
    keyboard_start.row(button_online)
    bot.send_message(message.chat.id, 'Выберите форму обучения, а после номер вопроса ответ на который хотите получить.', reply_markup=keyboard_start)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Оффлайн обучение':
        for count in range(1, len(questions_offline)+1):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text=f'Ответ на вопрос {count}', callback_data=str(count) + ' ' + 'offline'))
            bot.send_message(message.chat.id, f"Вопрос: {count}. " + "\n" + "Форма обучения: offline" + "\n" + questions_offline[count][0], reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Если вы не нашли ответа на свой вопрос, то обратитесь непосредственно в деканат.')

    elif message.text == 'Онлайн обучение':
        for count in range(1, len(questions_online)+1):
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text=f'Ответ на вопрос {count}', callback_data=str(count) + ' ' + 'online'))
            bot.send_message(message.chat.id, f"Вопрос: {count}. " + "\n" + "Форма обучения: online" + "\n" +  questions_online[count][0], reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Если вы не нашли ответа на свой вопрос, то обратитесь непосредственно в деканат.')
    else:
        bot.send_message(message.chat.id, 'Напишите "/start", выберите форму обучения, а после номер вопроса ответ на который хотите получить.')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    split = call.data.split()
    if split[1] == 'online':
        bot.send_message(call.message.chat.id, f"Вопрос: {split[0]} \nФорма обучения: {split[1]} \nОтвет:\n " + questions_online[int(split[0])][1])
    else:
        bot.send_message(call.message.chat.id, f'Вопрос: {split[0]} \nФорма обучения: {split[1]} \nОтвет:\n ' + questions_offline[int(split[0])][1])


bot.polling()
