import random

counter = 0
rand = random.uniform(0.85, 1.00)
move = 0

# type effectivity
def typeEff(p1Type, p2Type, p1Type2):
    typeEffectivity = 0.0
    if p1Type == "Dragon" and p2Type == "Dragon":
      typeEffectivity = 2.0
    elif (p1Type2 == "Electric" and p2Type == "Dragon") or (p1Type2 == "Fire" and p2Type == "Dragon"):
      typeEffectivity = 0.5
    else:
      typeEffectivity = 1.0
    typeEffectivity = typeEff
    return typeEff
#Attacks
class Attack:
  Type = "None"
  def __init__(self, name, Type, kind, power, accuracy, pp):
    self.name = name
    self.Type = Type
    self.kind = kind
    self.power = power
    self.accuracy = accuracy
    self.pp = pp
  
hyperVoice = Attack("Hyper Voice", "Normal", "Special", 90, 100, 10)
boltStrike = Attack("Bolt Strike", "Electric", "Physical", 130, 85, 5)
dragonPulse = Attack("Dragon Pulse", "Dragon", "Special", 85, 100, 10)
brutalSwing = Attack("Brutal Swing", "Dark", "Physical", 60, 100, 20)
blueFlare = Attack("Blue Flare", "Fire", "Special", 130, 85, 5)
outrage = Attack("Outrage", "Dragon", "Physical", 120, 100, 10)
crunch = Attack("Crunch", "Dark", "Physical", 80, 100, 15)


class Pokemon:
  level = 100
  speed = 0
  def __init__(
    self, name, type1, type2, hp, attack, defense, spa, spd, speed, move_1, move_2, move_3, move_4
    ):
      self.name = name
      self.type1 = type1
      self.type2 = type2
      #self.baseStats = [hp, attack, defense, spa, spd, speed]
      self.currentStats = [hp, attack, defense, spa, spd, speed]
      self.moveSet = [move_1, move_2, move_3, move_4]
Zekrom = Pokemon("Zekrom", "Dragon", "Electric", 1404.0, 438, 372, 372, 328, 305, boltStrike, dragonPulse, brutalSwing, hyperVoice)
Reshiram = Pokemon("Reshiram", "Dragon", "Fire", 1404.0, 372, 328, 438, 372, 304, blueFlare, outrage, crunch, hyperVoice)


# Critical Hit 
crit = 0.0
randCrit = random.randint(0, 255)
t = Pokemon.speed / 2
p = t / 256
if randCrit < t:
    crit = 1.5
    print("Critical Hit!")
else:
    crit = 1.0

# STAB value 
stab = 0.0;
if (Zekrom.type1 == Attack.Type) or (Attack.Type == Zekrom.type2) or (Reshiram.type1 == Attack.Type) or (Attack.Type == Reshiram.type2):
  stab = 1.5
  print ("The move was of the same type as your Pokemon!")
else:
  stab = 1.0
  
def modifier(bonus, effectivity, critical, random):
  mod = bonus * effectivity * critical * random
  return mod
typeEff = 1  
# damage calculator
def damage(level, usrAtk, opDef, base):
    mod = modifier(stab, typeEff, crit, rand)
    damage = (((2 * level + 10) / 250) * (usrAtk / opDef) * base + 2) * mod
    return damage
def Fight(pkmn, uattck, odefe):
  attackPower = damage(100, uattck, odefe, move)
  print (boltStrike.pp)
  print ("attack power: {:0.3f}" .format(attackPower))
  print (pkmn.name, "old health: {:0.3f} " .format (pkmn.currentStats[0]))
  pkmn.currentStats[0] -= attackPower
  print (pkmn.name, "new health: {:0.3f} " .format (pkmn.currentStats[0]))
  print ("\n")

