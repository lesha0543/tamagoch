import random
import keyboard as kb
import time
import sys



class Dinozavrik:
    def __init__(self):
        self.live = 0
        self.zdorov = 100
        self.eda = 100
        self.fun = 100
        self.clear = 100
        self.dlina_live = 50
        self.dead = 0

    def poysnenie(self):
        return f"1 - Полечить, 2 - Покормить, 3 - Поиграть, 4 - Помыть"

    def schetchik_live(self):
        self.live += 1
        return self.live

    def deads(self):
        if self.live >= self.dlina_live:
            self.dead = "умер от старости"
            self.live = "GAME OVER"
        if self.zdorov <= 0:
            self.dead = "умер от болезни"
            self.live = "GAME OVER"
        elif self.eda <= 0:
            self.dead = "умер от голода"
            self.live = "GAME OVER"
        elif self.fun <= 0:
            self.dead = "умер от скуки"
            self.live = "GAME OVER"
        elif self.clear <= 0:
            self.dead = "умер от грязи"
            self.live = "GAME OVER"
        elif random.randint(1,100) == 1:
            self.dead = "убило метеоритом"
            self.live = "GAME OVER"

    def schetchik_dlina_live(self):
        return self.dlina_live

    def schetchik_zdorov(self):
        self.zdorov -= random.randint(1,5)
        return self.zdorov

    def schetchik_eda(self):
        self.eda -= random.randint(1,5)
        return self.eda

    def schetchik_fun(self):
        self.fun -= random.randint(1,5)
        return self.fun

    def schetchik_clear(self):
        self.clear -= random.randint(1,5)
        return self.clear

    def lechenie(self):
        self.zdorov += random.randint(5,10)
        self.dlina_live += 1

    def kormit(self):
        self.eda += random.randint(5,10)

    def igra(self):
        self.fun += random.randint(5,10)

    def chistka(self):
        self.clear += random.randint(5,10)

    def svodka_zdorov(self):
        if  40 < self.zdorov < 60:
            return f'Пора подлечиться'
        elif self.zdorov < 40:
            return f'Мне совсем плохо'
        elif self.zdorov > 60:
            return ""
    def svodka_eda(self):
        if 40 < self.eda < 60:
            return f'Может перекусим????'
        elif self.eda < 40:
            return f'ЖРААААТТТТЬЬЬ!!!!'
        elif self.eda > 60:
            return ""
    def svodka_fun(self):
        if 40 < self.fun < 60:
            return f'Скучччччннннооооо(((('
        elif self.fun < 40:
            return f'Ну ты хотя бы мячик кинь....'
        elif self.fun > 60:
            return ""
    def svodka_clear(self):
        if 40 < self.clear < 60:
            return f'Почти как свинья'
        elif self.clear < 40:
            return f'Хрююююююююююююююююю'
        elif self.clear > 60:
            return ""


bz = Dinozavrik()

print(bz.poysnenie())
kb.add_hotkey('1',bz.lechenie)
kb.add_hotkey('2',bz.kormit)
kb.add_hotkey('3',bz.igra)
kb.add_hotkey('4',bz.chistka)
while True:
    if bz.live == "GAME OVER":
        print(f"\nИгра окончена, {bz.dead}")
        break
    else:
        sys.stdout.writelines(f"\rЛет динозаврику: {bz.schetchik_live()}/{bz.schetchik_dlina_live()} "
                              f"Здоровье: {bz.schetchik_zdorov()} {bz.svodka_zdorov()} "
                              f"Покормить: {bz.schetchik_eda()} {bz.svodka_eda()}"
                              f"Поиграть: {bz.schetchik_fun()} {bz.svodka_fun()}"
                              f"Помыть: {bz.schetchik_clear()} {bz.svodka_clear()}")
        time.sleep(3)
        bz.deads()