"""
Name(s): catherine mao & olive eng
Name of Project: "The Island: A Psychological Thriller in Three Acts"
"""

def start():
  print("You are on a cruise.")
  print("The boat crashes.")
  print("You wash up on a shore of an island.")
  print("The only survivors are you, your childhood best friend, a preganant person, an old man, and a screaming and crying orphan. They look to you for directions.")
  print("")
  print("There are two paths in front of you.")
  print("")
  print("You can either: ")
  print("Lead the group down a mysterious path leading to the FOREST at the heart of the island...")
  print("OR all of you can explore the BEACH you washed up on.")    
  print("")

  choice = input(str("Enter Forest to explore the forest or Beach to explore the beach: "))
  while choice.lower() != "forest" and choice.lower() != "beach":
    choice = input(str("You must choose 'forest' or 'beach': "))
  if choice.lower() == "forest":
    forest()
  elif choice.lower() == "beach":
    beach()


def forest():
  print("")
  print("You are now in the forest.")
  print("")
  print("You are surrounded by thick, towering trees. The pregnant person suggests cutting the trees to make a boat to leave the island.")
  print("")
  print("You have cut enough trees to make a boat, but you're not sure it can hold more than one person. In the distance, you hear a roar.")
  print("")
  print("You can either:")
  print("Leave the forest with only enough wood for a small boat, but avoid the source of the ominous roaring...")
  print("Or stay in the forest and and collect enough wood for a bigger boat.")
  print("")

  choice = input(str("Enter Leave to leave the forest and Stay to stay in the forest: "))
  while choice.lower() != "stay" and choice.lower() != "leave":
    choice = input(str("You must choose 'stay' or 'leave': "))
  if choice.lower() == "stay":
    stayinjury()
  elif choice.lower() == "leave":
    leaveboats()


def stayinjury():
  print("")
  print("You chose to stay in the forest.")
  print("")
  print("As you collect more wood, you accidentally drop a log on your best friend.")
  print("")
  print("Their foot is not bending the way a foot is meant to bend and a pool of blood is collecting between you.")
  print("")
  print("You fashion a makeshift splint, but the roaring gets louder with every second. Suddenly, you hear rapidly approaching footsteps and a pack of Very Ferocious Dogs runs towards you, snarling.")
  print("")
  print("You try to run away, but with your friend's broken foot, the Very Ferocious Dogs are catching up. It seems they are attracted to the blood spurting out of your best friend's foot.")
  print("")
  print("The other people run away, leaving you and your best friend to fend off the Very Ferocious Dogs. The dogs have you surrounded, but if you leave your friend, you reckon you have a chance to escape them.")
  print("")
  print("Do you want to abandon your helpless, injured friend to be mauled by the dogs and save yourself...")
  print("OR stay with them and try to fend off the dogs together?")
  print("")

  choice = input(str("Enter Abandon to run and save yourself and enter Help to stay behind and help the friend to fend off the dogs: "))
  while choice.lower() != "abandon" and choice.lower() != "help":
    choice = input(str("you must choose 'abandon' or 'help': "))
  if choice.lower() == "help":
    print("")
    print("You chose to help your friend against the dogs.")
    print("")
    print("You try to fend off the dogs, but you and your friend are no match for their Ferocity. You both get mauled and die.")
    print("")
    print("your path: FOREST, STAY in forest, HELP friend")
  elif choice.lower() == "abandon":
    print("")
    print("You chose to abandon your friend against the dogs.")
    print("")
    print("You dodge the dogs. As you run away, leaving your friend for dead, you hear their screams and the ripping of tendons. A feeling of intense guilt overwhelms you.")
    print("")
    print("Distracted, you trip on a root. The dogs quickly catch up to you and maul you. You die within minutes.")
    print("")
    print("Karma moment.")
    print("")
    print("Your path: FOREST, STAY in forest, ABANDON friend")


def leaveboats():
  print("")
  print("You have returned to the beach, and the roaring has stopped. Together, everybody is able to make a small boat to escape the island on.")
  print("")
  print("The old man is looking weaker by the second, mumbling to himself about jelly beans, and the others are ailing, in need of medical attention. You need to make a decision on how to leave the island, and fast.")
  print("")
  print("Do you guarantee one person's safe return to land or try to save everyone?")
  print("")

  choice = input(str("Enter Save Everyone to save everyone or Save One Person to save only one person: "))
  while choice.lower() != "save one person" and choice.lower() != "save everyone":
    choice = input(str("You must choose 'save one person' or 'save everyone': "))
  if choice.lower() == "save one person":
    onepersononboat()
  elif choice.lower() == "save everyone":
    everyoneonboat()


