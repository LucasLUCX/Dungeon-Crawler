from resources import *

class Dungeon:
    def __init__(self) -> None:
        self.in_dungeon = True
        self.in_battle = True
        self.player_in_attack = True
        self.enemy = None
        self.room = 0
        self.dungeon()
    
    #this is the entire dungeon loop -- this code is very bad im not refactoring
    def dungeon(self) -> None:
        while self.in_dungeon:
            if player.health <= 0:
                self.in_dungeon = False
                break
            
            
            self.enemy = self.pick_enemy() 
            self.in_battle = True
            print(" ")
            print("--------------------")
            print(f"the player has encountred {self.enemy.name}")
            self.room += 1
            while self.in_battle :
                self.player_in_attack = True
                while self.player_in_attack:
                    if player.player_turn(self.enemy,self) :
                        self.player_in_attack = False
                
                self.enemy.enemy_turn(player,self)
                    
                
            self.enemy.health = self.enemy.max_health
            player.defense = player.armor.defense
            
            if self.room == 31:
                self.win()

    #simple enmy picking based on room
    def pick_enemy(self) -> Enemy:
        if self.room <= 10:
            if self.room == 10:
                return enemy_0_01 
            return [enemy_1_01,enemy_1_02,enemy_1_03,enemy_1_04,enemy_1_05][rng.randint(0,4)]
        elif self.room <= 20:
            if self.room == 20:
                return enemy_0_02 
            return [enemy_2_01,enemy_2_02,enemy_2_03,enemy_2_04,enemy_2_05][rng.randint(0,4)]
        elif self.room <= 30:
            if self.room == 30:
                return enemy_0_03
            return [enemy_3_01,enemy_3_02,enemy_3_03,enemy_3_04,enemy_3_05][rng.randint(0,4)]
    
    def win():
        print("====================================")
        print("|Congrats on destroing the dungeon |")
        print("====================================")
        player.print_stats()
        exit()