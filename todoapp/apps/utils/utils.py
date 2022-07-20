def is_cardlist_user(request):
    return request.user.groups.filter(name='cardlist_user').exists()


def is_cardlist_admin(request):
    return request.user.groups.filter(name='cardlist_admin').exists()


def in_dict(dic, key, default=None):
    res = None
    for k in dic:
        if isinstance(k, (list, tuple)):
            for x in k:
                if x == key:
                    res = dic[k]
                    break
            if res:
                break
        else:
            if k == key:
                res = dic[k]
                break
    return res or default