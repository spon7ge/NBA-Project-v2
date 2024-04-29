from django.shortcuts import render,redirect
from .nba_client import get_player_game_log
from .forms import PlayerForm

def player_games(request, player_name):
    context = {
        'player_name': player_name,
        'games': get_player_game_log(player_name)
    }
    return render(request, 'games/player_games.html', context)

def home(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data['player_name']
            return redirect('player_games', player_name=player_name)
    else:
        form = PlayerForm()
    return render(request, 'games/home.html', {'form':form})