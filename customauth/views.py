from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponseForbidden
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import check_password

from customauth.models import MyUser
from customauth.utils import get_player_related_details, get_players_by_filter
from team.models import Team


@require_http_methods(["POST"])
@csrf_exempt
def login_user(request):
    """Login the User"""
    if request.user.is_authenticated:
        return JsonResponse({
            'success': True,
            'message': 'User is already logged in'
        }, safe=False)

    username = request.POST['username']
    password = request.POST['password']
    user = MyUser.objects.authenticate(username, password)

    if user is not None:
        login(request, user)
        user.login_count = user.login_count + 1
        user.login_time = now()
        user.save()
        return JsonResponse({
            'success': True,
            'message': 'User is logged in successfully'
        }, safe=False)
    else:
        return HttpResponseForbidden()


@require_http_methods(["GET"])
@csrf_exempt
def logout_user(request):
    """Logout the User"""
    logout(request)
    return JsonResponse({
        'success': True,
        'message': 'User is logged out successfully'
    }, safe=False)


@require_http_methods(["POST"])
@csrf_exempt
def create(request):
    """create and save the new user"""
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        dob = request.POST['date_of_birth']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_type = request.POST['user_type']
        height = request.POST['height']
        team_id = request.POST['team_id']

        MyUser.objects.create_user(
            username, password, email, dob, first_name, last_name, user_type, height, team_id
        )

        return JsonResponse({
            'success': True,
            'total': 1
        }, safe=False)

    except Exception as error:
        return JsonResponse({
            'success': False,
            'data': None,
            'error': str(error),
        }, safe=False)


@require_http_methods(["GET"])
def get_player_details(request, player_id):
    """
    Get Player Details
    @param request:
    @param player_id:
    @return: player
    """
    try:
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        player, message, success = MyUser.objects.get_player_by_id(player_id, request)
        return JsonResponse({
            'success': True,
            'data': player,
            'total': len(player)
        }, safe=False)
    except:
        return JsonResponse({
            'success': False,
            'data': None,
            'total': 0
        }, safe=False)


@require_http_methods(["GET"])
def get_players(request):
    """Get list of all the players"""
    try:
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        players, message, success = MyUser.objects.get_players(request)
        if players:
            players = get_player_related_details(players)
            total = len(players)
        else:
            players = None
            total = 0
        return JsonResponse({
            'success': success,
            'message': message,
            'data': players,
            'total': total
        }, safe=False)
    except:
        return JsonResponse({
            'success': False,
            'error': 'Some thing went wrong',
            'total': 0
        }, safe=False)


@require_http_methods(["GET"])
def get_user_stats(request):
    """Get the user statistic related to login"""
    users_stats = MyUser.objects.get_user_stats()
    return JsonResponse({
        'success': True,
        'data': users_stats,
        'total': len(users_stats)
    }, safe=False)


@require_http_methods(["GET"])
def get_filtered_players(request, filter):
    """Get players filtered by avg score"""
    try:
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        players, message, success = MyUser.objects.get_players(request)
        if players:
            players = get_players_by_filter(players, filter)
            total = len(players)
        else:
            players = None
            total = 0
        return JsonResponse({
            'success': success,
            'message': message,
            'data': players,
            'total': total
        }, safe=False)
    except:
        return JsonResponse({
            'success': False,
            'error': 'Some thing went wrong',
            'total': 0
        }, safe=False)
