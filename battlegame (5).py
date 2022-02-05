### TASK 1 ###

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hitpoints, elf_hitpoints, human_hitpoints, dragon_hitpoints = 70, 100, 150, 300
wizard_damage, elf_damage, human_damage, dragon_damage = 150, 100, 20, 50

character = 0
my_hitpoints = 0
my_damage = 0

print("##############################")

### TASK 2 and TASK 3 ###

while character == 0:
    print("PLEASE SELECT THE NUMBER FOR YOUR CHARACTER BELOW:")
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = int(input("CHOOSE YOUR CHARACTER: "))
    if character == 1:
        character = wizard
        my_hitpoints = wizard_hitpoints
        my_damage = wizard_damage
        break
    elif character == 2:
        character = elf
        my_hitpoints = elf_hitpoints
        my_damage = elf_damage
        break
    elif character == 3:
        character = human
        my_hitpoints = human_hitpoints
        my_damage = human_damage
        break
    else:
        print("Uknown Character")
print(" ")
print("--------------------------------")
print(" ")
print("You have chosen:", character)
print("Health: ", my_hitpoints)
print("Damage: ", my_damage)
print(" ")
print("--------------------------------")
print(" ")

### TASK 4 ###

while True:
    dragon_hitpoints = dragon_hitpoints - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hitpoints)
    print(" ")

    if dragon_hitpoints <= 0:
        print("The Dragon has lost the battle!")
        break

    my_hitpoints = my_hitpoints - dragon_damage
    print("The Dragon strikes back!")
    print("The", character, "points are now ", my_hitpoints)
    print(" ")

    if my_hitpoints <= 0:
        print("The", character, "has lost the battle")
        break

print("--------------------------------")