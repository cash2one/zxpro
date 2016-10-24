from django import template
from xhzx.models import MnTWy, MnTAd, MnTTa, MnTGroup, MnTGlobal, MnTAnswer, MnTZwh
register = template.Library()


@register.filter(name='get_zwh')
def get_zwh(value, arg):
    return MnTZwh.objects.get(value=value).text
