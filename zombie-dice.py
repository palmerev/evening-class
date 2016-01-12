#! /usr/bin/env python3

from random import randint, sample, shuffle


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
        self.damage = 0

    def add_brains(self, num):
        self.brains += num

    def add_damage(self, num):
        self.damage += num


class Game():
    def __init__(self, players=None):
        if players is not None:
            self.players = players
        else:
            self.players = [Player('Player 1'), Player('Player 2')]
        self.current_player = self.players[0]
        self.dice = self.create_dice()
        self.current_round = 1
        self.round_status = 'in progress'

    def create_dice(self):
        dice = [ZombieDie('GREEN') for x in range(6)] + [ZombieDie('YELLOW') for x in range(4)] + [ZombieDie('RED') for x in range(3)]
        shuffle(dice)
        return dice

    def refill_dice_cup(self):
        print("refilling dice cup, but not really")

    def take_dice(self, num):
        # TODO: handle empty dice cup
        taken = self.dice[:num]
        self.dice = self.dice[num:]
        if len(self.dice) == 0:
            self.refill_dice_cup()

    def do_player_turn(self):
        player = self.current_player
        print("{}, press any key to roll.")
        input()
        current_dice = self.take_dice(3)
        # display dice
        print("\nYou rolled: {}".format(current_dice))
        # check for three shotguns

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
