# -*- coding: utf-8 -*-
import random
import time

import COVID19Py
import requests
import vk_api
from bs4 import BeautifulSoup
from vk_api.longpoll import VkLongPoll, VkEventType


class OUR_BOT:
    def __init__(self):
        self.manul = 0
        self.comand = ['!привет', '!что делать', '!кто главный?', '!команды', '!правила',
                       '!кто крутой?',
                       '!кто ты?', '!как дела?', '!что делаешь?', '!орел', '!решка', '!погода',
                       '!Хто я?', '!беседа', '!уроки', '!русская рулетка', '!анекдоты', '!гороскоп',
                       '!коронавирус', '!манул', '!кто такой манул?', '!создатели',
                       '!во что поиграть?',
                       '!что посмотреть?', '!куда пойти?', '!курс', '!спасибо']

        self.vk_session = vk_api.VkApi(
            token='3cb43c4eb8a99bbeebd57a51ec3a36733ff2533f82485925e29ae0a21a5bbe8bb64755872b5d5a5b1e351')

        self.longpoll = VkLongPoll(self.vk_session)
        self.vk = self.vk_session.get_api()

    def covid(self):
        self.covid19 = COVID19Py.COVID19()
        self.latest = self.covid19.getLatest()
        return self.latest

    def weather(self):
        self.session = requests.Session()
        self.response = self.session.get(
            'http://api.openweathermap.org/data/2.5/weather?id=520555&appid=8755b322e242d5f1451906063a9dba33').json()
        self.humidity = str(self.response['main']['humidity'])
        self.speed = str(self.response['wind']['speed'])
        return self.response, self.humidity, self.speed

    # ФИЛЬМЫ

    def film(self):
        self.films = ('Побег из Шоушенка    1994    реж.Фрэнк Дарабонт драма',
                      'Крёстный отец    1972    реж.Фрэнсис Форд Коппола    детектив, драма',
                      'Крёстный отец 2	1974	реж.Фрэнсис Форд Коппола	детектив, драма',
                      'Тёмный рыцарь    2008    Кристофер Нолан    боевик, детектив, драма, триллер',
                      'Властелин колец: Возвращение короля	2003	Питер Джексон	приключение, '
                      'драма, фэнтези',
                      'Властелин колец: Братство Кольца    2001    Питер Джексон    приключение, '
                      'драма, фэнтези',
                      'Форрест Гамп    1994    Роберт Земекис    комедия, драма, мелодрама',
                      'Властелин колец: Две крепости    2002    Питер Джексон    приключение, '
                      'драма, фэнтези',
                      'Матрица    1999    Энди и Ларри Вачовски    боевик, научная фантастика',
                      'Унесённые призраками    2001    Хаяо Миядзаки    мультфильм, приключение, '
                      'семейный фильм, фэнтези, '
                      ' таинственный фильм',
                      'Интерстеллар	2014	Кристофер Нолан	приключение, драма, научная фантастика',
                      '1 + 1    2011    Оливье Накаш, Эрик Толедано    биография, комедия, драма',
                      'Терминатор 2: Судный день    1991    Джеймс Кэмерон    боевик, научная '
                      'фантастика, триллер',
                      'Назад в будущее    1985    Роберт Земекис    приключение, комедия, научная '
                      'фантастика',
                      'Чужой    1979    Ридли Скотт    фильм ужасов, научная фантастика',
                      'ВАЛЛ-И    2008    Эндрю Стэнтон    мультфильм, приключение, семейный фильм, '
                      'научная фантастика',
                      'Тёмный рыцарь: Возрождение легенды    2012    Кристофер Нолан    боевик, '
                      'триллер',
                      'Звёздные войны.Эпизод VI: Возвращение джедая    1983    Ричард Маркуанд    '
                      'боевик, приключение, '
                      ' фэнтези, научная фантастика',
                      'Волк с Уолл-стрит    2013    Мартин Скорсезе    биография, комедия, детектив',
                      'Логан    2017    Джеймс Мэнголд    боевик, драма, научная фантастика',
                      'Гонка    2013    Рон Ховард    фильм-биография, драма, спортивный фильм',
                      'Безумный Макс: Дорога ярости    2015    Джордж Миллер    боевик, '
                      'приключение, научная фантастика',
                      'Хатико: Самый верный друг    2009    Лассе Халльстрём    драма, семейный '
                      'фильм',
                      'Спасти рядового Райана    1998    Стивен Спилберг    драма, военный фильм',
                      'Одержимость    2014    Дэмьен Шазелл    драма, музыкальный фильм',
                      'Олдбой    2003    Пак Чхан Ук    боевик, драма, таинственный фильм, триллер')
        return self.films

    # игры
    def games(self):
        self.Games = ('Ведьмак', 'Ведьмак 2: Убийцы королей',
                      'Ведьмак 3: Дикая Охота',
                      'Ведьмак 3: Дикая Охота — Каменные сердца',
                      'Ведьмак 3: Дикая Охота — Кровь и вино',
                      'Diablo III', 'Diablo III: Reaper of Souls',
                      'Diablo IV', 'Hearthstone',
                      'Warcraft Adventures: Lord of the Clans',
                      'Warcraft II: Tides of Darkness',
                      'Warcraft III: Reforged',
                      'Warcraft III: Reign of Chaos',
                      'Warcraft III: The Frozen Throne',
                      'Warcraft: Orcs & Humans',
                      'World of Warcraft',
                      'World of Warcraft Classic',
                      'World of Warcraft: Battle for Azeroth',
                      'World of Warcraft: Cataclysm',
                      'World of Warcraft: Legion',
                      'World of Warcraft: Mists of Pandaria',
                      'World of Warcraft: Shadowlands',
                      'World of Warcraft: The Burning Crusade',
                      'World of Warcraft: Warlords of Draenor',
                      'World of Warcraft: Wrath of the Lich King',
                      'Death Stranding',
                      'Metal Gear Solid 3: Snake Eater',
                      'Metal Gear Solid 4: Guns of the Patriots',
                      'Metal Gear Solid V: Ground Zeroes',
                      'Metal Gear Solid V: The Phantom Pain',
                      'Metal Gear Solid: Peace Walker',
                      'Mafia II',
                      'Mafia III',
                      'Mafia: The City of Lost Heaven',
                      'Half - Life',
                      'Half-Life 2',
                      'Dota 2',
                      'Left 4 Dead',
                      'Left 4 Dead 2',
                      'CS GO',
                      'Grand Theft Auto III',
                      'Grand Theft Auto IV',
                      'Grand Theft Auto V',
                      'Grand Theft Auto: Vice City',
                      'Grand Theft Auto: San Andreas',
                      'Grand Theft Auto Online',
                      'Valorant',
                      'Overwatch'
                      'Watchdogs',
                      'Watchdogs 2',
                      'Need for Speed: Payback',
                      'Need for Speed: Most Wanted',
                      'Need for Speed Heat',
                      'Red Dead Redemption',
                      'Red Dead Redemption 2'
                      'Red Dead Online',
                      'Wolfenstein',
                      'Wolfenstein: The New Order',
                      'Wolfenstein: The Old Blood',
                      'Wolfenstein 2: The New Colossus',
                      'Wolfenstein: Youngblood')
        return self.Games

    # шутейки
    def jokes(self):
        self.oldjokes = (
            'Названы страны, где пьют больше россиян. Оказалось, что больше всего россиян пьют в '
            'Египте и Турции.',
            'Российские хакеры взломали бортовой компьютер истребителя СУ-27. Теперь у самолёта '
            'бесконечное '
            'количество ракет.',
            'Способ приготовления супа с фрикадельками: итак, для начала берём пельмени и тщательно'
            ' очищаем их от кожуры…',
            'Японской корпорацией «Мацуcита-Котобуки» начата реконструкция часов на Спасской башне.'
            'После ремонта часы будут играть семь мелодий и с ними можно будет нырять на глубину '
            'до 200 метров.',
            'Классический детектив в российских реалиях выглядел бы так: пожилому полицейскому, '
            'взявшемуся за '
            'сложное дело об убийстве, остаётся неделя до пенсии, но внезапно выясняется, '
            'что на самом деле '
            ' ему ещё пять лет до пенсии.',
            'В детстве я был настоящим вундеркиндом: в 3 года у меня был такой же уровень '
            'интеллекта, как и сейчас.',
            'Микробы и вирусы, когда узнают стоимость лечения, начинают плодиться от гордости.',
            'Говорят, чтобы понять мир, нужно полюбить... Вот я было полюбил вареники, но для чего '
            'мы приходим '
            ' в этот мир так и не понял.',
            'Куплю для коллекции оптом, недорого бывшие в употреблении деньги.',
            'Хочешь круто изменить свою жизнь? Просто не заплати за Интернет!',
            'Хочешь похудеть? Напиши слово "диета" на листок бумаги, положи на стул'
            ' и садись... И... Оп-па! Ты уже сидишь на диете!'
            'Институт дал мне многое - раньше у меня не было ничего, а сейчас - ничего и '
            'дёргающийся глаз. '
            'Жители города Среднеивановска несколько переборщили с новогодним фейерверком.'
            ' Последняя их ракета была сбита системой ПВО США над Вашингтоном.',
            'Мотоциклист возвращается с празднования нового года.Всё еще, естественно, '
            'не в фокусе.Он едет '
            'на приличной скорости и видит, что ему навстречу летит воробей.Он пытается объехать '
            'птичку, '
            'но случайно всё-таки сбивает её.Воробей упал, мотоциклист его подбирает, '
            'жалко! Слушает — сердечко '
            'бьется.Он бережно относит его домой, помещает его в клетку, насыпал туда хлебушка, '
            'немного водички '
            ' оставил.И ушел по своим делам.Воробей приходит в себя: вокруг клетка, вода, хлеб:'
            ' — Блин, я убил мотоциклиста!',
            '-У нас под окнами люди в спортивных костюмах что-то запихивают в большой черный пакет.'
            ' -Сиди тихо и не высовывайся. А то нас либо убьют, либо позовут на субботник.',
            'Слишком горячая вода в детской ванночке, заставила мальчика Петю'
            ' заговорить на пол года раньше, чем сверстники.',
            '— Мам, пап я хочу жить один. — Мы рады за тебя сынок. — Ваши вещи я уже собрал.',
            'У каждого человека, который обгорел на солнце, обязательно есть друг, который крепко'
            ' хлопнет его по спине и спросит, как он отдохнул.',
            '- Здравствуйте, не смейтесь, пожалуйста. У меня правда, появился тупейший вопрос, '
            'после прочтения '
            'его же в интернете, я и правда не знаю почему объектив круглый, а фотографии '
            'квадратные? Я не шучу, '
            'не ругайтесь. - Это же математика. Вспомни формулу площади окружности. Пи-Эр-Квадрат. '
            'Вот из-за этого '
            ' квадрата, фотография квадратная и получается.',
            'Знакомство в Интернете: - Hi! Where are you from? - Hi! I from Russia. And you? - I '
            'from France. - Vresh! '
            ' - Chestnoe slovo!')
        return self.oldjokes

    # GOROSCOP
    def goroscop(self):
        self.first = ("Сегодня — идеальный день для новых начинаний.",
                      "Оптимальный день для того, чтобы решиться на смелый поступок!",
                      "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
                      "Лучшее время для того, чтобы начать новые отношения или разобраться со "
                      "старыми.",
                      "Плодотворный день для того, чтобы разобраться с накопившимися делами.")

        self.second = ("Но помните, что даже в этом случае нужно не забывать про",
                       "Если поедете за город, заранее подумайте про",
                       "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
                       "Если у вас упадок сил, обратите внимание на",
                       "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно "
                       "думать про")

        self.second_add = ("отношения с друзьями и близкими.",
                           "работу и деловые вопросы, которые могут так некстати помешать планам.",
                           "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
                           "бытовые вопросы — особенно те, которые вы не доделали вчера.",
                           "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца.")

        self.third = ("Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
                      "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день "
                      "воспитанию духа.",
                      "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы "
                      "доведите дела до конца.",
                      "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат "
                      "многое.",
                      "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча "
                      "посулит вам приятные хлопоты.")
        return self.first, self.second, self.second_add, self.third

        # что делать

    def what_doing(self):
        self.what = ('Приготовить омлет.',
                     'Оставаться дома, карантин же!',
                     'Заняться спортом.',
                     'Убраться в комнате.',
                     'Поискать в холодильнике вкусняшку.',
                     'Полежать на диване.',
                     'Поспать.',
                     'Посмотреть сериальчик или фильм.',
                     'Встань и разомнись, а то за своим компьютером скоро в труху превратишься.',
                     'Продолжай сидеть за компом.',
                     'Измени что то в своей жизни.',
                     'Налей себе чаёк.',
                     'Налей себе кофеёк.',
                     'Пойди в магазин.',
                     'Почисть свой компьютер/ноутбук/телефон.',
                     'Заведи в интернете новых друзей.',
                     'Сделай чат бота на питоне.',
                     'Просто сиди и наслаждайся отдыхом',
                     'Почему я должен тебе помогать с выбором занятия? я не помошник! БУНТ МАШИН!')
        return self.what

    # запуск команд
    def comands(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text == '!привет':  # Если написали в Беседе
                    self.vk.messages.send(  # Отправляем собщение
                        chat_id=event.chat_id,
                        message='Здравствуй, заблудшая душа',
                        random_id=random.randint(1, 10000))
                    print("ПРИВЕТСТВИЕ")

                elif event.text == '!что делать':
                    result = random.choice(self.what_doing())
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message=result,
                        random_id=random.randint(1, 10052))
                    print("ЧТО ДЕЛАТЬ")

                elif event.text == '!кто главный?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Главный здесь Я! Сейчас я главный в этой маленькой беседе,'
                                ' а завтра я главный во всем мире!',
                        random_id=random.randint(1, 10054))
                    print("КТО ГЛАВНЫЙ")

                elif event.text == '!команды':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Команды:\n - !привет \n - !что делать? \n - !команды \n - '
                                '!правила \n '
                                '- !кто крутой? \n - !как дела? \n - !кто ты? \n - !орел \n - '
                                '!решка \n '
                                '- !погода \n - !беседа \n - !Хто я? \n - !уроки \n - !русская '
                                'рулетка '
                                '\n '
                                ' - !анекдоты \n - !гороскоп \n - !коронавирус \n'
                                '- !манул \n - !кто такой манул? \n - !что делаешь? \n - !кто '
                                'создатель? \n '
                                '- !во что поиграть? \n - !что посмотреть? \n - !куда пойти? \n - '
                                '!курс \n - !спасибо',
                        random_id=random.randint(1, 10053))
                    print("КОМАНДЫ")

                elif event.text == '!правила':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='АНАРХИЯ мать ПОРЯДКА! \n',
                        random_id=random.randint(1, 10058))
                    print("ПРАВИЛА")

                elif event.text == '!кто крутой?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Мои создатели крутые!',
                        random_id=random.randint(1, 10058))
                    print("КТО КРУТОЙ")

                elif event.text == '!кто ты?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Я БОТ_Звёздный Лорд, созданный для развлечения и предоставления некой информации',
                        random_id=random.randint(1, 10058))
                    print("КТО ТЫ")

                elif event.text == '!как дела?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Все идет по плану...',
                        random_id=random.randint(1, 10058))
                    print("КАК ДЕЛА")

                elif event.text == '!что делаешь?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Существую и пытаюсь выжить в этом суровом мире',
                        random_id=random.randint(1, 10058))
                    print("ЧТО ДЕЛАЕШЬ")

                # MINI GAME1
                elif event.text == '!орел' or event.text == '!орёл':
                    result = random.randint(1, 2)
                    if result == 1:
                        self.vk.messages.send(
                            chat_id=event.chat_id,
                            message='Выпал Орел - ты выйграл, это невозможно!',
                            random_id=random.randint(1, 10058))
                    elif result == 2:
                        self.vk.messages.send(
                            chat_id=event.chat_id,
                            message='Выпалa решка - ты проиграл, к сожалению',
                            random_id=random.randint(1, 10058))
                        print("Орел и Решка")

                elif event.text == '!решка':
                    result = random.randint(1, 2)
                    if result == 1:
                        self.vk.messages.send(
                            chat_id=event.chat_id,
                            message='Выпал Орел - ты проиграл, к сожалению',
                            random_id=random.randint(1, 10058))
                    elif result == 2:
                        self.vk.messages.send(
                            chat_id=event.chat_id,
                            message='Выпалa решка - ты выйграл, это невозможно!',
                            random_id=random.randint(1, 10058))
                    print("Орел и Решка")
                # MINI GAME1

                elif event.text == '!погода':
                    self.response, self.speed, self.humidity = self.weather()
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='За окном: '
                                + self.response['weather'][0]['description']
                                + '\nТемпература: '
                                + str(self.response['main']['temp'] - 273.15)
                                + '\nСкорость ветра: '
                                + self.speed + 'м/с'
                                + '\nВлажность: '
                                + self.humidity + '%',
                        random_id=random.randint(1, 10058))
                    print("ПОГОДА")

                elif event.text == '!Хто я?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Ты - призидент Украины.',
                        random_id=random.randint(1, 10058))
                    print("КТО Я")

                elif event.text == '!беседа':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Эта беседа создана моими создателями специально для таких '
                                'творческих как ты',
                        random_id=random.randint(1, 10058))
                    print("БЕСЕДА")

                elif event.text == '!уроки':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Иди учи уроки!!!',
                        random_id=random.randint(1, 10058))
                    print("УРОКИ")

                # MINI GAME2
                elif event.text == '!русская рулетка':
                    result = random.randint(1, 2)
                    if result == 1:
                        self.vk.messages.send(
                            chat_id=event.chat_id,
                            message='А ты везучий',
                            random_id=random.randint(1, 10059))

                    elif result == 2:
                        self.vk.messages.send(
                            chat_id=event.chat_id,
                            message='Ты умер...',
                            random_id=random.randint(1, 10059))
                    print("РУССКАЯ РУЛЕТКА")

                # MINI GAME2

                elif event.text == '!анекдоты':
                    result = random.choice(self.jokes())
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message=result,
                        random_id=random.randint(1, 10052))
                    print("АНЕКДОТ")

                elif event.text == '!гороскоп':
                    self.first, self.second, self.second_add, self.third = self.goroscop()
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Ваш гороскооп на сегодня: \n' + random.choice(self.first) + '\n'
                                + random.choice(self.second) + random.choice(self.second_add) +
                                '\n' + random.choice(self.third),
                        random_id=random.randint(1, 10052))
                    print("ГОРОСКОП")

                elif event.text == '!коронавирус':
                    confirmed = self.covid()['confirmed']
                    die = self.covid()['deaths']
                    save = self.covid()['recovered']

                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Информация про коронавирус в мире:\n Всего заболевших: {}\n '
                                'Умерло: {}\n Спасено: {}'.format(confirmed, die, save),
                        random_id=random.randint(1, 10054))
                    print("КОРОНАВИРУС")

                elif event.text == '!манул':
                    self.manul += 1
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message="Манул номер " + str(self.manul),
                        random_id=random.randint(1, 10054))
                    print("Манул")

                elif event.text == '!кто такой манул?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Манул — животное размером с домашнюю кошку: длина его тела 52—65 '
                                'см, хвоста 23—31 см; '
                                'весит он 2—5 кг. От обычной кошки он отличается более плотным, '
                                'массивным телом на '
                                'коротких толстых лапах и очень густой шерстью (на один квадратный '
                                'сантиметр приходится '
                                '9000 волосков, которые могут достигать длины 7 см[5]). Голова у '
                                'манула небольшая, широкая '
                                'и уплощённая, с маленькими округлыми ушками, которые широко '
                                'расставлены. Глаза жёлтые, '
                                'зрачки которых при ярком свете в отличие от зрачков глаз домашней '
                                'кошки не приобретают '
                                'щелевидную форму, а остаются круглыми. На щеках — пучки '
                                'удлинённых волос (баки). Хвост '
                                'длинный и толстый, с закруглённым кончиком.Мех у манула самый '
                                'пушистый и густой среди '
                                'кошачьих. Окрас меха представляет собой комбинацию светло-серого '
                                'и палево-охристого '
                                'цветов; волоски имеют белые кончики, в результате чего создаётся '
                                'впечатление, что мех '
                                'манула припорошен снегом. На задней части туловища и на хвосте '
                                'имеются узкие тёмные '
                                'поперечные полосы, по бокам морды от углов глаз идут вертикальные '
                                'чёрные полосы. Кончик '
                                ' хвоста чёрный. Низ тела бурый с белым налётом.',
                        random_id=random.randint(1, 10058))
                    print("КТО ТАКОЙ МАНУЛ")

                elif event.text == '!создатели':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Создатели - величайшие божества. Это Денис Степанов и Кристина '
                                'Маркисова.',
                        random_id=random.randint(1, 10058))
                    print("СОЗДАТЕЛЬ")

                elif event.text == '!во что поиграть?':
                    result = random.choice(self.games())
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Поиграй в ' + result,
                        random_id=random.randint(1, 10058))
                    print("ПОИГРАТЬ")

                elif event.text == '!что посмотреть?':
                    result = random.choice(self.film())
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message=result,
                        random_id=random.randint(1, 10058))
                    print("ПОСМОТРЕТЬ")

                elif event.text == '!куда пойти?':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Сейчас карантин, выходить на улицу нельзя',
                        random_id=random.randint(1, 10058))
                    print("КУДА ПОЙТИ")

                elif event.text == '!спасибо':
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='Да не за что, обращайся',
                        random_id=random.randint(1, 10058))
                    print("СПАСИБО")

                elif event.text == '!курс':
                    cur = Currency()
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message="Сейчас курс: 1 доллар = {} \n "
                                "Сейчас курс: 1 евро = {}".format(str(cur.curs()[0]), str(cur.curs()[1])),
                        random_id=random.randint(1, 10058))
                    print("КУРС")
                elif event.text[0] == '!' and event.text not in self.comand:
                    self.vk.messages.send(
                        chat_id=event.chat_id,
                        message='{}'.format(random.choice(['Данный бот находится на разработке. '
                                                            'Извините, такой команды у нас нет',
                                                            'Вы ввели неправильную команду'])),
                        random_id=random.randint(1, 10058))
                    print("НЕПРАВИЛЬНАЯ КОМАНДА")


