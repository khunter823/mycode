#!/usr/bin/python3

def showInstructions():
  #print a main menu and the commands
  print('''
MIDNIGHT TRAIN
========
Commands:
  go [direction]
  get [item]
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
ITEMS = ["Flashlight"]

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Cab' : {
                  'south' : 'Engine Room',
                  'item'  : 'key'
                },

            'Engine Room' : {
                  'north' : 'Cab',
                  'south' : 'Passenger Car I',
                  'item'  : 'Coal Shovel'
                },
            'Passenger Car I' : {
                  'north' : 'Engine Room',
                  'south': 'Passenger Car II',
               },
            'Passenger Car II' : {
                  'north' : 'Passenger Car I',
                  'south' : 'Passenger Car III',
               },
            'Passenger Car III' : {
                  'south' : 'Crew Car',
                  'north' : 'Passenger Car II',
                  'item' : 'cookie'
            },
            'Crew Car' :{
                  'south' : 'Caboose',
                  'north' : 'Passenger Car III',
                  'item' : 'Keycard'
                  },
            'Caboose'  :{
                  'north' : 'Crew Car',
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
  if currentRoom == 'Cab' and 'Keycard' in ITEMS:
    print('You enter the card into the terminal and flip an important looking switch to shut off the engine. Congratulations! Youstopped the train....................................but what is that scratching sound behind the door you just came through??')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
