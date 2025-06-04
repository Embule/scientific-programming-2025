import random
import matplotlib.pyplot as plt

board_values= [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180,
                0, 180, 200, 0, 220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300,
                0, 320, 200, 0, 350, 0, 400]
def throw_two_dice() :
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    return dice1 + dice2

# function for processing a throw, buying properties and updating position
def process_turn(position, money, n_properties, possession_count) :
    position += throw_two_dice()

    # after passing START, update position and give money
    if position > 39 :
        position -= 40
        money += 200

    # allow player to buy a property if it is still free and they have enough money
    if board_values[position] != 0 and possession_count[position] == 0 :
            if money >= board_values[position]:
                money -= board_values[position]
                possession_count[position] = 1
                n_properties += 1

    return position, money, possession_count, n_properties


def simulate_monopoly(starting_money_p1, starting_money_p2) :
    position_p1 = 0
    position_p2 = 0
    n_properties_p1 = 0
    n_properties_p2 = 0
    possession_count = [0] * 40

    # processes turns until all properties are sold 
    while possession_count.count(1) < 28:
        position_p1, starting_money_p1, possession_count, n_properties_p1 = process_turn(
            position_p1, starting_money_p1, n_properties_p1, possession_count)
        position_p2, starting_money_p2, possession_count, n_properties_p2 = process_turn(position_p2, starting_money_p2, n_properties_p2, possession_count)
  
    # the differenc in number of properties between the players
    delta = n_properties_p1 - n_properties_p2

    return delta

def simulate_monopoly_games(total_games, starting_money_p1, starting_money2) :
    delta_list = []

    # simulate as many games as user specifies and save the final number 
    # of throws for collecting all properties
    for game in range(0, total_games):
        delta = simulate_monopoly(starting_money_p1, starting_money2)
        delta_list.append(delta)

    avg = sum(delta_list) / len(delta_list)

    return avg

def equilibrium() :
    print("Monopoly simulator: 2 players\n")
    starting_money_p1 = 1500
    starting_money_p2 = 1500
    extra_money = [50, 100, 150, 200, 250, 300]
    avg_list = []

    # simulate games and give player 2 extra strting money after each game
    for i in extra_money :

        # after each round of simulations, save the average difference of owned properties to a list
        avg = simulate_monopoly_games(10000, starting_money_p1, starting_money_p2)
        starting_money_p2 = 1500 + i
        avg_list.append(avg)

        print(f'Starting money [{starting_money_p1},{starting_money_p2}]: player 1 on average {avg} more streets (player 2 {i} euros extra)')

    # loop through extra money while looking ahead of one step due to 
    # checking the previous and current value in the list simultaneously
    for i in range(len(extra_money) - 1):
        # checks whether there is a point where the sign changes to negative (equilibrium)
        if avg_list[i] > 0 and avg_list[i + 1] <= 0:
            # assigns the coordinates of sign change point for
            # both variables (extra money and average difference)
            x1, y1 = extra_money[i], avg_list[i]
            x2, y2 = extra_money[i + 1], avg_list[i + 1]
            # use linear equation to calculate the exact point of equilibrium
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            # solves the point for extra money where the average is zero
            equilibrium_point = -intercept / slope
            equilibrium_rounded = round(equilibrium_point / 50) * 50

    # plot the extra money and averages association
    # plt.plot(extra_money, avg_list, marker='o', linestyle='-', color='blue')
    # plt.axhline(0, color='gray', linestyle='--', linewidth=1)
    # plt.xlabel("Extra starting money player 2")
    # plt.ylabel("Average difference in number of streets")
    # plt.show()

    print(f'\nOn average, if player 2 receives {equilibrium_rounded} euros more starting money, both players collect an equal number of streets')

if __name__ == '__main__':
    equilibrium()