def onepersononboat():
  print("")
  print("You chose to save only one person, guaranteeing their safety.")
  print("")
  print("Now you have to make the choice of who deserves to leave the island. You do have the option to save yourself.")
  print("")

  choice = input("Who do you want to place on the boat? Enter Old Man, Infant, Pregant Person, Best Friend, or Yourself: ")

  while choice.lower() != "old man" and choice.lower() != "infant" and choice.lower() != "infant" and choice.lower() != "pregnant person" and choice.lower() != "best friend" and choice.lower() != "yourself":
    choice = input(str("You must choose 'old man' or 'infant' or 'infant' or 'pregnant person' or 'best friend' or 'yourself': "))
  if choice == "old man":
    print("You chose to save the old man.")
    print("")
    print("The old man floats away to safety, leaving the rest of the group to wither away on the island. Slowly but surely, all of you die of starvation, exposure, and exhaustion.")
    print("")
    print("Because of his age, the old man dies only a few months after his return to land.")
    print("")
    print("Was that the right choice?")
    print("")
    print("your path: FOREST, LEAVE forest, save OLD MAN")
  elif choice == "infant":
    print("You chose to save the infant.")
    print("")
    print("You place the baby on the raft, praying it will find its way to safety. Slowly but surely, all of you die of starvation, exposure, and exhaustion on the island.")
    print("")
    print("The infant is unable to find their way to land, and drowns at sea.")
    print("")
    print("Was that the right choice?")
    print("")
    print("your path: FOREST, LEAVE forest, save INFANT")
  elif choice == "pregnant person":
    print("You chose to save the pregnant person.")
    print("")
    print("The pregant person floats away, leaving the rest of the group to wither away on the island. Slowly but surely, all of you die of starvation, exposure, and exhaustion.")
    print("")
    print("The pregnant person goes into labor at sea. Because of lack of proper medical care, the baby dies. The mother is heartbroken.")
    print("")
    print("Maybe they could've gotten better medical care on the island, and the baby could have survived. The mother is eventually able to get to land safely.")
    print("")
    print("Was that the right choice?")
    print("")
    print("Your path: FOREST, LEAVE forest, save INFANT")
  elif choice == "best friend":
    print("You chose to save your best friend.")
    print("")
    print("Your friend floats away to safety, leaving the rest of the group to wither away on the island. Slowly but surely, all of you die of starvation, exposure, and exhaustion.")
    print("")
    print("Your best friend lives a long life on land. Is it a happy ending?Up to you to decide.")
    print("")
    print("Was that the right choice?")
    print("")
    print("Your path: FOREST, LEAVE forest, save BEST FRIEND")
  elif choice == "yourself":
    print("You chose to save yourself.")
    print("")
    print("You float away to safety, leaving the rest of the group to wither away on the island. They all die due to starvation, exposure, and exhuastion.")
    print("")
    print("You make it to land safely. You struggle to sleep at night with a guilty conscience. But, you are alive.")
    print("")
    print("Was that the right choice?")
    print("")
    print("Your path: FOREST, LEAVE forest, save YOURSELF")


def everyoneonboat():
  print("You chose to save everyone.")
  print("")
  print("Everybody crowds onto the singular boat.")
  print("")
  print("The boat is sitting very low in the water, but after hours of navigation, you make it to dry land.")
  print("")
  print("Congratulations! You won. You made all the right choices.")
  print("")
  print("This is the one true 'happy ending'")
  print("Your path: FOREST, LEAVE forest, save EVERYONE")



def beach():
  print("")
  print("You are now on the beach.")
  print("")
  print("As you walk along, you notice that some food washed up further along the shore.")
  print("")
  print("Your best friend, who is conveniently a toxicologist, suggests that the food might be poisonous or contaminated. One of the cans of Beefaroni is cracked open from the crash and doesn't smell quite right.")
  print("")
  print("But the rest of the group is exhausted and starving, with no other food source forseeable. ")
  print("")
  print("You can either:")
  print("Eat the food but risk poison/contamination...")
  print("OR choose not to eat the food and stay safe but hungry.")
  print("")

  choice = input(str("Enter Eat for eating the food and Don't Eat for not eating the food: "))
  while choice.lower() != "eat" and choice.lower() != "don't eat":
    choice = input(str("you must choose 'eat' or 'don't eat': "))
  if choice.lower() == "eat":
    eatfood()
  elif choice.lower() == "don't eat":
    cannibalism()