while (Zekrom.currentStats[0] > 0) and (Reshiram.currentStats[0] > 0):
    counter += 1
    if Zekrom.currentStats[5] > Reshiram.currentStats[5]:
          #Zekrom's turn
        print ("It's Zekrom's turn.")
        print ("Zekrom's HP: ", int(Zekrom.currentStats[0]))
        print ("Zekrom's Moveset: \n Bolt Strike \n Dragon Pulse \n Brutal Swing \n Hyper Voice")
        choice = int(input("Choose the number corresponding to what move you would like Zekrom to do : "))
        if choice == 1:
          move = 130
          boltStrike.pp -= 1
          typeEff = 0.5 #type effectivity
          Fight(Zekrom, Zekrom.currentStats[1], Reshiram.currentStats[2])
        elif choice == 2:
          move = 85
          dragonPulse.pp -= 1
          typeEff = 2
          Fight(Zekrom, Zekrom.currentStats[3], Reshiram.currentStats[4])
        elif choice == 3:
          move = 60
          brutalSwing.pp -= 1
          typeEff = 1
          Fight(Zekrom, Zekrom.currentStats[1], Reshiram.currentStats[2])
        else:
          move = 90
          hyperVoice.pp -= 1
          typeEff = 1
          Fight(Zekrom, Zekrom.currentStats[3], Reshiram.currentStats[4])
      
        if Zekrom.currentStats[0] == 0:
          break
        
          #Reshiram's turn
        print ("It's Reshiram's turn.")
        print ("Reshiram's HP: ", int(Reshiram.currentStats[0]))
        print ("Reshiram's Moveset: \n Blue Flare \n Outrage \n Crunch \n Hyper Voice")
        choice = int(input("Choose the number corresponding to what move you would like Reshiram to do : "))
        if choice == 1:
          move = 130
          blueFlare.pp -= 1
          typeEff = 0.5
          Fight(Reshiram, Reshiram.currentStats[3], Zekrom.currentStats[4])
        elif choice == 2:
          move = 85
          outrage.pp -= 1
          typeEff = 2
          Fight(Reshiram, Reshiram.currentStats[1], Zekrom.currentStats[2])
        elif choice == 3:
          move = 60
          crunch.pp -= 1
          typeEff = 1
          Fight(Reshiram, Reshiram.currentStats[1], Zekrom.currentStats[2])
        else:
          move = 90
          hyperVoice.pp -= 1
          typeEff = 1
          Fight(Reshiram, Reshiram.currentStats[3], Zekrom.currentStats[4])
        
        if Zekrom.currentStats[0] == 0:
          break
        
    else:
        #Reshiram's turn
      print ("It's Reshiram's turn.")
      print ("Reshiram's HP: ", int(Reshiram.currentStats[0]))
      print ("Reshiram's Moveset: \n Blue Flare \n Outrage \n Crunch \n Hyper Voice")
      choice = int(input("Choose the number corresponding to what move you would like Reshiram to do : "))
      if choice == 1:
        move = 130
        blueFlare.pp -= 1
        typeEff = 0.5
        Fight(Reshiram, Reshiram.currentStats[3], Zekrom.currentStats[4])
      elif choice == 2:
        move = 85
        outrage.pp -= 1
        typeEff = 2
        Fight(Reshiram, Reshiram.currentStats[1], Zekrom.currentStats[2])
      elif choice == 3:
        move = 60
        crunch.pp -= 1
        typeEff = 1
        Fight(Reshiram, Reshiram.currentStats[1], Zekrom.currentStats[2])
      else:
        move = 90
        hyperVoice.pp -= 1
        typeEff = 1
        Fight(Reshiram, Reshiram.currentStats[3], Zekrom.currentStats[4])
      
      if Zekrom.currentStats[0] == 0:
          break
        
        #Zekrom's turn
      print ("It's Zekrom's turn.")
      print ("Zekrom's HP: ", int(Zekrom.currentStats[0]))
      print ("Zekrom's Moveset: \n Bolt Strike \n Dragon Pulse \n Brutal Swing \n Hyper Voice")
      choice = int(input("Choose the number corresponding to what move you would like Zekrom to do : "))
      if choice == 1:
        move = 130
        boltStrike.pp -= 1
        typeEff = 0.5
        Fight(Zekrom, Zekrom.currentStats[1], Reshiram.currentStats[2])
      elif choice == 2:
        move = 85
        dragonPulse.pp -= 1
        typeEff = 2
        Fight(Zekrom, Zekrom.currentStats[3], Reshiram.currentStats[4])
      elif choice == 3:
        move = 60
        brutalSwing.pp -= 1
        typeEff = 1
        Fight(Zekrom, Zekrom.currentStats[1], Reshiram.currentStats[2])
      else:
        move = 90
        hyperVoice.pp -= 1
        typeEff = 1
        Fight(Zekrom, Zekrom.currentStats[3], Reshiram.currentStats[4])
      if Zekrom.currentStats[0] == 0:
        break

else:
  if Zekrom.currentStats[0] <= 0:
    print ("Zekrom has fainted!")
    print ("The battle took:", counter, "rounds.")
  elif Reshiram.currentStats[0] <= 0:
    print ("Reshiram had fainted!")
    print ("The battle took:", counter, "rounds.")
  else:
    print("LOL")