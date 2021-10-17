

def get_team_avg_score(team_scores):
    """
    Calculate the avg team Score
    @param team_scores:
    @return: avg team Score
    """
    total_count = 0
    goal_count = 0
    for score in team_scores:
        if score['activity'] == 1:
            goal_count = score['activity_count']
            total_count = total_count + score['activity_count']
        if score['activity'] == 0:
            total_count = total_count + score['activity_count']
    if total_count is not None:
       avg_score = round((goal_count / total_count) * 100,2)
    else:
       avg_score = 0
    return avg_score