from django import template

from applications.models import Email, AuthUser, AuthUserGroups

register = template.Library()


@register.simple_tag(takes_context=True)
def get_staff(context):
    try:
        user = context['user']
        if user:
            user_id = AuthUser.objects.get(username=user)
            group_id = AuthUserGroups.objects.get(user_id=user_id)
            return AuthUserGroups.objects.filter(group_id=group_id.group_id)
        else:
            return False
    except:
        pass


@register.simple_tag()
def get_count_new_order():
    return Email.objects.filter(open_order=False, close_order=False).count()


@register.simple_tag(takes_context=True)
def get_count_in_work(context):
    try:
        user = context['user']
        if user:
            user_id = AuthUser.objects.filter(username=user).values('id')
            return Email.objects.filter(open_order=True, specialist=user_id[0]['id']).count()
        else:
            return False

    except:
        pass



