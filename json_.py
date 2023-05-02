import json

with open("config/trigger.json", encoding='UTF-8') as f:
    triggers_json = json.load(f)

    for trigger in triggers_json:
        triggers = []

        for data in triggers_json[trigger]["trigger"]:
                triggers.append((data["coordinates"], data["pixels"]))

        сompleted_trigger = 1

        for data in triggers:
            print(trigger, 'pixel', data[0], 'coord', data[1], triggers_json[trigger]["func"])
            if False:
                сompleted_trigger = 0

        if сompleted_trigger == 1:
            pass

            #return trigger,


funcs = 'func'


print(type([]), type(()))



print(2)

json2 = {
    100: {
        "trigger": [
            {
                "coordinates": [40, 790]
                , "pixels": [
                [255, 255, 255]
            ]
                , "comment_rus": "Облоко эмодзи"
            },
            {
                "coordinates": [529, 950]
                , "pixels": [
                [7, 71, 144],
                [7, 71, 143],
                [7, 71, 142],
            ]
                , "comment_rus": "Низ экрана боя"
            },
        ]
        , "func": ["self._getElixir", "self._getCardsInBatlle"]
        , "comment": "Триггер нахождения в меню боя"
    }
    , 121: {
        "trigger": [
            {
                "coordinates": [40, 790]
                , "pixels": [
                [255, 255, 255]
            ]
                , "comment_rus": "Облоко эмодзи"
            },
            {
                "coordinates": [300, 840]
                , "pixels": [
                [104, 187, 255],
            ]
                , "comment_rus": "Экран результата боя"
            }
        ]
        , "func": ["self._getNumeberCrown"]
        , "comment_rus": "Выход из меню игры 2Х2"
    }
    , 122: {
        "trigger": [
            {
                "coordinates": [40, 790]
                , "pixels": [
                [255, 255, 255]
            ]
                , "comment_rus": "Облоко эмодзи"
            },
            {
                "coordinates": (526, 951)
                , "pixels": [
                [52, 66, 83],
            ]
                , "comment_rus": "Экран результата боя"
            },
        ]
        , "func": ["self._getNumeberCrown"]
        , "comment_rus": "Выход из меню игры 2Х2"
    }
    ,

    404: {
        "trigger": [
            {
                "coordinates": [40, 790]
                , "pixels": [
                (255, 255, 255)
            ]
                , "comment_rus": "Облоко эмодзи"
            },
            {
                "coordinates": (529, 950)
                , "pixels": [
                [7, 71, 144],
            ]
                , "comment_rus": "Низ экрана боя"
            },
        ]
        , "func": []
        , "comment": "Триггер нахождения в меню боя"
    }
}

'''for i in json2:
    print(i, json2[i]["trigger"])
    for j in json2[i]["trigger"]:
        print(j)
        print(j["coordinates"])
        print(j["pixels"])'''
