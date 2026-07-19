import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 6000  # 血量统一6000

    def is_alive(self):
        return self.hp > 0

# 创建角色
A = Player("G哥")
B = Player("清风·烟雨")

print("===== 对战开始 =====")
print("G哥血量：6000")
print("清风·烟雨血量：6000")
print("====================\n")

# 循环直到一方倒下
while A.is_alive() and B.is_alive():

    # ========== 1. 你手动选择进攻方 ==========
    print("请选择进攻方：")
    print("1 —— G哥 进攻")
    print("2 —— 清风·烟雨 进攻")
    choice = input("请输入 1 或 2：")

    # 防止输错
    #while choice not in ["1", "2"]:
     #   choice = input("输入错误！重新输入 1 或 2：")

    # 自动确定攻防
    if choice == 1:
        attacker = A
        defender = B
    elif choice == 2:
        attacker = B
        defender = A

    # ========== 2. 系统随机：攻击类型 ==========
    atk_mode = random.choice(["物理", "法术"])

    # ========== 3. 系统随机：防御类型 ==========
    def_mode = random.choice(["物理防御", "法术防御"])

    # ========== 4. 按角色设定伤害与减伤 ==========
    # A 的伤害
    if attacker.name == "A":
        if atk_mode == "物理":
            damage = 2000
        else:
            damage = 200
    # B 的伤害
    else:
        damage = 500  # B物理法术都是500

    # 防御减伤
    if defender.name == "A":
        defend = 200
    else:
        defend = 1000

    # ========== 5. 计算最终伤害 ==========
    final_dmg = max(damage - defend, 0)
    defender.hp = max(defender.hp - final_dmg, 0)

    # ========== 6. 展示战斗过程 ==========
    print("\n----- 战斗结果 -----")
    print(f"进攻方：{attacker.name}（{atk_mode}攻击）")
    print(f"防御方：{defender.name}（{def_mode}）")
    print(f"基础伤害：{damage}，减免：{defend}")
    print(f"最终伤害：{final_dmg}")
    print(f"{defender.name} 剩余血量：{defender.hp}\n")

# ========== 结束 ==========
print("========================")
if A.hp <= 0:
    print("🏆 B 获胜！")
else:
    print("🏆 A 获胜！")
print("========================")