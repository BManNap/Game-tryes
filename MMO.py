#Ideas
#So for the Upgrade Sword option I was thinking from going to wood(2) to iron(3), gold(5), titaniam(8), diamond(12), Then uraninam(17)
#

#imports
import random

#Varibals

#hero health
hero_health = 15
max_health = 15

#stuff for goblin health
goblin_health2 = 10
goblin_health = goblin_health2

#goblin attack damage
goblin_damage = 2

#heros attack damage
attack_damage = 2

#heros inventory
bandage = 3
mana_potion = 4
gold = 0

#heal amount
heal = 10

#mana amout
mana = 50

#how many goblins you killed
goblin_kill = 0

#enemys stautes
no_stun = False
enemy = no_stun
stun = True

#Beging of the script
hero_name = input("What is your heros name: ")

if hero_name == 'test':
    hero_health = 999
    max_health = 999
    attack_damage = input('attack damage:')
    attack_damage = int(attack_damage)
    mana = 999
    gold = 99999
    
while (hero_health > 0):
    print("\n",hero_name,"'s Health:",hero_health,"mana:",mana ,", Golbins killed", goblin_kill,',Gold:', gold,
          "\nWhat would you like to do? attack, heal, shield, inventory, \nspell list(You can use the spells), mana potion, quit")
    do = input(":").lower()

#Damage doing things
    #attack

    if do == "attack":
        goblin_health = goblin_health - attack_damage
        

        if goblin_health <= 0:
            goblin_health2 = goblin_health2 + 5
            goblin_health = goblin_health2
            goblin_kill = goblin_kill + 1
            gold2 = random.randint(10,30)
            gold = gold + gold2
            print("You killed a goblin! You got",gold2,'gold')
            enemy = False
            print("New Goblins Health:", goblin_health)
        
        else:
            if enemy == stun:
                enemy == no_stun
                print("The goblin is not stuned any more")
                print("Goblin health:", goblin_health)
            else:
                print("You took", goblin_damage)
                hero_health = hero_health - goblin_damage
                print("Goblin health:", goblin_health)
        


            
    #fire ball
    elif do == "fire ball":
        if mana - 5 < 0:
            print("You have no mana left")
        else:
            mana = mana - 5
            goblin_health = goblin_health - attack_damage - 4
            if goblin_health <= 0:
                goblin_health2 = goblin_health2 + 5
                goblin_health = goblin_health2
                goblin_kill = goblin_kill + 1
                gold2 = random.randint(10,30)
                gold = gold + gold2
                print("You killed a goblin! You got",gold2,'gold')
                enemy = False
                print("New Goblins Health:", goblin_health)
                    
            elif enemy == stun:
                print("The goblin is not stuned any more")
                print("Goblin health:", goblin_health)

                
            else:
                print("You took", goblin_damage)
                hero_health = hero_health - goblin_damage
                print("Goblin health:", goblin_health)


        
    #stun bomb
    elif do =="stun bomb":
        if mana - 7 < 0:
            print("You don't have enogh mana.")
        else:
            enemy = stun
            mana = mana - 7
            print("You have stun the enemy for 1 turn.")
            



#Iteam useage
    elif do == "heal":
        if bandage <= 0:
            print("\nYou have no bandages left")

        else:
            if hero_health == max_health:
                print("\nYou are already healed")


            else:
                hero_health = hero_health + heal
                bandage = bandage - 1
                if hero_health > max_health:
                    hero_health = max_health
                print("\nYou used a bandage, you healed", heal , "damage")

    elif do == "mana potion":
        if mana_potion == 0:
            print("You have no more potions left")
        else:
            if mana == 50:
                print("Your already full")
            else:
                print("You used a mana potion")
                mana = mana + 25
                mana_potion = mana_potion - 1
                if mana > 50:
                    mana = 50


#Shop
                     
    elif do == "shop":
        if enemy == False or True:
            shop = True
            while shop == True:
                print("What would you like to do? Buy: bandage (50), mana potion(100), \n attack up, health up, or leave (ex:buy bandage) ")
                do_shop = input(':')
                if do_shop == 'leave':
                        shop = False
                elif do_shop == 'buy bandage':
                    if gold - 50 >=0:
                        gold = gold - 50
                        bandage = bandage + 1
                        print('Bandage added, you now have', bandage, 'bandages')
                    else:
                        print('Not enough gold\n')
                elif do_shop == 'buy mana potion':
                    if gold - 100 >=0:
                        gold=gold-100
                        mana_potion = mana_potion+1
                        print('Mana potion added, you now have',mana_potion,'mana potions\n')
                    else:
                        print("You don't have enoghe gold\n")

                elif do_shop == 'buy damage up':
                    if gold - 250 >= 0:
                        gold = gold - 250
                        attack_damage = attack_damage + 1
                        print("You'r Damage is now\n", attack_damage)
                    else:
                        print("You Don't have Enoguh Gold\n")

                elif do_shop =='buy health up':
                    if gold - 300 >=0:
                        gold = gold - 300
                        hero_health = hero_health +5
                        max_health = max_health +5
                        print("Your max health is now\n", max_health)
                    else:
                        print("You Don't Have Eough Gold\nS")


                elif do_shop == 'leave':
                    shop = False

        else:
            print('You have to kill the enemy first')
            
#useless command (shield)
    elif do == "shield":
        print("\nYou have used a usless iteam and you lost", goblin_damage - 1 ,"health")
        hero_health = hero_health - goblin_damage - 1

    elif do == "quit":
        quit()

#Listing things you have avaible
    elif do == "inventory":
        print("Bandage:", bandage)
        print("mana potion:", mana_potion)

    elif do == "spell list":
        print("\nfire ball: 5 mana\nstun bomb:7 mana")

    elif do == 'die':
        hero_health = 0

        
    else:
        print("That's not a command")
    
print("Game over")
input("Press Enter to End")
