def main():
    def game_instructions():  # Displays game instructions at the start of game and never again
        print("\n----------------------------------------\n"
              "Welcome to my text based game project!\n"
              "Movement directions: 'go' north, east, south, west.\n"
              "Add an item to your inventory: 'get' item\n"
              "to quit, type 'exit game'.\n"
              "You are currently in the Garage.\n"
              "----------------------------------------\n")

    def current_status():  # Displays players status after every move.
        while True:
            if current_room == 'exit':
                print("\nThanks for playing. You have left the game.")
                break
            else:
                print("\n-------------------------------------")
                print(f"You are in the {current_room}")
                if rooms_in_home[current_room]['Item'] not in item_inventory:  # If statement to let the player know if they have gathered the item in the room already or not.
                    print(f"You see {rooms_in_home[current_room]['Item']}")
                else:
                    print('You already have the item from this room.')
                if len(item_inventory) == 0:  # If statement that displays different text depending on if the player has gathered items or not.
                    print("you have not picked any items up yet.")
                else:
                    print(f"You already have {', '.join(item_inventory)}")
                print(f"-------------------------------------\n")
            break

    def player_move(direction, room='Garage'):  # Allows the player to move room to room
        while direction in rooms_in_home[room].keys():
            if direction in rooms_in_home[room].keys():
                return rooms_in_home[room][direction]
            else:
                print('Invalid')
                continue

    def player_get(item, room='Garage'):  # Allows the player to pick up an item if the item is in their current room
        while item in rooms_in_home[room].values():
            if item in rooms_in_home[room].values():
                return rooms_in_home[room]['Item']
            else:
                print('Invalid Input. Please try again.\n')

    def roll_credits():  # This gives the player the option to play again or not.
        while current_room == 'Porch':
            if current_room == 'Porch':
                if len(item_inventory) != 6:
                    losing_end = input("\n-------------------------------------"
                                       "\nYou lost! You need all six items to be prepared to go out! "
                                       "\n-------------------------------------\n"
                                       "\nWould you like to play again? ")
                    if losing_end[0] == 'yes' or "Yes":
                        main()
                    elif losing_end[0] == 'no' or 'No':
                        break
                else:
                    winning_end = input("\n-------------------------------------"
                                        "\nyou win! You were totally prepared to go to Target!"
                                        "\n-------------------------------------\n"
                                        "\nWould you like to play again? ")
                    if winning_end == 'Yes' or 'yes':
                        main()
                    elif winning_end[0] == 'no' or 'No':
                        break

    rooms_in_home = {
        'Garage': {'east': 'Living Room', 'Item': 'no item'},
        'Living Room': {'north': 'Bedroom', 'east': 'Kitchen', 'south': 'Mud Room', 'west': 'Garage', 'Item': 'keys'},
        'Bedroom': {'east': 'Bathroom', 'south': 'Living Room', 'Item': 'watch'},
        'Kitchen': {'north': 'Closet', 'west': 'Living Room', 'Item': 'snacks'},
        'Mud Room': {'north': 'Living Room', 'east': 'Porch', 'Item': 'shoes'},
        'Closet': {'south': 'Kitchen', 'Item': 'pocketknife'},
        'Bathroom': {'west': 'Bedroom', 'Item': 'wallet'},
        'Porch': {'End Game': 'Game Over'},
        'exit': {'Exit': 'Exit'}}

    item_inventory = []  # Inventory set to blank
    directions = ['north', 'east',  'south', 'west', 'exit']  # List that is read every round to determine if input makes sense
    current_room = 'Garage'  # Starting point
    game_instructions()
    while True:
        user_input = input('What is your next move? ').lower().split()  # I used .lower() as case control. .split() to validate input.
        if len(user_input) != 2:  # Ensures player provides two statements
            print('\nYour input has to be two statements long. Please see instructions.')
            current_status()
            continue
        if user_input[0] == 'go':  # Activates current room function. Allowing player to move rooms
            if user_input[1] not in directions:
                print("\nThat's not a direction!")
                current_status()
                continue
            elif user_input[1] in rooms_in_home[current_room].keys():
                current_room = player_move(user_input[1], current_room)
            else:
                print('Invalid Input. Try again.\n')
                continue
            if current_room == 'Porch':  # End of game. Player is provided option to play again
                roll_credits()
        elif user_input[0] == 'get':  # Activates player get function. Allowing player to get items.
            if user_input[1] not in rooms_in_home[current_room].values():
                print("\nThat's not the item you need.")
            elif user_input[1] in rooms_in_home[current_room].values():
                item_inventory.append(player_get(user_input[1], current_room))
                current_status()
                continue
            else:
                pass
        elif user_input[0] == 'exit':  # Lets player quit if they wish to.
            current_room = 'exit'
            current_status()
            break
        else:
            print('Invalid input. Please try again.\n')
            continue
        current_status()


if __name__ == '__main__':  # Runs script above.
    main()
