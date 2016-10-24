# coding:utf-8
from django import template
from django.utils.html import format_html
from xhzx.models import MnTZwh, MnTJiebie, MnTParty, MnTWy, MnTTa, MnTBljg_tian, MnTBljg_sqmy

register = template.Library()


@register.filter(name='get_zwh')
def get_zwh(value):
    try:
        return "专委会:%s" % MnTZwh.objects.get(value=value).text
    except:
        return ""


@register.filter(name='get_jiebie')
def get_jiebie(value):
    try:
        return "界别:%s" % MnTJiebie.objects.get(value=value).text
    except:
        return ""


@register.filter(name='get_party')
def get_party(value):
    try:
        return "党派:%s" % MnTParty.objects.get(value=value).text
    except:
        return ""


@register.filter(name='zcellphone')
def zcellphone(value):
    if value:
        return format_html('''<i class="fa fa-mobile-phone"></i> %s''' % value)
    else:
        return ""


@register.filter(name='zworkphone')
def zworkphone(value):
    if value:
        return format_html('''<i class="fa fa-phone"></i> %s''' % value)
    else:
        return ""


@register.filter(name='get_wytype')
def get_wytype(value):
    if value == 1:
        return "政协委员"
    else:
        return "管理员"


@register.filter(name='zjieduan')
def zjieduan(value):
    if len(value) > 15:
        return "%s..." % value[:14]
    else:
        return value


@register.filter(name='getname')
def getname(value):
    return GetAllName(value)



@register.filter(name='sq_banlijieguo')
def sq_banlijieguo(value):
    bljg = ''

    try:
        bljg = MnTBljg_sqmy.objects.get(value=value)
    except:
        pass

    if bljg:
        return format_html('''<span class="label label-primary">%s</span>''' % bljg)
    else:
        return ''
@register.filter(name='mind_stat')
def mind_stat(value):
    if value:
        return format_html('''<span class="label label-primary">未读</span>''')
    else:
        return format_html('''<span class="label label-default">已读</span>''')

@register.filter(name='ta_banlijieguo')
def ta_banlijieguo(value):
    bljg = ''

    try:
        bljg = MnTBljg_tian.objects.get(value=value)
    except:
        pass

    if bljg:
        return format_html('''<span class="label label-primary">%s</span>''' % bljg)
    else:
        return ''
@register.filter(name='zlen')
def zlen(value):
    count = 0
    for x in value:
        if x.unread:
            count += 1
    return count


@register.filter(name='enablen')
def enablen(value):
    count = 0
    for x in value:
        if x.enable:
            count += 1
    return count


@register.filter(name='getsqwriter')
def getsqwriter(value):
    value = (MnTTa)(value)
    if value.class_field == "社情民意" and value.grper == "组织":
        contact = "联系方式:" + value.sqmy_contact
        zbname = value.sqmy_zbname
        zbwork = "工作单位和职务:" + value.sqmy_zbwork
        return format_html('''<span class="label label-info" title="%s\n%s">%s</span>''' % (contact, zbwork, zbname))
    else:
        return format_html('''<span class="label label-info">%s</span>''' % (GetAllName(value.writer)))


def GetAllName(name):
    names = []
    if ' ' in name:
        for x in name.split():
            names.append(GetRealName(x))
        names = " ".join(names)
    else:
        names = name
    return GetRealName(names)


def GetRealName(no_or_name):
    if ('-' in no_or_name) or ('0' in no_or_name):
        name = "找不到"
        try:
            name = MnTWy.objects.get(wyno=no_or_name).name
        except:
            pass
    else:
        name = no_or_name
    return name
@register.filter(name='Get_bldw')
def Get_bldw(zis):
    try:
        banlidanwei = format_html( "%s %s %s" %("<code>主办:%s</code>" % ",".join(map(lambda x: x.text, zis.zhuban.all())) if zis.zhuban.count() > 0 else "" ,"<code>会办:%s</code>" % ",".join(map(lambda x: x.text, zis.huiban.all())) if zis.huiban.count() > 0 else "","<code>合办:%s</code>" % ",".join(map(lambda x: x.text, zis.heban.all())) if zis.heban.count() > 0 else ""))
    except:
        banlidanwei = "出错"
    return banlidanwei


@register.filter(name='htmlset')
def htmlset(value):
    if "\n" in value:
        html = "%s" % value.replace("\n", "</p><p>")
    else:
        html = value
    return format_html(html)



