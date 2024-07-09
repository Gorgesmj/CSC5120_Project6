# Project 4
# Author: Geoffrey Tan
# Date: 6/24/2024
# Create a game Battle Sim

from mugwump import Mugwump
from warrior import Warrior
from ironman import IronMan
from michael_new_char import MichaelNewChar
from chris_new_char import ChrisNewChar
from dice import Die
import csv
import pandas as pd

d10 = Die(10)
# : Please change the name at here
c1Name = "Mugwump"
c2Name = "Warrior"
c3Name = "IronMan"
c4Name = "michaelNewChar"
c5Name = "chrisNewChar"


class Player():
    def __init__(self, charNum: int = 1, is_player: bool = True):
        self.chara_choose = charNum
        self.is_player = is_player
        self.className = None
        self.nickName = None


def main():  # not testable
    keep_playing = True
    victor = ""
    while keep_playing:
        # print the introduction and rules
        intro()
        # initialize game
        # Initialize the Warrior and Mugwump classes, set the current victor to "none"
        # change to player1 and player2, we ask the user what is what
        player_1 = Player()
        player_2 = Player()
        # the set up function will ask the users to select which player do they want to be and which one is the ai or
        # real player
        startANewGame = newGameAsk()
        if startANewGame:
            setUpNewGame(player_1, player_2)
            print(player_1.chara_choose)
            print(player_2.chara_choose)
            p1 = chooseChar(player_1)
            p2 = chooseChar(player_2)
            # if player_1.chara_choose == 1:
            #     p1 = Warrior(player_1.is_player)  ## player_1 .is_plaer returns the vlaue of 1 if it is a real player.
            # else:
            #     p1 = Mugwump(player_1.is_player)
            #
            # if player_2.chara_choose == 1:
            #     p2 = Warrior(player_2.is_player)
            # else:
            #     p2 = Mugwump(player_2.is_player)
            p1.setName("Please set a name for player 1: ")
            player_1.nickName = p1.name
            p2.setName("Please set a name for player 2: ")
            player_1.nickName = p2.name
        else:
            print("Load data from previous game")

        victor = "none"

        while victor == "none" and keep_playing == True:
            report(p1, p2)
            victor = battle(p1, p2)
            report(p1, p2)

            if victor != "none":  # one of them has won
                report(p1, p2)
                victory(victor)
                # ask to play again
                keep_playing = playAgain()

            else:
                # ask do they want to continue play or store it as CSV
                pauseSave = pauseAndSave()
                if pauseSave:
                    # get the data from the class and output it as CSV
                    playerName1, isRealPlayer1, player1_currentHP, player1_maxHP = p1.outputData()
                    playerName2, isRealPlayer2, player2_currentHP, player2_maxHP = p2.outputData()
                    player1Class = player_1.className
                    player2Class = player_1.className
                    # format the data
                    dataMessages = [[player1Class, playerName1, isRealPlayer1, player1_currentHP, player1_maxHP],
                                    [player2Class, playerName2, isRealPlayer2, player2_currentHP, player2_maxHP]]
                    columns = ["Class Name", "Player Name", "Real Player ?", "Current HP", "Max HP"]

                    df = pd.DataFrame(dataMessages, columns=columns)
                    csv_file_path = './gamingData.csv'
                    df.to_csv(csv_file_path, index=False)
                    print(f"Gaming data saved to: {csv_file_path}")
                    keep_playing = False

    print("Thank you for playing Battle Simulator 3000!")


def intro():  # not testable
    # Write a suitable introduction to the game

    print("Welcome to Battle Simulator 4000! The world's more low tech battle simulator!"
          "You can select to be a Valiant Warrior defending your humble village from an evil Mugwump! Fight bravely, "
          "or you can be the evil Mugwump to destroy a village "
          "\n The warrior has a Trusty Sword, which deals decent damage, but can be tough to hit with sometimes. "
          "The warrior also has a Shield of Light, which is not as strong as your sword, but is easier to deal "
          "damage with."
          "\n the Mugwump also have 2 damage skills as well with one additional healing skill "
          "\n this game support both PvP and PvE and EvE"
          "\nLet the epic battle begin!")


