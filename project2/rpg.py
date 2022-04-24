#!/usr/bin/python3

def showInstructions():
  #print a main menu and the commands
  print('''
MIDNIGHT TRAIN
========
Commands:
  go [direction]
  get [item]
=======
You awake to the cruel stench of death. The train you were taking home after work has been overrun by undead creatures. As far as you know, you are the only survivor. Find a way to stop the train and escape with your life!
''')
def showStatus():
  #print the player's current status
  print('---------------------------')
  print('LOCATION: ' + currentRoom)
  #print the current inventory
  print('ITEMS: ' + str(ITEMS))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
ITEMS = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Cab' : {
                  'south' : 'Engine Room',
                  'item' : 'zombie'
                },

            'Engine Room' : {
                  'north' : 'Cab',
                  'south' : 'Passenger Car I',
                  'item'  : 'coal shovel'
                },
            'Passenger Car I' : {
                  'north' : 'Engine Room',
                  'south': 'Passenger Car II',
                  'west' : 'Outside'
               },
            'Passenger Car II' : {
                  'north' : 'Passenger Car I',
                  'south' : 'Passenger Car III',
                  'item' :  'zombie'
               },
            'Passenger Car III' : {
                  'south' : 'Crew Car',
                  'north' : 'Passenger Car II'
            },
            'Crew Car' :{
                  'south' : 'Caboose',
                  'north' : 'Passenger Car III',
                  'item' : 'keycard'
                  },
            'Caboose'  :{
                  'north' : 'Crew Car'
                  },
            'Outside'  :{
                  'east' : 'Passenger Car I'
                  }
                }
#start the player in the Hall
currentRoom = 'Passenger Car I'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      ITEMS += [move[1]]
      #display a helpful message
      print(move[1] + ' added to inventory!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  ## Define how a player can win
  if currentRoom == 'Cab' and 'keycard' in ITEMS:
    print('You enter the card into the terminal and flip an important looking switch to shut off the engine. Congratulations! You stopped the train...You should try taking the exit in the first passenger car now!')

  ## If a player enters a room with a zombie
  elif 'item' in rooms[currentRoom] and 'zombie' in rooms[currentRoom]['item'] and 'coal shovel' not in ITEMS:
    print('ARGHHHHHH! You are attacked and bitten by a zombie...YOU DIED.')
    break
  ## If a player enters a room with a zombie and a weapon
  elif 'item' in rooms[currentRoom] and 'zombie' in rooms[currentRoom]['item'] and 'coal shovel' in ITEMS:
      print('You encounter a zombie and bash it with the shovel until it stops moving!')
      del rooms[currentRoom]['item']
  ## End of game/goal area
  elif currentRoom == 'Outside':
      print('FREEDOM! You sigh in relief before hearing a whistling sound in the distance. What is that? The government has decided to launch a military strike at the train before it reaches the city...damn, YOU DIED.')
      break
      
