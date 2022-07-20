
def is_cardlist_admin(request):
    return request.employee.permissions.filter(code='cardlist_admin').exists()