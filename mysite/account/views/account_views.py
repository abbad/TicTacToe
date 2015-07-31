from django.views.generic import View
from mysite.tictactoe.models import Account
import json
from django.http import HttpResponse

__author__ = 'Ahmad Abbad'


class AddUserView(View):
    """
        View for adding a user.
    """
    def post(self, request):
        error = False
        user_name = request.POST.get('username', None)

        if user_name:
            Account.objects.create(username=user_name)
        else:
            error = True

        context = {'error': error}

        return HttpResponse(json.dumps(context))