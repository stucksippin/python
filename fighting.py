import random


class Fighter:
    def __init__(self, name):
        self.live = 100
        height = random.randint(150, 200) / 100
        weight = random.randint(50, 100)
        self.name = name
        self.power = int(weight / height ** 2)
        is_alive = True
        self.show_info()

    def attack(self, fighter: Fighter) -> bool:
        hit = random.randint(1, 10)
        if (hit < 6):
            hit = int(self.power * 0.8)
            fighter.live -= hit
            print(fighter.name, "Отхватил:", hit, "Здоровье", fighter.live)
            return True
        else:
            print(fighter.name, "заблокировал удар")
            return False

    def show_info(self):
        print('Name', self.name, 'Power', self.power)


class Contest:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def fight(self):

        while (self.first.live > 0 and self.second.live > 0):
            attacker = random.choice([self.first, self.second])
            if attacker == self.second:
                defender = self.first
            else:
                defender = self.second
            attacker.attack(defender)

        if self.first.live > 0:
            return self.first
        else:
            return self.second


contest = Contest(Fighter("Вася"), Fighter("Петя"))
winner = contest.fight()
print("Win:", winner.name)