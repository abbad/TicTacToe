from django.db import models
from mysite.account.models import Account
from django.core.exceptions import ObjectDoesNotExist

class TicTacToe(models.Model):


    @classmethod
    def get_number_of_games_played(cls, user_name="AI"):
        """
        :return: number of games played for a certain user.
        """
        # get player
        try:
            user = Account.objects.get(username=user_name)
        except ObjectDoesNotExist:
            #  If AI does not exist create it.
            if user_name=="AI":
                user = Account.objects.create(username="AI")
                user.save()

        player_wins_losses = user.wins + user.losses + user.draws
        return player_wins_losses

    @classmethod
    def get_number_of_losses(cls, user_name="AI"):
        """
        Get number of losses for a certain user.
        :param user_name:
        :return:
        """

        player = Account.objects.get(username=user_name)

        return player.losses


    @classmethod
    def get_number_of_wins(cls, user_name="AI"):
        """
        get number of wins for a certain user.
        :param user_name:
        :return:
        """
        player = Account.objects.get(username=user_name)
        return player.wins

    @classmethod
    def add_win(cls, user_name="AI"):
        """
        add a win for a certain user.
        :param user_name:
        """
        player = Account.objects.get(username=user_name)
        player.wins += 1
        player.save()


    @classmethod
    def add_loss(cls, user_name="AI"):
        """
        add a loss for a certain user.
        :param user_name:
        """
        player = Account.objects.get(username=user_name)
        player.losses += 1
        player.save()

    @classmethod
    def add_draw(cls, user_name="AI"):
        """
        add a draw.
        # TODO: mark who it was between.
        :param user_name:
        :return:
        """
        player = Account.objects.get(username=user_name)
        player.draws += 1
        player.save()


    @classmethod
    def get_total_draws(cls, user_name="AI"):
        """
        Return the number of draws.
        """
        player = Account.objects.get(username=user_name)
        return player.draws
