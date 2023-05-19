
class Hero:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def speak(self):
        print(f"当前英雄{self.name}的血量为{self.hp}， 攻击力为{self.power}")

    def fight(self, enemy_name, enemy_hp, enemy_power):
        my_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if my_final_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif enemy_final_hp > my_final_hp:
            print(f"敌人{enemy_name}赢了")
        else:
            print("平局，请重新输入")