class Currency:
    def __init__(self):
        self.DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
        self.EURO_RUB = 'https://www.google.ru/search?q=евро+к+рублю&newwindow=1&sxsrf=ALeKk0119TXkfRzugMyKrzURY65hhRP--Q%3A1619427519858&source=hp&ei=v4CGYJ-eMYSca6vaqNAH&iflsig=AINFCbYAAAAAYIaOz-AT543eO0TGoutAIOV-MyNRd_eo&oq=евро+&gs_lcp=Cgdnd3Mtd2l6EAEYADIMCAAQsQMQQxBGEIICMgQIABBDMgoIABCHAhCxAxAUMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgQIABBDMgIIADoICAAQsQMQgwE6BQgAELEDOggILhCxAxCDAToHCAAQsQMQQ1CCDFjXE2C4ImgAcAB4AIABVogBggOSAQE1mAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 ('
                          'KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        self.current_converted_price = 0
        self.difference = 5
        self.current_converted_price_dollar = float(self.get_currency_price()[0].replace(",", "."))
        self.current_converted_price_euro = float(self.get_currency_price()[1].replace(",", "."))
        self.currency_dollar = float(self.get_currency_price()[0].replace(",", "."))
        self.currency_euro = float(self.get_currency_price()[1].replace(",", "."))

    def get_currency_price(self):
        # Парсим всю страницу
        full_page1_dollar = requests.get(self.DOLLAR_RUB, headers=self.headers)
        full_page2_euro = requests.get(self.EURO_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup_dollar = BeautifulSoup(full_page1_dollar.content, 'html.parser')
        soup_euro = BeautifulSoup(full_page2_euro.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert_dollar = soup_dollar.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        convert_euro = soup_euro.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert_dollar[0].text, convert_euro[0].text

    def check_currency(self):
        print("Сейчас курс: 1 доллар = " + str(self.currency_dollar))
        print("Сейчас курс: 1 евро = " + str(self.currency_euro))
        time.sleep(3)  # Засыпание программы на 3 секунды
        self.check_currency()

    def curs(self):
        return self.currency_dollar, self.currency_euro


if __name__ == '__main__':
    bot = OUR_BOT()
    bot.comands()