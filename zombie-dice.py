#! /usr/bin/env python3

from random import randint, shuffle


class ZombieDie():
    def __init__(self, color):
        self.color = color
        if self.color.upper() == 'GREEN':
            self.sides = ['B', 'B', 'B', 'F', 'F', 'S']
        elif self.color.upper() == 'YELLOW':
            self.sides = ['B', 'B', 'S', 'F', 'F', 'S']
        elif self.color.upper() == 'RED':
            self.sides = ['B', 'S', 'S', 'F', 'F', 'S']
        else:
            raise
        shuffle(self.sides)
        self.current_value = self.sides[0]

    def roll(self):
        self.current_value = self.sides[randint(0, len(self.sides) - 1)]
        return self.current_value

    def __str__(self):
        return '[' + str(self.current_value) + ']'


class Player():
    def __init__(self, name):
        self.name = name
        self.brains = 0

    def add_brains(self, num):
        self.brains += num

    def __str__(self):
        return "{}, Brains={}".format(self.name, self.brains)


class Game():
    def __init__(self, players=None):
        if players is not None:
            self.players = players
        else:
            self.players = [Player('Player 1'), Player('Player 2')]
        self.current_player = self.players[0]
        self.dice_in_cup = self.create_dice()
        self.dice_on_table = []
        # for holding a player's accrued brains if the dice cup is refilled
        self.player_brain_count = 0

    def create_dice(self):
        dice = [ZombieDie('GREEN') for x in range(6)] \
            + [ZombieDie('YELLOW') for x in range(4)] \
            + [ZombieDie('RED') for x in range(3)]
        shuffle(dice)
        return dice

    def refill_dice_cup(self):
        pass

    def take_dice(self, num):
        taken = []
        while len(self.dice_in_cup) > 0 and len(taken) < num:
            taken.append(self.dice_in_cup.pop())
        # there weren't enough dice
        if len(taken) < num:
            pass

    def do_player_turn(self):
        player = self.current_player
        shotguns = footprints = 0
        print("{}, press any key to roll.")
        input()
        dice_on_table = self.take_dice(3)
        values_showing = [die.current_value for die in dice_on_table]
        # display dice
        print("\nYou rolled: {}".format(current_dice))
        # check for three shotguns
        if values_showing.count('S') == 3:
            # end player's turn
            print("{}, you got shotgunned!")
            return
        else:
            shotguns += values_showing.count('S')
            brains += values_showing.count('B')
            footprints = values_showing.count('F')
            if footprints == 0:
                print("You ate {} brains, and took {} shotgun wounds this turn. Your turn is over.".format(self.player_brain_count, shotguns))
                player.brains += self.player_brain_count
            if footprints > 0:
                # player may continue and re-roll footprints
                print("You have {} brains, {} shotguns, and {} footprints this turn.".format(self.player_brain_count, shotguns, footprints))
                if not confirm("Continue? (y/n): "):
                    return

    def check_dice(self):
        pass

    def begin_round(self):
        print("--------------------")
        print("ROUND {}".self.current_round)
        print("--------------------\n")

    def end_round(self):
        for player in self.players:
            player.brains = 0
        self.current_player = self.players[0]


def confirm(prompt):
    choice = input(prompt)
    while True:
        choice = choice.lower()
        if choice == 'y' or choice.startswith('y'):
            return True
        elif choice == 'n' or choice.startswith('n'):
            return False
        else:
            choice = input(prompt)
