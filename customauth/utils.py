from game.models import GameActivity


def get_player_avg_score(player_id):
    """
    Get the avg score of player (goal/try*100)
    @param player_id: str
    @return: avg score
    """
    player_score = GameActivity.objects.get_player_scores(player_id)
    total_count = 0
    goal_count = 0
    player_avg_score =0
    for score in player_score:
        if score['activity'] == 1:
            goal_count = score['activity_count']
            total_count = total_count + score['activity_count']
        if score['activity'] == 0:
            total_count = total_count + score['activity_count']
    if total_count != 0:
        player_avg_score = (goal_count / total_count) * 100
        return player_avg_score
    else:
        return player_avg_score


def get_players_by_filter(players,filter):
    """
    get filtered players by avg score
    @param players: MyUser
    @return: filtered_players :List[MyUser]
    """
    filtered_players = []
    for player in players:
        player_avg_score = get_player_avg_score(player['id'])
        player['avg_score'] =player_avg_score
        if int(player['avg_score']) > filter:
            filtered_players.append(player)
    return filtered_players


def get_player_related_details(players):
    """
    Get player related details team,avg score
    @param players: MyUser
    @return: detailed player :List[MyUser]
    """
    detailed_player =[]
    for player in players:
        player_avg_score = get_player_avg_score(player['id'])
        player['avg_score'] = player_avg_score
        detailed_player.append(player)
    return detailed_player



