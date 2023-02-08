from django.shortcuts import render

from lib.cache import rds
from lib.http import render_json

from social.helper import recommend_users, like_someone, super_like_someone, regreted, users_liked_me, add_swipe_score, \
    get_top_n_swiped, get_recommend_user_from_redis

from social.models import Swiped
from vip.helper import need_permission


# Create your views here.
def index(request):
    return render_json(None)


"""
1. 用户登录, 向Celery 提交任务
    1. 加载我滑动过的人, 到缓存, 并添加过期时间
    执行推荐算法, 得到一批用户, 再将取到的用户与缓存中被滑动过的数据进行去重处理
    2. celery 将推荐结果添加到缓存
2. 用户获取推荐列表, 直接从缓存中获取
3. 如果缓存中没有数据
    从数据库中获取数据(将数据库作为一种备份的方案)
    
用户每滑动一个人, 直接将该用户ID添加到滑动过的列表(去重)
"""


def get_recommend_users(request):
    """获取推荐列表"""
    # 分页处理
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page

    user = request.user
    users = recommend_users(user)[start: end]  # 懒加载
    result = [user.to_dict() for user in users]
    return render_json(result)


def new_recommend_users(request):
    # 从redis中获取推荐列表
    users = get_recommend_user_from_redis(request.user)
    result = [u.to_dict() for u in users]
    return render_json(result)


def like(request):
    """喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    is_matched = like_someone(user, sid)
    add_swipe_score(sid, 'like')  # 添加滑动排行
    rds.srem('RCMD-%s' % request.user.id, sid)
    return render_json({'is_matched': is_matched})


def dislike(request):
    """不喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    Swiped.dislike(user.id, sid)
    add_swipe_score(sid, 'dislike')  # 添加滑动排行
    rds.srem('RCMD-%s' % request.user.id, sid)
    return render_json(None)


@need_permission('super_like')
def super_like(request):
    """超喜欢"""
    user = request.user
    sid = int(request.POST.get('sid'))
    is_matched = super_like_someone(user, sid)
    add_swipe_score(sid, 'superlike')  # 添加滑动排行
    rds.srem('RCMD-%s' % request.user.id, sid)
    return render_json({'is_matched': is_matched})


@need_permission('regret')
def regret(request):
    """反悔"""
    regreted(request.user)
    return render_json(None)


@need_permission('show_liked_me')
def show_liked_me(request):
    """显示喜欢我的"""
    users = users_liked_me(request.user)
    result = [u.to_dict() for u in users]
    return render_json({'result': result})


def get_friends(request):
    """获取好友列表"""
    result = [friend.to_dict() for friend in request.user.friends()]
    return render_json(result)


def hot_swiped(request):
    """获取排行榜榜单"""
    data = get_top_n_swiped(10)
    for item in data:
        item[0] = item[0].to_dict()
    return render_json(data)
