from django.shortcuts import render,redirect
from .nba_client import get_player_game_log
from .forms import PlayerForm

def player_games(request, player_name):
    all_games = get_player_game_log(player_name)  # Assuming this returns a queryset or list
    display_all = request.GET.get('all', 'no') == 'yes'  # Check if 'all' parameter is set to 'yes'

    if display_all:
        games = all_games
    else:
        games = all_games[:5]  # Adjust this according to how your data is ordered

    context = {
        'player_name': player_name,
        'games': games,
        'display_all': display_all  # Pass whether all games are being displayed
    }
    return render(request, 'games/player_games.html', context)


def games(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player_name = form.cleaned_data['player_name']
            return redirect('player_games', player_name=player_name)
    else:
        form = PlayerForm()
    return render(request, 'games/home.html', {'form':form})







posts = [
    {
        'author': 'Alex Gonzalez - ESPN',
        'title': 'NBA blog post 1',
        'content': 'First post content',
        'data_posted': 'May 1, 2024'
    },
     {
        'author': 'Jane Doe - First Take',
        'title': 'NBA blog post 2',
        'content': 'Second post content',
        'data_posted': 'Apirl 28, 2024'
    }
]

def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'games/blog.html', context)