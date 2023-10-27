
from src.config import config
from src.utils.fuzzy_filters import check_text_for_keywords


def test_fuzzy_searcher():
    MESSAGES = ["Я хочу поменять рубли на баты",
                "Где можно обменять деньги?",
                "Нужны баты с доставкой",
                "Я хочу обменять валюту",
                "Куплю баты за рубли",
                "Мне нужна информация об обменнике крипты",
                "Я хочу обналичить рубли",
                "Можно ли получить наличку?",
                "Предложения по обмену в личку",
                "Мне нужны баты, предложения в лс",
                "Можете привезти наличку?",
                "Я готов поменять деньги",
                "Я хочу поменять рубли на баты и ˛получить наличку",
                "Где можно обменять деньги и купить баты?",
                "Нужны баты с доставкой в течение дня",
                "Я хочу обменять валюту наличными",
                "Куплю баты за рубли по выгодному курсу",
                "Мне нужна информация об обменнике крипты и возможности обмена usdt",
                "Я хочу обналичить рубли с карты и получить наличные баты",
                "Можно ли получить наличку в обмен на рубли?",
                "Предложения по обмену в личку или личные сообщения",
                "Мне нужны баты, предложения в лс или личные сообщения",
                "Можете привезти наличку в удобное для меня время?",
                "Я готов поменять деньги наличными или через Qr-код",
                "Где можно обменять рубли на баты в Москве?",
                "Нужны баты с доставкой в другой город",
                "Я хочу обменять валюту наличными в банке",
                "Куплю баты за рубли по текущему курсу",
                "Мне нужна информация об обменнике крипты и возможности обмена usdt на баты",
                "Я хочу обналичить рубли с карты и получить наличные баты в ближайшем отделении банка",
                "Можно ли получить наличку в обмен на рубли без комиссии?",
                "Предложения по обмену в личку или личные сообщения с подробностями",
                "Мне нужны баты, предложения в лс или личные сообщения с информацией о курсе обмена",
                "Можете привезти наличку в удобное для меня время и место?",
                "Я готов поменять деньги наличными или через Qr-код в любом банке",
                "Где можно обменять рубли на баты в Санкт-Петербурге?",
                "Нужны баты с доставкой в другую страну",
                "Я хочу обменять валюту наличными в обменном пункте",
                "Куплю баты за рубли по самому выгодному курсу",
                "Мне нужна информация об обменнике крипты и возможности обмена usdt на баты с минимальной комиссией",
                "Я хочу обналичить рубли с карты и получить наличные баты в банкомате",
                "Можно ли получить наличку в обмен на рубли без ограничений по сумме?",
                "Предложения по обмену в личку или личные сообщения с указанием времени и места встречи",
                "Мне нужны баты, предложения в лс или личные сообщения с подробной информацией о курсе обмена и комиссии",
                "Можете привезти наличку в удобное для меня время и место, например, в офисе",
                "Я готов поменять деньги наличными или через Qr-код в любом банке в пределах города",

                "Где можно обменять рубли на баты в Казани?",
                "Нужны баты с доставкой в другую страну в течение недели",
                "Я хочу обменять валюту наличными в обменном пункте на вокзале",
                "Куплю баты за рубли по самому выгодному курсу с возможностью получения наличных в любом отделении банка",
                "Мне нужна информация об обменнике крипты и возможности обмена usdt на баты с минимальной комиссией и быстрой обработкой заявки",
                "Я хочу обналичить рубли с карты и получить наличные баты в банкомате с возможностью выбора купюр",
                "Можно ли получить наличку в обмен на рубли без ограничений по сумме и без дополнительных комиссий?",
                "Предложения по обмену в личку или личные сообщения с указанием времени и места встречи в центре города",
                "Мне нужны баты, предложения в лс или личные сообщения с подробной информацией о курсе обмена и комиссии, а также с фотографией паспорта для идентификации",
                "Можете привезти наличку в удобное для меня время и место, например, в офисе или кафе",
                "Я готов поменять деньги наличными или через Qr-код в любом банке в пределах города с возможностью получения квитанции о сделке",
                "-----------", "Когда я был маленьким, я мечтал стать астронавтом",
                "Можете рассказать мне о вашем любимом фильме?",
                "Вчера я видел замечательный закат над океаном",
                "Какой цвет травы?", "Когда я был маленьким, я - usdt мечтал стать астронавтом,Можете рассказать мне о вашем любимом фильме? Вчера я видел замечательный закат над океаном, Какой цвет травы"
                ]

    for message in MESSAGES:
        is_pass = check_text_for_keywords(message, config.keywords, 30)
        print(f"{is_pass}: {message}\n")


def test():
    test_fuzzy_searcher()