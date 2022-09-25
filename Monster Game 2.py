class Monster():
    def __init__(self, name, hp=20):
        self.exp = 0
        #your code here
        self.name = name
        self.type = "Normal"
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.attacks = {"wait": 0}
        self.possible_attacks = {"sneak_attack" : 1, "slash" : 2, "ice_storm" : 3, "fire_storm" : 3, "whirlwind" : 3, "earthquake" : 2, "double_hit" : 4, "tornado" : 4, "wait" : 0}
    
    def add_attack(self, attack_name):
        if attack_name not in self.possible_attacks:
            return False
        if len(self.attacks) < 4:
            self.attacks[attack_name] = self.possible_attacks[attack_name]
            return True
        else:
            smallest_attack = ""
            for word in self.attacks.keys():
                if self.attacks[word] == min(self.attacks.values()):
                    if smallest_attack != "":
                        if word < smallest_attack:
                            smallest_attack = word
                    else:
                        smallest_attack = word
            self.remove_attack(smallest_attack)
            self.attacks[attack_name] = self.possible_attacks[attack_name]
            return True
      
    def remove_attack(self, attack_name):
        if attack_name not in self.attacks.keys():
            return False
        del self.attacks[attack_name]
        if len(self.attacks) == 0:
            self.attacks["wait"] = 0
        return True
            
    def win_fight(self):
        self.exp = self.exp + 5
        self.hp = self.max_hp
    
    def lose_fight(self):
        self.exp = self.exp + 1
        self.hp = self.max_hp
  
def monster_fight(monster1, monster2):
        
    if len(monster1.attacks) == 1 and len(monster2.attacks) == 1:
        if "wait" in monster1.attacks and "wait" in monster2.attacks:
            return -1, None, None
    # strongest_attack1 = max(monster1.attacks.value())
    # strongest_attack2 = max(monster2.attacks.value())

    # get the sorted list of monsters attack
    sorted_list1 = []
    sorted_list2 = []   
    
    sorted_attack1 = sorted(list(monster1.attacks.keys()))
    sorted_attack2 = sorted(list(monster2.attacks.keys()))
    
    sort_value1 = max(monster1.attacks.values())
    sort_value2 = max(monster2.attacks.values())
    loop1 = sort_value1 + 1
    loop2 = sort_value2 + 1
    
    for i in range(loop1):
        for key in sorted_attack1:
            if monster1.attacks[key] == sort_value1:
               sorted_list1.append(key)
        sort_value1 -= 1
    
    for i in range(loop2):
        for key in sorted_attack2:
            if monster2.attacks[key] == sort_value2:
               sorted_list2.append(key)
        sort_value2 -= 1
    
    # initialize two things, init empty list for 
    user_attack1 = []
    user_attack2 = []

    # init index
    index1 = 0 
    index2 = 0
    
    # print(sorted_list2)
    # print(sorted_list1)
    
    round_cnt = 1
 
    # go through the final list from 0 to 1 for the moves
    while monster1.current_hp > 0 and monster2.current_hp > 0:
        key1 = sorted_list1[index1]
        # print(key1, index1)
        key2 = sorted_list2[index2]
        # print(key2, index2)
        value1 = monster1.attacks[key1]
        value2 = monster2.attacks[key2]
        monster2.current_hp = monster2.current_hp - value1
        monster1.current_hp = monster1.current_hp - value2
        # append moves for monster1
        user_attack1.append(key1)
        user_attack2.append(key2)
        # if the monster2 dies, monster1 attacking
        if monster2.current_hp <= 0:
            monster1.win_fight()
            monster2.lose_fight()
            # print(round_cnt)
            # print(monster1)
            # print(user_attack1)
            # print(type(round_cnt))
            # print(type(monster1))
            # print(type(user_attack1))
            return round_cnt, monster1, user_attack1
        if monster1.current_hp <= 0:
            monster2.win_fight()
            monster1.lose_fight()
            return round_cnt, monster2, user_attack2
        index2 = (index2+1) % len(sorted_attack2) 
        index1 = (index1+1) % len(sorted_attack1)
        round_cnt += 1
        
        # print(user_attack1)
        # print(user_attack2)
       


# monster1 = Monster("s", 10)
# monster2 = Monster("d", 9)

# # monster1.add_attack("earthquake")
# # monster1.add_attack("ice_storm")
# monster1.add_attack("fire_storm")
# monster1.add_attack("whirlwind")
# # monster1.remove_attack("wait")


# monster2.add_attack("whirlwind")
# monster2.add_attack("ice_storm")
# # monster2.add_attack("fire_storm")
# # monster2.add_attack("double_hit")
# # monster2.remove_attack("wait")

# monster_fight(monster1, monster2)
# roundc, winner, attackL = monster_fight(monster1, monster2)

# print(attackL)
# print(roundc)
# print(winner)
    
