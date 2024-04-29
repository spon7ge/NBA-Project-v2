from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog

def get_player_game_log(player_name):
    # Find players by name
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        player_id = player_dict[0]['id']
        # Fetch player's game log
        gamelog = playergamelog.PlayerGameLog(player_id=player_id)
        return gamelog.get_data_frames()[0]  # Return DataFrame of game logs
    return None
