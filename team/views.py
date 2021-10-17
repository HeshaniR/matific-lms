
from django.http import JsonResponse

from game.models import  GameActivity
from team.models import Team
from django.views.decorators.http import require_http_methods

from team.utils import get_team_avg_score


@require_http_methods(["GET"])
def index(request):
    """Get all teams"""
    teams = Team.objects.get_teams()
    try:
        return JsonResponse({
            'success': True,
            'data': teams,
            'total': len(teams)
        }, safe=False)
    except:
        return JsonResponse({
            'success': False,
            'data': None,
            'total': 0
        }, safe=False)


@require_http_methods(["GET"])
def get_team_details(request, team_id):
    """Get team details by Id"""
    team = Team.objects.get_team_by_id(team_id)
    team_scores = GameActivity.objects.get_team_scores(team_id)
    data = {
        'team_name' : team.name,
        'avg_score': get_team_avg_score(team_scores)
    }
    try:
        return JsonResponse({
            'success': True,
            'data': data,
            'total': len(data)
        }, safe=False)
    except:
        return JsonResponse({
            'success': False,
            'data': None,
            'total': 0
        }, safe=False)
