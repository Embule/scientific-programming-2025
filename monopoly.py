import random
import matplotlib.pyplot as plt

board_values= [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                0, 320, 200, 0, 350, 0, 400]
def throw_two_dice() :
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    return dice1 + dice2

def simulate_monopoly(starting_money) :
    position = 0
    throws = 0
    n_properties = 0
    possessions = [0] * 40

    # continue playing until all the properties are bought
    while n_properties < 28:
        position += throw_two_dice()
        throws += 1

        # after passing START, update position and give money
        if position > 39:
            position = position - 40
            starting_money += 200

        # allow player to buy a property if it is still free and they have enough money
        if board_values[position] != 0 and possessions[position] == 0 :
                if starting_money >= board_values[position]:
                    starting_money -= board_values[position]
                    possessions[position] = 1
                    n_properties += 1

    return throws

def simulate_monopoly_games(total_games, starting_money) :
    throws_list = []

    # simulate as many games as user specifies and save the final number 
    # of throws for collecting all properties
    for game in range(0, total_games):
        number_of_throws = simulate_monopoly(starting_money)
        throws_list.append(number_of_throws)

    # take the average of throws from all the simulations
    avg = sum(throws_list) / len(throws_list)

    print(f'Monopoly simulator: 1 player, {starting_money} euros starting money, Trump mode We simulated {total_games} games It took an average of {avg} throws for the player to collect all streets')
    return avg

if __name__ == '__main__':
    simulate_monopoly_games(2500, 1500)