def setUpNewGame(player1: Player, player2: Player):
    print("Please make the selection for player 1 ")
    print(f"1 - {c1Name}")
    print(f"2 - {c2Name}")
    print(f"3 - {c3Name}")
    print(f"4 - {c4Name}")
    print(f"5 - {c5Name}")
    char1 = int(input())
    if char1 > 5 or char1 < 1:
        char1 = 2
    player1.chara_choose = char1
    print("is this an actual player or AI? ""\n 1 for Real Player and 0 for AI""\n Default is Real Player")
    player1.is_player = bool(int(input()))

    print("Please make the selection for player 2 ")
    print(f"1 - {c1Name}")
    print(f"2 - {c2Name}")
    print(f"3 - {c3Name}")
    print(f"4 - {c4Name}")
    print(f"5 - {c5Name}")
    char2 = int(input())
    if char2 > 5 or char2 < 1:
        char2 = 2
    player2.chara_choose = char2
    print("is this an actual player or AI? ""\n 1 for Real Player and 0 for AI""\n Default is Player")

    player2.is_player = bool(int(input()))


"""
   This method handles the battle logic for the game.
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
   @return The name of the victor, or "none", if the battle is still raging on
"""


def battle(player1, player2):  # not testable?
    # determine who attacks first (Roll! For! Initiative!) and store the result
    cur_inititive = initiative()  # this a 1 or 2
    # attack code
    # If the Warrior attacks first
    if cur_inititive == 1:
        # P1 attacks and assigns the resulting damage to the P2

        print(f"The Player 1 ({player1.name})attacks first!")

        damage = player1.attack()  #calculate damage caused by P1
        if (damage > 0):
            player2.takeDamage(damage)  # apply damage to P2
        else:  # the P1 may have healed itself, so have to check
            player1.takeDamage(damage)  #healing because it is negative

        # Check if the P2 has been defeated
        if (player2.hitPoints <= 0):
            return "player1"
        # If not, player2 attacks!
        damage = player2.attack()
        # the P2 may have healed itself, so have to check
        if (damage > 0):
            player1.takeDamage(damage)
        else:  # P2 healed
            player2.takeDamage(damage)  #healing because it is negative

        if (player1.hitPoints == 0):
            return "player2"  #P2 wins!
    else:  # P2 attacks first!

        print(f"Player 2 ({player2.name}) attacks first!")
        # P2 attacks and assigns the resulting damage to the P1
        damage = player2.attack()
        # the P2 may have healed itself, so have to check
        if (damage > 0):
            player1.takeDamage(damage)
        else:  # P2 healed
            player2.takeDamage(damage)  # healing because it is negative

        if (player1.hitPoints == 0):
            return "mugwump"  # P2 wins!

        damage = player1.attack()  # calculate damage caused by P1
        if (damage > 0):
            player2.takeDamage(damage)  # apply damage to P2
        else:  # the P1 may have healed itself, so have to check
            player1.takeDamage(damage)  #healing because it is negative

        # Check if the P2 has been defeated
        if (player2.hitPoints <= 0):
            return "player2"

    # If neither combatant is defeated, the battle rages on!
    return "none"


"""
   This method reports the status of the combatants
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
 """


def report(p1, p2):  # not testable
    print(f"Player 1 {p1}")
    print(f"Plater 2 {p2}")


"""
   Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if the warrior goes first, 2 if the mugwump goes first
 """


# this has randomness, how can we test it? Can we set a seed for the random number generator?
def initiative() -> int:  # return 1 for warrior, 2 for mugwump
    # roll for initiative for both combatants
    # until one initiative is greater than the other
    player1_initiative = d10.roll()
    player2_initiative = d10.roll()
    while player1_initiative == player2_initiative:
        player1_initiative = d10.roll()
        player2_initiative = d10.roll()

    if player1_initiative > player2_initiative:
        return 1  # warrior goes first
    else:
        return 2  # mugwump goes first


"""
   This method declares the victor of the epic battle
   @param victor the name of the victor of the epic battle
 """


def victory(victor):  # not testable (or at least we won't worry about testing it)
    if (victor == "player1"):
        print("Player 1 win ")
    else:
        print("Plater 2 win")


"""
   This method asks the user if they would like to play again
   @param in Scanner
   @return true if yes, false otherwise
 """


def playAgain() -> bool:  # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    choice = input("Would you like to play again (yes/no)?")
    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        return True
    return False


def pauseAndSave() -> bool:
    choice = input("Would you like to pause and save the game?(yes/no)?")
    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        return True
    return False


def newGameAsk() -> bool:  # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a
    # -function-with-input-call
    choice = input("Do you want to start a new game (yes/no)?")
    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        return True
    return False


def chooseChar(player: Player):
    try:
        match player.chara_choose:
            case 1:
                player.className = c1Name
                return Mugwump(player.is_player)
            case 2:
                player.className = c2Name
                return Warrior(player.is_player)
            case 3:
                player.className = c3Name
                return IronMan(player.is_player)
            case 4:
                player.className = c4Name
                return MichaelNewChar(player.is_player)
            case 5:
                player.className = c5Name
                return ChrisNewChar(player.is_player)
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
