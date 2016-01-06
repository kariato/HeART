from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from dnadata.models import Family,DNAKit
#from tictactoe.models import Game


@login_required
def home(request):
    myFamilies = Family.objects.families_for_user(request.user)
    myDnakits = {}
    for family in myFamilies:
        myDnakits[family.user.id] = DNAKit.objects.kitsForFamily(family)
    #my_games = Game.objects.games_for_user(request.user)
    #active_games = my_games.filter(status="A")
    #finished_games = my_games.exclude(status="A")
    #waiting_games = active_games.filter(next_to_move=request.user)
    #other_games = active_games.exclude(next_to_move=request.user)
    #invitations = request.user.invitations_received.all()
    context = { 'myFamilies': myFamilies,
                'myDnakits': myDnakits } #'other_games': other_games,
    #            'waiting_games': waiting_games,
    #            'finished_games': finished_games,
    #            'invitations': invitations}
    return render(request, "user/home.html", context)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "user/signup.html"
    success_url = reverse_lazy('user_home')