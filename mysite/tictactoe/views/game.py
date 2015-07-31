from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect, HttpResponse

from mysite.tictactoe.models import TicTacToe
import json
__author__ = 'Ahmad Abbad'


class HomeView(TemplateView):
    """
        Main page for running app.
    """

    def get(self, request, *args, **kwargs):
        self.template_name = 'tictactoe/index.html'

        total_number_of_games = TicTacToe.get_number_of_games_played()

        total_losses = TicTacToe.get_number_of_losses()

        total_wins = TicTacToe.get_number_of_wins()

        total_draws = TicTacToe.get_total_draws()

        context = {
            'total_number_of_games': total_number_of_games,
            'total_losses': total_losses,
            'total_wins': total_wins,
            'total_draws': total_draws,
        }

        return self.render_to_response(context)


class StartGame(TemplateView):

    def get(self, request, *args, **kwargs):
        self.template_name = 'tictactoe/game.html'
        return self.render_to_response({})


class AddWinView(View):
    """
        View to add a win.
    """

    def post(self, request, *args, **kwargs):
        # default to AI
        TicTacToe.add_win()

        return HttpResponse(json.dumps({}))


class AddLossView(View):
    """
        View for adding a loss
    """

    def post(self, request, *args, **kwargs):
        # defaults to AI
        TicTacToe.add_loss()
        return HttpResponse(json.dumps({}))


class AddDraw(View):
    """
        View for adding draw gamess
    """

    def post(self, request, *args, **kwargs):
        # defaults to AI
        TicTacToe.add_draw()
        return HttpResponse(json.dumps({}))