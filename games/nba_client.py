from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, playercareerstats, playerestimatedmetrics, commonplayerinfo
import numpy as np

def get_player_game_log(player_name):#get players game log for the season
    # Find players by name
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        player_id = player_dict[0]['id']
        # Fetch player's game log
        gamelog = playergamelog.PlayerGameLog(player_id=player_id)
        return gamelog.get_data_frames()[0]  # Return DataFrame of game logs
    return None

def get_player_id(player_name): #Finds the players ID
    player = players.find_players_by_full_name(player_name)
    return player[0]['id']

def player_career_stats(player_name): #gets players career stats for each season
    if player_name:
        player_id = get_player_id(player_name)
        data = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
        return data
    return None

def get_players_adv_metrics(player_name):
    data = playerestimatedmetrics.PlayerEstimatedMetrics(season='2023-24').get_data_frames()[0]
    player = get_player_id(player_name)
    return data.loc[data['PLAYER_ID'] == player]

def get_name(player_name):
    player = players.find_players_by_full_name(player_name)
    return player[0]['full_name']

