class Country(object):
    def __init__(self, name, life):
        self.name = name
        self.life = life

    #攻撃
    #攻撃する相手を選択
    def attack(self, enemy):
        enemy.life -= 1

    #防御
    #防御する相手を選ぶ

gi_country = Country("魏", 100)
go_country = Country("呉", 100)

gi_country.attack(go_country)
print(go_country.life)