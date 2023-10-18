# # Example 1
# def a():
#     print("A")
 
# def b():
#     print("B")
 
# def c():
#     print("C")
 
# a()


# # Example 2
# def a():
#     b()
#     print("A")
 
# def b():
#     c()
#     print("B")
 
# def c():
#     print("C")
 
# a()



# # Example 3
# def a():
#     print("A")
#     b()
 
# def b():
#     print("B")
#     c()
 
# def c():
#     print("C")
 
# a()



# # Example 4
# def a():
#     print("A start")
#     b()
#     print("A end")
 
# def b():
#     print("B start")
#     c()
#     print("B end")
 
# def c():
#     print("C start and end")
 
# a()




# # Example 5
# def a(x):
#     print("A start, x =",x)
#     b(x + 1)
#     print("A end, x =",x)
 
# def b(x):
#     print("B start, x =",x)
#     c(x + 1)
#     print("B end, x =",x)
 
# def c(x):
#     print("C start and end, x =",x)
 
# a(5)



# # Example 6
# def a(x):
#     x = x + 1
 
# x = 3
# a(x)
 
# print(x)



# # Example 7
# def a(x):
#     x = x + 1
#     return x
 
# x = 3
# a(x)
 
# print(x)



# # Example 8
# def a(x):
#     x = x + 1
#     return x
 
# x = 3
# x = a(x)
 
# print(x)



# # Example 9
# def a(x, y):
#     x = x + 1
#     y = y + 1
#     print(x, y)
 
# x = 10
# y = 20
# a(y, x)



# # Example 10
# def a(x, y):
#     x = x + 1
#     y = y + 1
#     return x
#     return y
 
# x = 10
# y = 20
# z = a(x, y)
 
# print(z)


# # Example 11
# def a(x, y):
#     x = x + 1
#     y = y + 1
#     return x, y
 
# x = 10
# y = 20
# z = a(x, y)
 
# print(z)



# # Example 12
# def a(x, y):
#     x = x + 1
#     y = y + 1
#     return x, y
 
# x = 10
# y = 20
# x2, y2 = a(x, y) # Most computer languages don't support this
 
# print(x2)
# print(y2)



# # Example 13
# def a(my_data):
#     print("function a, my_data =  ", my_data)
#     my_data = 20
#     print("function a, my_data =  ", my_data)
 
# my_data = 10
 
# print("global scope, my_data =", my_data)
# a(my_data)
# print("global scope, my_data =", my_data)





# # Example 14
# def a(my_list):
#     print("function a, list =  ", my_list)
#     my_list = [10, 20, 30]
#     print("function a, list =  ", my_list)
 
# my_list = [5, 2, 4]
 
# print("global scope, list =", my_list)
# a(my_list)
# print("global scope, list =", my_list)




# # Example 15
# # New concept!
# # Covered in more detail in Chapter 12
# def a(my_list):
#     print("function a, list =  ", my_list)
#     my_list[0] = 1000
#     print("function a, list =  ", my_list)
 
# my_list = [5, 2, 4]
 
# print("global scope, list =", my_list)
# a(my_list)
# print("global scope, list =", my_list)






"""
This is a sample text-only game that demonstrates the use of functions.
The game is called "Mudball" and the players take turns lobbing mudballs
at each other until someone gets hit.
"""
 
import math
import random
 
 
def print_instructions():
    """ This function prints the instructions. """
 
    # You can use the triple-quote string in a print statement to
    # print multiple lines.
    print("""
Welcome to Mudball! The idea is to hit the other player with a mudball.
Enter your angle (in degrees) and the amount of PSI to charge your gun
with.
        """)
 
 
def calculate_distance(psi, angle_in_degrees):
    """ Calculate the distance the mudball flies. """
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance
 
 
def get_user_input(name):
    """ Get the user input for psi and angle. Return as a list of two
    numbers. """
    # Later on in the 'exceptions' chapter, we will learn how to modify
    # this code to not crash the game if the user types in something that
    # isn't a valid number.
    psi = float(input(name + " charge the gun with how many psi? "))
    angle = float(input(name + " move the gun at what angle? "))
    return psi, angle
 
 
def get_player_names():
    """ Get a list of names from the players. """
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True
 
    print()
    return players
 
 
def process_player_turn(player_name, distance_apart):
    """ The code runs the turn for each player.
    If it returns False, keep going with the game.
    If it returns True, someone has won, so stop. """
    psi, angle = get_user_input(player_name)
 
    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart
 
    # By looking ahead to the chapter on print formatting, these
    # lines could be made to print the numbers is a nice formatted
    # manner.
    if difference > 1:
        print("You went", difference, "yards too far!")
    elif difference < -1:
        print("You were", difference * -1, "yards too short!")
    else:
        print("Hit!", player_name, "wins!")
        return True
 
    print()
    return False
 
 
def main():
    """ Main program. """
 
    # Get the game started.
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)
 
    # Keep looking until someone wins
    done = False
    while not done:
        # Loop for each player
        for player_name in player_names:
            # Process their turn
            done = process_player_turn(player_name, distance_apart)
            # If someone won, 'break' out of this loop and end the game.
            if done:
                break
 
if __name__ == "__main__":
    main()