def cannibalism():
  print("You chose to not eat the food.")
  print("")
  print("To their dismay, you forbid the hungry group from eating the food. The group is resentful of you, and more starved than ever.")
  print("")
  print("A feverish look comes over the group. You can see their moral boundaries collapsing, and they're beginning to look at each other as potential food, not potential friends.")
  print("")
  print("You get the sense that if you don't do something now, you'll be the first to get roasted and toasted over an open spit fire.")
  print("")
  print("You can suggest another person as a target for the group's ravenous appetite.")
  print("There is also the option to sacrifice yourself and let yourself become food for the group.")

  choice = input(str("Who do you want to eat? Enter Old Man, Pregnant Person, Infant, Best Friend, or Yourself: " ))
  while choice.lower() != "old man" and choice.lower () != "pregnant person" and choice.lower() != "infant" and choice.lower() != "best friend" and choice.lower() != "yourself":
    choice = input(str("you must choose 'old man' or 'pregnant person' or 'infant' or 'best friend' or 'yourself': "))
  if choice.lower() == "old man":
    print("You chose to eat the old man. He wasn't going to be much help with surviving on the island, anyway.")
    print("")
    print("The rest of you are able to survive for a few more days at most.")
    print("")
    print("Was that the right choice?")
    print("")
    print("your path: BEACH, DON'T EAT beefaroni, eat the OLD MAN")
  elif choice.lower() == "pregnant person":
    print("You chose to eat the pregnant person. She wasn't going to be much help with surviving on the island, anyway.")
    print("")
    print("The rest of you are able to survive for a few more days at most.")
    print("")
    print("Was that the right choice?")
    print("")
    print("Your path: BEACH, DON'T eat beefaroni, eat the PREGNANT PERSON")
  elif choice.lower() == "infant":
    print("You chose to eat the infant. They wouldn't have been able to help with surviving on the island, anyway.")
    print("")
    print("The baby is eaten. The rest of you are able to survive for a few more days at most.")
    print("")
    print("Was that the right choice?")
    print("")
    print("your path: BEACH, DON'T eat beefaroni, eat the INFANT")
  elif choice.lower() == "best friend":
    print("You chose to eat your best friend.")
    print("")
    print("The rest of you are able to survive for a few more days at most.")
    print("")
    print("Was that the right choice?")
    print("")
    print("your path: BEACH, DON'T eat beefaroni, eat your BEST FRIEND")
  elif choice.lower() == "yourself":
    print("You chose to sacrifice yourself to be eaten.")
    print("")
    print("Was that the right choice?")
    print("")
    print("Your path: BEACH, DON'T eat beefaroni, sacrifice YOURSELF to be eaten")


def eatfood():
  print("You chose to eat the food.")
  print("")
  print("")
  print("The beach in front of you starts getting blurry, and you hear distorted voices yelling out. Seems like your friend was right about the toxic beefaroni. Through the confusion, you can see that strangely, the food poisoning is only showing up at your toes.")
  print("")
  print("The rest of the group are slowly passing out, except for your friend, who didn't eat the food.")
  print("")
  print("The only way to save your life is to amputate your foot.")

  choice = input(str("Who do you trust to amputate your foot? Enter Best Friend for best friend and Yourself for yourself: "))
  while choice.lower() != "best friend" and choice.lower() != "yourself":
    choice = input(str("You must choose 'best friend' or 'yourself': "))
  if choice.lower() == "best friend":
    print("You let your best friend amputate your toes.")
    print("")
    print("But your friend stares down at you with a strange look. 'You didn't listen to me, and now you will pay the price.'")
    print("")
    print("They walk away from you, and the last thing you see is the fateful can of beefaroni.")
    print("")
    print("Was that the right choice?")
    print("")
    print("your path: BEACH, EAT beefaroni, BEST FRIEND amputates")
  elif choice == "yourself":
    print("You chose to trust yourself to amputate your toes.")
    print("")
    print("You successfully operate on yourself. You are no longer poisoned! You are mentally scarred, though.")
    print("")
    print("The rest of the group was too far gone to be saved. You and your best friend make it a few more hours before dying of starvation.")
    print("")
    print("Was that the right choice?")
    print("")
    print("Your path: BEACH, EAT beefaroni, SELF-amputate")

start()