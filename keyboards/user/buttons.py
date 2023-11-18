# 0: Kazakh
# 1: English
# 2: Russian
# 3: Spanish
# 4: Polish
# 5: Azerbaijani
# 6: Turkish
# 7: Chinese
# 8: Tajik
# 9: Uzbek

def get_lang_id(lang):
    match(lang):
        case "kz":
            return 0
        case "en":
            return 1
        case "ru":
            return 2
        case "es":
            return 3
        case "pl":
            return 4
        case "az":
            return 5
        case "tr":
            return 6
        case "zh":
            return 7
        case "tg":
            return 8
        case "uz":
            return 9
        case _:
            return 1

languages = [
    "Kazakh", "English", "Russian",
    "Spanish", "Polish", "Azerbaijani",
    "Turkish", "Chinese", "Tajik",
    "Uzbek"
]

volunteer = [
    "Ерікті", "Volunteer", "Волонтер",
    "Spanish", "Polish", "Azerbaijani",
    "Turkish", "Chinese", "Tajik",
    "Uzbek"
]

consumer = [
    "Тұтынушы", "Consumer", "Потребитель",
    "Spanish", "Polish", "Azerbaijani",
    "Turkish", "Chinese", "Tajik",
    "Uzbek"
]

sendContact = [
    "Kazakh", "Send contact", "Russian",
    "Spanish", "Polish", "Azerbaijani",
    "Turkish", "Chinese", "Tajik",
    "Uzbek"
]

sendLocation = [
    "Kazakh", "Send location", "Russian",
    "Spanish", "Polish", "Azerbaijani",
    "Turkish", "Chinese", "Tajik",
    "Uzbek"
]
