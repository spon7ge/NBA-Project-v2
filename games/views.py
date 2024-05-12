from django.shortcuts import render,redirect
from .nba_client import *
from .forms import PlayerForm

def player_games(request, player_name): #grathers the players games from last season and full_name to display on top
    try:
        all_games = get_player_game_log(player_name)
        player_info = get_player_info(player_name)
        player_full_name = player_info['full_name']
        player_team_name = player_info['team_name']
        player_team_city = player_info['team_city']
        player_position = player_info['position']

    except Exception as e:
        # Handle error: log it and create an empty context or redirect
        all_games = []
        player_full_name = None

    display_all = request.GET.get('all', 'no') == 'yes'  # Check if 'all' parameter is set to 'yes'
    if display_all:
        games = all_games
    else:
        games = all_games[:5]  # Adjust this according to how your data is ordered

    context = {
        'player_name': player_full_name,
        'games': games,
        'display_all': display_all,
        'position':player_position,
        'team_name':player_team_name,
        'team_city': player_team_city  
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