import time
import random
start1=input("start?")
masti=["♡","♢","♣","♠"]
karti=["1","2","3","4","5","6","7","8","9","10",]
if start1 == "start ":
    print("так, друг сказал мне идти сюда, здесь некого нет... хм... он что, меня обма...")
    time.sleep(5)
    print("хей, Ден, сюда!")
    time.sleep(1)
    print("топает")
    time.sleep(1)
    print("Ден, садись")
    time.sleep(1)
    print("ого, новая тачила")
    time.sleep(1)
    print("странный звук...")
    start=input("точно хочеш начать путешествие? " )
    if start=="хочу":
        print("ой ё...")
        time.sleep(1)
        print("так, стоп чо происходит")
        time.sleep(1)
        print("осматривается")
        time.sleep(1)
        print("...")
        time.sleep(3)
        print("Через время")
        time.sleep(3)
        print("...")
        time.sleep(3)
        print("Я хожу по этому лесу'эх'девятый'эх'день'эх'и тут даже ягод нет")
        time.sleep(5)
        print("...")
        time.sleep(3)
        print("ч-что!")
        time.sleep(1)
        print("бег")
        time.sleep(1)
        print("скрип двери")
        time.sleep(1)
        print("чья это хижена по среди леса?")
        time.sleep(1)
        print("хлопок двери")
        time.sleep(1)
        print("Эй!...что...происходит...")
        time.sleep(2)
        print("зажглась свеча твоей игры, путник")
        time.sleep(2)
        print("АаАа. Вашуж мать. т-ты кто?")
        time.sleep(1)
        print("Я заведующий местной игрой")
        print("А именно")
        time.sleep(2)
        print("Безумие!")
        time.sleep(2)
        print("Хочеш сыграть?")
        time.sleep(1)
        print("'Я не могу отказаться. Мне нужна еда и начлег, хотя бы на сегодня'")
        time.sleep(5)
        print("Согласен")
        time.sleep(2)
        print("правила таковы")
        time.sleep(1)
        print("твоя задача-угадать загаданную мной карту")
        print("небойся, карты обычные, не кусаются")
        print("у тебя, такуш и быть, на первый раз количества попыток нет")
        start2=input("согласен? ")
        if start2 == "согласен":
            print("прекрастно...")
            time.sleep(1)
            print("на поле карты:")
            mastikarti1=(masti[random.randint(0,3)])
            nomerkarti1=(nomer[random.randint(0,9)])
            print(mastikarti1,nomerkarti1)
            mastikarti2=(masti[random.randint(0,3)])
            nomerkarti2=(nomer[random.randint(0,9)])
            print(mastikarti2,nomerkarti2)
            mastikarti3=(masti[random.randint(0,3)])
            nomerkarti3=(nomer[random.randint(0,9)])
            print(mastikarti3,nomerkarti3)
            mastikarti4=(masti[random.randint(0,3)])
            nomerkarti4=(nomer[random.randint(0,9)])
            print(mastikarti4,nomerkarti4)
            mastikarti5=(masti[random.randint(0,3)])
            nomerkarti5=(nomer[random.randint(0,9)])
            print(mastikarti5,nomerkarti5)
            mastikarti6=(masti[random.randint(0,3)])
            nomerkarti6=(nomeri[random.randint(0,9)])
            print(mastikarti6,nomerkarti6)
            mastikarti7=(masti[random.randint(0,3)])
            nomerkarti7=(nomer[random.randint(0,9)])
            print(mastikarti7,nomerkarti7)
            mastikarti8=(masti[random.randint(0,3)])
            nomerkarti8=(nomer[random.randint(0,9)])
            print(mastikarti8,nomerkarti8)
            mastikarti9=(masti[random.randint(0,3)])
            nomerkarti9=(nomer[random.randint(0,9)])
            print(mastikarti9,nomerkarti9)
            mastikarti10=(masti[random.randint(0,3)])
            nomerkarti10=(nomer[random.randint(0,9)])
            print(mastikarti10,nomerkarti10)
            sagadanno=random.randint(1,10)
            if sagadanno == "1":
                sagadannayamast=mastikarti1
                sagadanniynomer=nomerkarti1
            elif sagadanno == "2":
                sagadannayamast=mastikarti2
                sagadanniynomer=nomerkarti2
            elif sagadanno == "3":
                sagadannayamast=mastikarti3
                sagadanniynomer=nomerkarti3
            elif sagadanno == "4":
                sagadannayamast=mastikarti4
                sagadanniynomer=nomerkarti4
            elif sagadanno == "5":
                sagadannayamast=mastikarti5
                sagadanniynomer=nomerkarti5
            elif sagadanno == "6":
                sagadannayamast=mastikarti6
                sagadanniynomer=nomerkarti6
            elif sagadanno == "7":
                sagadannayamast=mastikarti7
                sagadanniynomer=nomerkarti7
            elif sagadanno == "8":
                sagadannayamast=mastikarti8
                sagadanniynomer=nomerkarti8
            elif sagadanno == "9":
                sagadannayamast=mastikarti9
                sagadanniynomer=nomerkarti9
            elif sagadanno == "10":
                sagadannayamast=mastikarti10
                sagadanniynomer=nomerkarti10
            otgadivanyemasti=input("какую масть я загадал ")
            while otgadivanyemasti!=sagadannayamast:
                print("Нет! Думай дальше!")
                otgadivanyemasti=input("какую масть я загадал ")
            else:
                print("Молодец, Угадал")
                time.sleep(2)
            print("Так... Каую масть я загодал, ты-отгодал. а кокая карта ")
            time.sleep(5)
            while otgadivanyemasti!=sagadannayamast:
                print("Нет! Думай дальше!")
                otgadivanyemasti=input("какую кату я загадал ")
            else:
                print("Молодец, Угадал всё")
            
            
