import os

class Dice:
    def init():
        self.extra_rolls = get_dice(1000)

    def get_dice(number_of_dice):
        """Try to get 'number_of_dice'. This will attempt to get those dice, but you will want to pull extrax from 'extra_rolls'

        """
        dice_bytes = os.urandom(number_of_dice)
        filtered_dice = filter(lambda x: x if x<252 else False, map(ord, dice_bytes))
        modded_dice = list(map(lambda x: x%6, filtered_dice))
        return modded_dice

    def get_exact_dice(number_of_dice):
        cur_dice = get_dice(number_of_dice)
        while len(cur_dice) != number_of_dice:
            cur_dice += get_dice(number_of_dice - len(cur_dice))
        try:
            assert(len(cur_dice) == number_of_dice)
        except AssertionError as e:
            print('Error: Number of dice generated are more than asked for.')

        return cur_dice

    def add_to_extra_rolls(number_of_dice):
        self.extra_rolls += get_dice(number_of_dice)

    def roll(num_dice):
        if num_dice > len(self.extra_rolls):
            add_to_extra_rolls(1000)
        dice_to_return = self.extra_rolls[:num_dice]
        del self.extra_rolls[:num_dice]
        return dice_to_return
        
