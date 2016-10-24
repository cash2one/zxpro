# -*-coding:utf-8 -*-
import hashlib
import json
import os

from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import format_html
from .models import MnTWy, MnTSq, MnTTa, MnTBljg_sqmy, MnTBljg_tian, MnTAnswer, MnTAd, MnTNotice, MnTTHyjc, MnTGlobal, \
    MnTTips, MnTGroup, Jiafenchi, AutoSubmit, MnTZwh, MnTParty, MnTJiebie

from django.http import HttpResponseRedirect
def custom_proc(request):
    wyno = request.REQUEST.get("wyno", "")
    wy = None
    if wyno:
        try:
            wy = MnTWy.objects.get(wy_id=wyno)
        except Exception as e:
            pass
    else:
        wy = request.session.get('wy', default=None)
        if wy:
            wy = MnTWy.objects.get(pk=wy)
    if wy:

        query = """select name from mn_t_wy WHERE IsWy = 1 AND DATEDIFF( CAST(CONCAT('2015',DATE_FORMAT(birth,'-%m-%d'))  AS DATETIME),CAST(CURRENT_DATE()  AS DATETIME )) = 0 ;"""
        query7 = """select name from mn_t_wy WHERE IsWy = 1 AND DATEDIFF( CAST(CONCAT('2015',DATE_FORMAT(birth,'-%m-%d'))  AS DATETIME),CAST(CURRENT_DATE()  AS DATETIME )) BETWEEN 1 AND 7 ORDER BY CAST(CONCAT('2015',DATE_FORMAT(birth,'-%m-%d'))  AS DATETIME)"""
        from django.db import connection
        cursor = connection.cursor()  # 获得一个游标(cursor)对象
        cursor.execute(query)
        tobirth = cursor.fetchall()  # 返回结果行 或使用 #raw = cursor.fetchall()

        botn = []
        for x in tobirth:
            botn.append(x[0])

        cursor = connection.cursor()
        cursor.execute(query7)
        camebirth = cursor.fetchall()  # 返回结果行 或使用 #raw = cursor.fetchall()
        camen = []
        for x in camebirth:
            camen.append(x[0])

        return {
            'wy': wy,
            'ads': GetAds(),
            "minds": GetMinds(wy.wyno),
            "tobirth": botn,
            "camebirth": camen

        }


def GetAds():
    return MnTAd.objects.filter(enable=True).order_by("-submit_time")


def GetMinds(wy):
    return MnTNotice.objects.filter(wyno=wy).order_by("-time")


def index(request):

    wy = request.session.get('wy', default=None)

    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            mtitle = '个人中心'
            stitle = '首页'

            return render_to_response('index.html',
                                      {'mtitle': mtitle, "zhuye": True,
                                       'stitle': stitle,},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def myta(request, tos, submit):
    wy = request.session.get('wy', default=None)

    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            mtitle = '个人中心'

            if tos == "提案":
                status = MnTBljg_tian
                someone = MnTTa
                rstr = "tian"
                istian = True

            else:
                status = MnTBljg_sqmy
                someone = MnTSq
                rstr = "sqmy"
                istian = False
            stitle = tos
            status = status.objects.all().order_by('sort')
            othertitle = ""
            try:
                if not submit:
                    stitle = "本人" + tos
                    iss = someone.objects.filter(
                        Q(writer__contains=wy.name) | Q(writer__contains=wy.wyno) | Q(mname__contains=wy.name) | Q(
                            mno__contains=wy.wyno)).order_by('-submit_time')
                else:
                    stitle = "提交的%s" % tos
                    othertitle = "提交的%s【使用该注册账号提交的%s，包含为他人或者组织成员提交】" % (tos, tos)
                    iss = someone.objects.filter(submit_wyno=wy.wyno).order_by('-submit_time')
            except Exception as e:
                iss = []
                print e
            hyjcs = MnTTHyjc.objects.all()[::-1]

            return render_to_response('me/mytian.html',
                                      {'status': status,
                                       'iss': iss,
                                       "rstr": rstr,
                                       "istian":istian,
                                       'hyjcs': hyjcs,
                                       'mtitle': mtitle,
                                       'stitle': stitle,
                                       "tos": tos,
                                       'cpath': rstr,
                                       'othertitle': othertitle
                                       }, context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def mynt(request, tos):
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            mtitle = '个人中心'
            stitle = '我的提醒'
            return render_to_response('ad/search_nt.html',
                                      {'mtitle': mtitle, 'stitle': stitle},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def timeline(request, tos):
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            mtitle = '个人中心'
            stitle = '我的记录'
            return render_to_response('me/timeline.html',
                                      {'mtitle': mtitle, 'stitle': stitle},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def myad(request, tos):
    wyno = request.REQUEST.get("wyno", "")

    if wyno:
        try:
            wy = MnTWy.objects.get(wy_id=wyno)
            request.session['wy'] = wy.id
        except Exception as e:
            print e
            wy = None
    else:
        wy = request.session.get('wy', default=None)
        if wy:
            wy = MnTWy.objects.get(pk=wy)

    if wy:
        if wy.enable:
            mtitle = '个人中心'
            stitle = '公告'

            return render_to_response('ad/search_ad.html',
                                      {'mtitle': mtitle, 'stitle': stitle},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def SubmitTa_change(request, tos):
    "修改提交"
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            if request.method == 'POST':
                biaoti = request.POST['biaoti']
                qkfy = request.POST['qkfy']
                yjhjy = request.POST['yjhjy']
                iid = request.POST['iid']

                if tos == "提案":
                    Something = MnTTa
                    path = 'tian'
                else:
                    path = 'sqmy'
                    Something = MnTSq

                gI = Something.objects.get(pk=iid)

                if gI.biaoti != biaoti:
                    gI.biaoti = biaoti

                if gI.qkfy != qkfy:
                    gI.qkfy = qkfy

                if gI.yjhjy != yjhjy:
                    gI.yjhjy = yjhjy
                gI.save()
                AddMind(wy.wyno, "您修改了%s:《%s》" % (tos, biaoti), "/issue/%s/detail/%s/" % (path, gI.pk))
                return HttpResponseRedirect("/issue/%s/detail/%s/" % (path, gI.pk))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")

def issue_change(request, tos, iid):
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            mtitle = '提案|社情民意 中心'
            stitle = tos + '修改'
            if tos == "提案":
                Something = MnTTa
                istian = True
            else:
                Something = MnTSq
                istian = False
            try:
                iss = Something.objects.get(pk=iid)
            except Exception as e:
                print e
                return render_to_response('error.html', {'error': "没找到该%s!" % tos})
            changeable = True
            if tos == "提案":
                if iss.admin_status:
                    changeable = False
            else:
                if len(iss.admin_status.all()) > 0:
                    changeable = False

            if not changeable:
                return render_to_response('error.html', {'error': "您来晚了,%s已经发布了!" % tos})
            if iss:
                biaoti = iss.biaoti
                yjhjy = iss.yjhjy
                qkfy = iss.qkfy

                if tos == "提案":
                    thispath = "/sbmc_ta/"
                else:
                    thispath = "/sbmc_sq/"

                return render_to_response('issue/submit_ta_change.html',
                                          {'iss': iss,
                                           'mtitle': mtitle, 'stitle': stitle, 'mypath': "", "thispath": thispath, "tos": tos,
                                           "istian": istian, "biaoti": biaoti, "yjhjy": yjhjy, "qkfy": qkfy,
                                           },
                                          context_instance=RequestContext(request, processors=[custom_proc]))

            else:
                return render_to_response('error.html', {'error': "没找到"})
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')

    else:
        return HttpResponseRedirect("/login/")


def SubmitTa(request, tos):
    "提案提交"
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            mtitle = '提案|社情民意 中心'
            stitle = tos + '提交'

            if tos == "提案":
                thispath = "/sbm_ta/"
                mypath = "/my_ta/"
                istian = True
            else:
                thispath = "/sbm_sq/"
                mypath = "/my_sq/"
                istian = False


            om = False
            if request.method == 'POST':
                biaoti = request.POST['biaoti']
                goj = request.POST['goj']
                qkfy = request.POST['qkfy']
                yjhjy = request.POST['yjhjy']
                jf_name = request.POST['jf_name']
                jf_wyno = request.POST['jf_wyno']

                if tos == "提案":
                    if goj == u'geren':
                        goj = '个人'
                        mname = jf_name
                        mno = jf_wyno
                    else:
                        goj = '集体'
                        mname = jf_name
                        mno = ''
                    jianyi = request.POST['jianyi']
                    # qkfy = qkfy.strip().replace("。", ".",).replace("，",",").replace( "；", ";").replace( "：", ":").replace("？", "?").replace( "！",  "!").replace("……","…").replace( "—","-").replace( "～", "~").replace("〔", "(").replace("〕",")").replace("《","<").replace( "》",">").replace("‘","'").replace("’","'").replace("“",'"').replace("”",'"').replace("%",'')
                    nI = MnTTa.objects.create(biaoti=biaoti, qkfy=qkfy.strip(), chengbandanwei=jianyi, yjhjy=yjhjy.strip(),
                                              writer=mname.replace(',', ' '),
                                              finish=1, filetogovs=0,
                                              state=0, submit_wyno=wy.wyno, submit_name=wy.name, grper=goj, mno=mno,
                                              mname=mname,
                                              docx=0, hyjc=MnTGlobal.objects.get(pk=1).dqhyjc)

                    mnostr = nI.mno
                    mnamestr = nI.mname
                    if "," in nI.mno:
                        if len(nI.mno.split(',')) > 3:
                            mnostr = ",".join((nI.mno.split(','))[:3])
                            mnamestr = ",".join((nI.mname.split(','))[:3])

                    Jiafenchi.objects.create(djf_issueno=nI.issueno,
                                             djf_tos=nI.class_field,
                                             djf_issueid=nI.pk,
                                             djf_issuebt=nI.biaoti,
                                             djf_wyno=mnostr,
                                             djf_wyname=mnamestr,
                                             djf_state=1,
                                             djf_type=2 if (nI.mno and ',' in nI.mno) else 1,
                                             djf_time=nI.submit_time)

                    AddMind(wy.wyno, "您添加了%s:《%s》" % (tos, biaoti), "/issue/tian/detail/%s/" % nI.pk)
                    return HttpResponseRedirect("/issue/tian/detail/%s/" % (nI.pk))
                else:
                    sqmy_contact = request.POST['contact']
                    sqmy_zbname = request.POST['zbname']
                    sqmy_zbwork = request.POST['zbwork']
                    if goj == u'geren':
                        goj = '个人'
                        mname = jf_name
                        mno = jf_wyno
                    else:
                        goj = '组织'
                        mname = jf_name
                        mno = ""
                    hyjc = MnTGlobal.objects.get(pk=1).dqhyjc
                    for s in MnTSq.objects.exclude(issueno="").filter(hyjc=hyjc):

                        tmp1 = 0
                        newi = int((s.issueno.split("-"))[1])
                        if tmp1 < newi:
                            tmp1 = newi
                    try:
                        if tmp1:

                            pass
                        else:
                            tmp1 = 2000
                    except Exception as e:
                        print e
                        tmp1 = 2000
                    ngz = MnTGlobal.objects.get(pk=1)
                    issueno = "%s%s" % (ngz.year, tmp1 + 1)

                    nI = MnTSq.objects.create(issueno=issueno, biaoti=biaoti, qkfy=qkfy.strip(), yjhjy=yjhjy.strip(),
                                              writer=mname,
                                              finish=1, filetogovs=0,
                                              submit_wyno=wy.wyno, submit_name=wy.name, grper=goj,
                                              state=0, sqmy_contact=sqmy_contact, sqmy_zbname=sqmy_zbname,
                                              sqmy_zbwork=sqmy_zbwork, mname=mname,
                                              mno=mno.replace(';', '_').replace(',', '_').replace(' ', '_').replace('.',
                                                                                                                    '_'),
                                              docx=0, hyjc=hyjc)

                    AddMind(wy.wyno, "您添加了%s:《%s》" % (tos, biaoti), "/issue/sqmy/detail/%s/" % nI.pk)
                    return HttpResponseRedirect("/issue/sqmy/detail/%s/" % (nI.pk))


            else:

                # users = MnTWy.objects.all()
                users = MnTWy.objects.exclude(Q(wy_id__isnull=True)|Q(wy_id=''))

                if tos == "提案":

                    julist = MnTGroup.objects.filter(ta=True).order_by('ta_sort')
                else:
                    julist = MnTGroup.objects.filter(sqmy=True).order_by('sqmy_sort')

                return render_to_response('issue/submit_ta.html',
                                          {'iss': '',
                                           'mtitle': mtitle, 'stitle': stitle,
                                           'users': users,
                                           'jitis': julist, 'mypath': mypath, "thispath": thispath, "tos": tos,
                                           "istian": istian,
                                           'om': om},
                                          context_instance=RequestContext(request, processors=[custom_proc]))

        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def AddMind(wy, text, detail):
    MnTNotice.objects.create(text=text, type=0, wyno=str(wy), detail=detail)


def read(request, iid, tos, dlt):
    feedback = {"success": False}
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            try:
                if tos == "提醒":
                    getit = MnTNotice.objects.get(pk=iid, wyno=MnTWy.objects.get(pk=wy).wyno)
                    if dlt:
                        getit.enable = False
                    else:
                        getit.unread = False
                    getit.save()
                    feedback['success'] = True
                else:

                    thistip = MnTTips.objects.get(wyno=MnTWy.objects.get(pk=wy).wyno)
                    adlist = []
                    for x in thistip.adur_list.split(','):

                        xx = x.split(':')
                        if xx[0] == iid:
                            xx[1] = "0"
                        adlist.append("%s:%s", xx[0], xx[1])

                    thistip.adur_list = ",".join(adlist)
                    thistip.save()
                    feedback['success'] = True

            except Exception as e:
                print e

    return HttpResponse(json.dumps(feedback), content_type="application/json")


def readall(request, tos, rod):
    feedback = {"success": False}
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            try:
                if rod == "已读":
                    for n in MnTNotice.objects.all():
                        n.unread = False
                        n.save()
                else:
                    for n in MnTNotice.objects.all():
                        n.enable = False
                        n.unread = False
                        n.save()

                feedback['success'] = True
            except Exception as e:
                print e

    return HttpResponse(json.dumps(feedback), content_type="application/json")


def redict(request, tos, thispath, mypath, ismine):
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            if ismine:
                msg = format_html("<a class='btn btn-link' href='%s'>点击查看刚刚提交的%s</a>" % (mypath, tos))
            else:
                msg = format_html(
                    "<p>您所提交的%s,作者不是您本人</p><p>登录作者<strong>本人</strong>帐号,才能够查看</p>" % (
                        tos))

            return render_to_response('redirect.html',
                                      {
                                          "thispath": thispath, "tos": tos,
                                          "msg": msg},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def GetjitiName(id):
    try:
        return MnTGroup.objects.get(value=id).text
    except Exception as e:
        print e
        return "找不到"


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def logout(request):
    try:
        del request.session['wy']
    except Exception as e:
        print e
    return HttpResponseRedirect("/login/")


def wy(request):
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if wy.enable:
            wys = MnTWy.objects.filter(iswy=1)
            mtitle = '委员'
            stitle = '所有委员'

            return render_to_response('wy/index.html',
                                      {'wys': wys,
                                       'mtitle': mtitle, 'stitle': stitle},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def issue(request, tos):
    """提交社情民意"""
    """如果有委员登录信息"""

    wyno = request.REQUEST.get("wyno", "")

    if wyno:
        try:
            wy = MnTWy.objects.get(wy_id=wyno)
            request.session['wy'] = wy.id
        except Exception as e:
            print e
            wy = None
    else:
        try:
            wy = request.session.get('wy', default=None)

            if wy:
                wy = MnTWy.objects.get(pk=wy)
        except Exception as e:
            print e
    if wy:
        if type(wy) == type(int):
            wy = MnTWy.objects.get(pk=wy)
        if True:
            if tos == "提案" and not wy.enable:
                return HttpResponseRedirect('/issue/sqmy/search/')

            if tos == '提案':
                mtitle = '提案中心'
                detailstr = '/issue/tian/detail/'
                iscount = MnTTa.objects.count()
                istian = True
                status = MnTBljg_tian.objects.all().order_by('sort')
                requeststr = "/issue/tian/all/"
            else:
                mtitle = '社情民意中心'
                istian = False
                detailstr = '/issue/sqmy/detail/'
                iscount = MnTSq.objects.count()
                status = MnTBljg_sqmy.objects.all().order_by('sort')
                requeststr = "/issue/sqmy/all/"

            hyjcs = MnTTHyjc.objects.all()

            return render_to_response('issue/search_ta.html',
                                      {'hyjcs': hyjcs,
                                       'iss': iscount,
                                       'istian':istian,
                                       "tos": tos,
                                       'mtitle': mtitle,
                                       'stitle': "%s%s %s" % (tos, '查询', iscount),
                                       'status': status, "requeststr": requeststr, 'detailstr': detailstr},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:

        return HttpResponseRedirect("/login/")


def addetail(request, iid):
    "某条公告的详细信息"
    wyno = request.REQUEST.get("wyno", "")

    if wyno:
        try:
            wy = MnTWy.objects.get(wy_id=wyno)
            request.session['wy'] = wy.id
        except Exception as e:
            print e
            wy = None
    else:
        wy = request.session.get('wy', default=None)
        if wy:
            wy = MnTWy.objects.get(pk=wy)
    if wy:
        if wy.enable:
            mtitle = '<a class="btn btn-link" href="/my_ad/"><i class="fa fa-newspaper-o"></i>所有公告</a>'
            stitle = '公告查看'
            try:
                mis = MnTAd.objects.get(id=int(iid))
                pl = MnTAnswer.objects.filter(articleid=iid)
            except Exception as e:
                print e
                return render_to_response('error.html', {'error': "没找到"})

            return render_to_response('ad/index.html',
                                      {'mis': mis,
                                       'mtitle': mtitle, 'stitle': stitle, 'wy': wy},
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


def issuedetail(request, iid, tos):
    wy = request.session.get('wy', default=None)
    if wy:
        wy = MnTWy.objects.get(pk=wy)
        if True:


            stitle = '%s查看' % tos
            msg = ''
            new = False
            try:
                if tos == "提案" and not wy.enable:
                    return HttpResponseRedirect('/issue/sqmy/search/')
                if tos == "提案":
                    someone = MnTTa
                    mtitle = '<a class="btn btn-link" href="/issue/tian/search/"><i class="fa fa-newspaper-o"></i>%s中心</a>' % tos
                    thispath = '/sbm_ta/'
                    cpath = 'tian'
                else:
                    someone = MnTSq
                    mtitle = '<a class="btn btn-link" href="/issue/sqmy/search/"><i class="fa fa-newspaper-o"></i>%s中心</a>' % tos
                    thispath = '/sbm_sq/'
                    cpath = 'sqmy'
                mis = someone.objects.get(id=int(iid))

                pl = MnTAnswer.objects.filter(articleid=iid)

                liulanplus(mis)
                if tos == "提案":
                    if not mis.admin_status:
                        if (mis.mno and (wy.wyno in mis.mno)) or (wy.wyno == mis.submit_wyno):
                            new = True
                        else:
                            return render_to_response('error.html',
                                                      {'error': tos + "还没有发布", 'mtitle': mtitle, 'stitle': stitle,})
                else:
                    if len(mis.admin_status.all()) == 0:
                        if (mis.mno and (wy.wyno in mis.mno)) or (wy.wyno == mis.submit_wyno):
                            new = True
                        else:
                            return render_to_response('error.html',
                                                      {'error': tos + "还没有发布", 'mtitle': mtitle, 'stitle': stitle,})

                if new:
                    msg = format_html(
                        "<ul class='list-group'><li  class='list-group-item list-group-item-success'>您的%s在被管理员<strong>发布或者立案</strong>之前</li><li  class='list-group-item list-group-item-success'>只有<strong>作者</strong>和<strong>提交者</strong>能看到该%s</li></ul><ul class='list-group'><li class='list-group-item list-group-item-success'>如果需要删除或者修改%s</li><li class='list-group-item list-group-item-success'>您可以在当前页面中操作</li><li class='list-group-item list-group-item-success'>也可以在 <i class='fa fa-user'></i>个人中心 > <a href='%s'>%s</a> 中操作</li></ul>" % (
                            tos, tos, tos, "/my_ta/" if (tos == "提案") else "/my_sq/", tos))

            except Exception as e:
                print e
                return render_to_response('error.html', {'error': "没找到这个" + tos, 'mtitle': mtitle, 'stitle': stitle,})
            return render_to_response('issue/index.html',
                                      {'mis': mis,
                                       'mtitle': mtitle,
                                       'stitle': stitle,
                                       'wy': wy,
                                       'pl': pl,
                                       'thispath': thispath,
                                       'writers': GetGAllName(mis),
                                       'new': new,
                                       'tos': tos,
                                       'msg': msg,
                                       'cpath': cpath
                                       },
                                      context_instance=RequestContext(request, processors=[custom_proc]))
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    else:
        return HttpResponseRedirect("/login/")


from datetime import *


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def system_setpassword(request):
    from django.contrib.auth.models import User
    if True:
        flag = True
        try:
            for w in MnTWy.objects.all():
                try:
                    if w.birth:
                        if "19" in str(w.birth):
                            passwd = (str(w.birth))[2:].replace("-", "")
                            user = User.objects.create_user(username=w.name, email=w.mailadd, password=passwd)
                            user.save()
                            print passwd
                        else:
                            print w.pk, w.name, w.wyno, w.birth
                    else:
                        print w.pk, w.name, w.wyno
                except Exception as e:
                    pass
        except Exception as e:
            print e
            flag = False
        return HttpResponse(flag)
    else:
        return HttpResponse(False)


# def system_setpassword(request):
#     if False:  # True
#         flag = True
#         try:
#             for w in MnTWy.objects.all():
#                 try:
#                     w.passwd = w.passwd.replace('-', '').lower()
#                     w.save()
#                 except Exception as e:
#                     pass
#         except Exception as e:
#             print e
#             flag = False
#         return HttpResponse(flag)
#     else:
#         return HttpResponse(False)


def adr_sqmy(request):
    "社情民意查询和提交的连接"
    fb = {"data": "0"}
    wyno = request.REQUEST.get("wyno", "")
    if wyno:
        fb["data"] = "http://211.144.101.198/issue/sqmy/search/?wyno=%s" % (wyno)
    return HttpResponse(json.dumps(fb), content_type="application/json")


def adr_ads(request):
    "公告列表的链接地址"
    fb = {"data": "0"}
    wyno = request.REQUEST.get("wyno", "")
    if wyno:
        fb["data"] = "http://211.144.101.198/my_ad/?wyno=%s" % (wyno)
    return HttpResponse(json.dumps(fb), content_type="application/json")


def adr_tian(request):
    "提案查询和提交按钮的连接"
    fb = {"data": "0"}
    wyno = request.REQUEST.get("wyno", "")
    if wyno:
        fb["data"] = "http://211.144.101.198/issue/tian/search/?wyno=%s" % (wyno)
    return HttpResponse(json.dumps(fb), content_type="application/json")


def createcsv(request, tos):
    fb = {'data': False}
    if tos == "个人提案":
        file_name = "grta.csv"
        try:
            if os.path.exist(file_name):
                os.remove(file_name)
        except Exception as e:
            print e
        import csv
        with open(file_name, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            spamwriter.writerow(["编  号", "提案人", "案  由", "类别", "主  办", "会  办", "办理情况"])
            for ta in MnTTa.objects.exclude(issueno="").filter(hyjc="十三届四次", grper="个人"):
                spamwriter.writerow([ta.issueno, GetAllName(ta.writer), ta.biaoti, "", "", "", ""])

        fb['data'] = True
    if tos == "集体提案":
        file_name = "jtta.csv"
        try:
            if os.path.exist(file_name):
                os.remove(file_name)
        except Exception as e:
            print e
            pass
        import csv
        with open(file_name, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            spamwriter.writerow(["编  号", "提案人", "案  由", "类别", "主  办", "会  办", "办理情况"])
            for ta in MnTTa.objects.exclude(issueno="").filter(hyjc="十三届四次", grper="集体"):
                spamwriter.writerow([ta.issueno, GetAllName(ta.writer), ta.biaoti, "", "", "", ""])

        fb['data'] = True

    if tos == "社情民意":
        file_name = "sqmy.csv"
        try:
            if os.path.exist(file_name):
                os.remove(file_name)
        except Exception as e:
            pass
        import csv
        with open(file_name, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            spamwriter.writerow(["编号", "报送单位", "报送人", "案由", "办理情况", "报送日期"])
            for ta in MnTSq.objects.exclude(issueno="").filter(hyjc="十三届四次"):
                spamwriter.writerow([ta.issueno, ta.grper, GetAllName(ta.writer), ta.biaoti, "", ""])

        fb['data'] = True
    return HttpResponse(json.dumps(fb), content_type="application/json")


def taisok(request, tos):
    fb = {'data': True, 'msg': ""}

    iid = request.REQUEST.get("id", "")
    ta = None
    if iid:
        try:
            ta = MnTTa.objects.get(pk=iid)
        except Exception as e:
            print e
            pass

    test = AutoSubmit.objects.filter(pro_tano=ta.issueno)
    if test.count() > 0:
        return HttpResponse(json.dumps({'data': False, 'msg': "%s已经提交过了!" % (ta.issueno)}),
                            content_type="application/json")
    if ta:
        if not ta.issueno:
            fb['msg'] = "提案未编号 "
            fb['data'] = False
        if not ta.biaoti:
            fb['msg'] = "提案未填写标题 "
            fb['data'] = False

        if (not ta.yjhjy) and (not ta.qkfy):
            fb['msg'] = "情况反映 或 意见和建议 未填写 "
            fb['data'] = False

        if not ta.reconfirmnames:
            fb['msg'] = "分类未选择 "
            fb['data'] = False

        if ta.zhuban.all().count() and not ta.heban.all().count():
            pass
        elif ta.heban.all().count() and not ta.zhuban.all().count():
            pass
        else:
            fb['msg'] += "主办或合办必须并且只能填写其中一个 "
            fb['data'] = False

        if fb['data']:
            try:
                if " " in ta.writer:
                    writer = (ta.writer.split())[0]
                else:
                    writer = ta.writer

                if "-" in writer:
                    writerwy = (MnTWy.objects.filter(wyno=writer))[0]
                else:
                    writerwy = (MnTWy.objects.filter(name=writer))[0]

                # fb['idata'] = {
                #     "pro": {
                #         "tano": ta.issueno,
                #         "title": ta.biaoti,
                #         "qkfy": ta.qkfy,
                #         "yjhjy": ta.yjhjy,
                #         "cbdw": ",".join(map(lambda x: x.text, ta.zhuban.all())),
                #         "type": "个人联名" if ta.grper == "个人" else "党派团体",
                #         "acceptdate": str(datetime.strftime(ta.submit_time, "%Y-%m-%d")),
                #         "hebandw": ",".join(map(lambda x: x.text, ta.heban.all())),
                #         "huibandw": ",".join(map(lambda x: x.text, ta.huiban.all())),
                #         "leader": ta.fenguan if ta.fenguan else "",
                #         "bo_type": ta.reconfirmnames,
                #         "partyindex": "区政协%s会议" % ta.hyjc
                #     },
                #     "zz": {
                #         "name": GetAllName(ta.writer),
                #         "tell1": ("021-%s" % writerwy.workphone) if writerwy.workphone else "",
                #         "tell2": writerwy.cellphone,
                #         "gzdw": writerwy.workpos,
                #         "zwh": writerwy.zwh.text if writerwy.zwh else "",
                #         "jb": writerwy.jiebie.text if  writerwy.jiebie else "",
                #         "dp": writerwy.party.text if writerwy.party else""
                #     }
                # }

                fl = ta.reconfirmnames
                if fl == "A":
                    leixing = "财政经济类"
                elif fl == "B":
                    leixing = "城市建设和管理类"
                elif fl == "C":
                    leixing = "教科文卫体类"
                elif fl == "D":
                    leixing = "综合类"
                else:
                    leixing = ta.reconfirmnames
                try:
                    wyzwh = writerwy.zwh.text
                except Exception as e:
                    wyzwh = ""

                try:
                    wyjiebie = writerwy.jiebie.text
                except Exception as e:
                    wyjiebie = ""
                try:
                    wyparty = writerwy.party.text
                except Exception as e:
                    wyparty = ""

                a = AutoSubmit.objects.create(
                    pro_tano=ta.issueno,
                    pro_title=ta.biaoti,
                    pro_qkfy=ta.qkfy,
                    pro_yjhjy=ta.yjhjy,
                    pro_cbdw=",".join(map(lambda x: x.text, ta.zhuban.all())),
                    pro_type="个人联名" if ta.grper == "个人" else "党派团体",
                    pro_acceptdate=str(datetime.strftime(ta.submit_time, "%Y-%m-%d")),
                    pro_hebandw=",".join(map(lambda x: x.text, ta.heban.all())),
                    pro_huibandw=",".join(map(lambda x: x.text, ta.huiban.all())),
                    pro_leader=ta.fenguan if ta.fenguan else "",
                    pro_bo_type=leixing,
                    pro_partyindex="区政协%s会议" % ta.hyjc,
                    zz_name=GetAllName(ta.writer),
                    zz_tell1=("%s" % writerwy.workphone) if writerwy.workphone else "",
                    zz_tell2=writerwy.cellphone,
                    zz_gzdw=writerwy.workpos,
                    zz_zwh=wyzwh,
                    zz_jb=wyjiebie,
                    zz_dp=wyparty
                )
                if a:
                    fb['data'] = True
                    fb['msg'] = '添加成功'
                else:
                    fb['data'] = False
                    fb['msg'] = '添加失败'
            except Exception as e:
                fb['data'] = False
                fb['msg'] = '添加失败:%s' % str(e)
                # gb = MnTGlobal.objects.get(pk=1)
                # if gb.panfu == "C":
                #
                #     posturl = "http://sysducha.xh.sh.cn/xhrddbjlpt/OA/XHRDJLPT/UI/Sugproc/AddSugproc.ashx?random=%s" % random.random()
                #     data = fb['idata']
                #     try:
                #         feedback = get(posturl, data)
                #         feedback = eval(feedback)
                #         if feedback['errcode'] != 0:
                #             fb['data'] = False
                #             fb['msg'] = "区: %s" % feedback['errmsg']
                #         else:
                #             fb['msg'] = "提交成功!"
                #     except Exception as e:
                #         fb['msg'] = "未知错误"
                # else:
                #     fb['data'] = False
                #     fb['msg'] = "地址还没有开通"
    return HttpResponse(json.dumps(fb), content_type="application/json")


import urllib
import urllib2


def get(url, content):
    content = json.dumps(content)
    content = content.encode('utf-8')
    content = urllib2.quote(content)
    return urllib2.urlopen('%s&data=%s' % (url, content)).read()


def post(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    # enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()


def getcsv(request, tos):
    try:
        if tos == "提案":
            file_name = "tian.csv"

        if tos == "社情民意":
            file_name = "sqmy.csv"

        with open(file_name) as f:
            c = f.read()
        from django.http import StreamingHttpResponse
        response = StreamingHttpResponse(c)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
    except Exception as e:
        print e
        response = ''
    if response:
        return response
    else:
        return HttpResponse('')


def gettazip(request, tos):
    return HttpResponseRedirect("/static/tar.zip")


def service_updatewy(request):
    "委员更新信息,姓名手机号密码等"
    fb = {"data": 0, "msg": ""}
    if request.method == 'GET':
        try:
            wyno = request.REQUEST.get('wyno', '')
            if wyno:
                try:
                    wy = MnTWy.objects.get(wy_id=wyno)
                except Exception as e:
                    print e
                    wy = None
                if wy:
                    localvar = locals()
                    zwh = request.REQUEST.get('zwh', 'novalue')
                    party = request.REQUEST.get('party', 'novalue')
                    jiebie = request.REQUEST.get('jiebie', 'novalue')
                    varslist = ['wynob', 'oldpd', 'newpd', 'cellphone', 'name', 'birth',
                                'gender', 'nation', 'workpos', 'workadr', 'workzip', 'workphone', 'homeadr',
                                'homephone',
                                'homezip', 'isexewy', 'issmallwy', 'email', 'xueli', 'xuewei', 'zhichen', 'jiguan']

                    for varname in varslist:
                        localvar[varname] = request.REQUEST.get(varname, '')
                    if localvar['cellphone'] or localvar['name'] or (localvar['newpd'] and localvar['oldpd']):
                        if localvar['cellphone']:
                            wy.cellphone = localvar['cellphone']

                        if localvar['name']:
                            wy.name = localvar['name']
                        if localvar['newpd'] and localvar['oldpd']:
                            m1 = hashlib.md5()
                            m1.update(localvar['oldpw'])

                            oldpwd = m1.hexdigest()

                            if oldpwd == wy.passwd:
                                m2 = hashlib.md5()
                                m2.update(localvar['newpd'])
                                newpwd = m2.hexdigest()
                                wy.passwd = newpwd
                    if zwh != 'novalue':
                        try:
                            wy.zwh = MnTZwh.objects.get(text=zwh).value
                        except Exception as e:
                            pass
                    if party != 'novalue':
                        try:
                            wy.party = MnTParty.objects.get(text=party).value
                        except Exception as e:
                            pass
                    if jiebie != 'novalue':
                        try:
                            wy.jiebie = MnTJiebie.objects.get(text=jiebie).value
                        except Exception as e:
                            pass
                    for varname in varslist:
                        try:
                            if localvar[varname] != 'novalue':
                                wy.varname = localvar[varname]
                            else:
                                wy.varname = None
                        except Exception as e:
                            print str(e)
                    wy.lastedittime = datetime.now()
                    wy.save()
                    fb['data'] = 1
        except Exception as e:
            fb['msg'] = str(e)
    return HttpResponse(json.dumps(fb), content_type="application/json")


def service_addwy(request):
    "新增委员,必填项 有委员固定编号，委员编号，密码，手机号码 ,委员姓名;委员固定编号有重复时或者手机号码有冲突时不能成功添加委员。"
    fb = {"data": 0, "msg": ""}
    if request.method == 'GET':
        wyno = request.REQUEST.get('wyno', '')
        if wyno:
            cellphone = request.REQUEST.get('cellphone', 'novalue')
            name = request.REQUEST.get('name', 'novalue')
            newpasswd = request.REQUEST.get('password', 'novalue')
            wynob = request.REQUEST.get('wynob', 'novalue')
            zwh = request.REQUEST.get('zwh', 'novalue')
            party = request.REQUEST.get('party', 'novalue')
            jiebie = request.REQUEST.get('jiebie', 'novalue')
            localvar = locals()
            varslist = ['birth',
                        'gender', 'nation', 'workpos', 'workadr', 'workzip', 'workphone', 'homeadr', 'homephone',
                        'homezip', 'isexewy', 'issmallwy', 'email', 'xueli', 'xuewei', 'zhichen', 'jiguan']

            for varname in varslist:
                localvar[varname] = request.REQUEST.get(varname, 'novalue')
            if wyno != 'novalue' and MnTWy.objects.filter(wy_id=wyno).count() == 0:
                if cellphone != 'novalue' and MnTWy.objects.filter(cellphone=cellphone).count() == 0:

                    if name != 'novalue' and newpasswd:
                        m1 = hashlib.md5()
                        m1.update(newpasswd)
                        newpw = m1.hexdigest()

                        try:
                            MnTWy.objects.create(wy_id=wyno, name=name, cellphone=cellphone, passwd=newpw,wyno=wynob)
                            fb['data'] = 1
                        except Exception as e:
                            fb['msg'] = str(e)
                        try:
                            newwy = MnTWy.objects.get(wy_id=wyno)
                            if zwh != 'novalue':
                                try:
                                    newwy.zwh = MnTZwh.objects.get(text=zwh).value
                                except Exception as e:
                                    pass
                            if party != 'novalue':
                                try:
                                    newwy.party = MnTParty.objects.get(text=party).value
                                except Exception as e:
                                    pass
                            if jiebie != 'novalue':
                                try:
                                    newwy.jiebie = MnTJiebie.objects.get(text=jiebie).value
                                except Exception as e:
                                    pass
                            for varname in varslist:
                                try:
                                    if localvar[varname] != 'novalue':
                                        newpw.varname = localvar[varname]
                                except Exception as e:
                                    print str(e)
                            newwy.save()

                        except Exception as e:
                            print str(e)
                else:
                    fb['msg'] = "The cellphone%s is already occupied." % ((":" + cellphone) if cellphone else "")
            else:
                fb['msg'] = "The wyno%s is already occupied." % ((":" + wyno) if wyno else "")
    return HttpResponse(json.dumps(fb), content_type="application/json")


def service_delwy(request):
    "删除委员"
    fb = {"data": 0, "msg": ""}
    if request.method == 'GET':
        wyno = request.REQUEST.get('wyno', '')
        if wyno:
            try:
                delwys = []
                if '_' in wyno:
                    for w in wyno.split('_'):
                        delwys.append(w)
                else:
                    delwys.append(wyno)

                for w in delwys:
                    wy = MnTWy.objects.get(wy_id=w)
                    wy.enable = False
                    wy.save()
                    fb['data'] = 1
            except Exception as e:
                fb['msg'] = str(e)
    return HttpResponse(json.dumps(fb), content_type="application/json")


def system_get(request):
    if False:
        wyno = request.REQUEST.get("wyno", "")
        shuxing = request.REQUEST.get("shuxing", "")

        if wyno and shuxing:
            wy = MnTWy.objects.get(wyno=wyno)
            x = getattr(wy, shuxing)

        return HttpResponse(x)
    else:
        return HttpResponse(False)


def service_getsqtacount(request):
    "获取当前用户提交的提案数和提交的社情民意数"
    data = {
        "tianshu": "0",
        "sheqingminyishu": "0"
    }
    wyno = request.REQUEST.get("wyno", "")
    try:
        wy = MnTWy.objects.get(wy_id=wyno)
        data["tianshu"] = MnTTa.objects.filter(Q(writer__contains=wy.name) | Q(writer__contains=wy.wyno)).count()
        data["sheqingminyishu"] = MnTSq.objects.filter(Q(writer__contains=wy.name) | Q(writer__contains=wy.wyno)).count()
    except Exception as e:
        pass


    return HttpResponse(json.dumps(data), content_type="application/json")


def service_getadn(request):
    "获取当前用户有权限查看的最新N条公告列表"
    list = []

    try:
        ads = MnTAd.objects.all().order_by("-submit_time")[0:int(request.REQUEST.get("count", "1"))]
        for ad in ads:
            list.append({
                "id": ad.pk,
                "biaoti": ad.name,
                "fabushijian": ad.submit_time,
                "faburen": "管理员",
                "chakanlianjie": "http://%s/ad/detail/%s/" % ("", ad.pk),
            })

    except Exception as e:
        pass

    return HttpResponse(json.dumps(list, cls=CJsonEncoder), content_type="application/json")


def mns(x):
    return x.text


def tianall(request, tos):
    wy = request.session.get('wy', default=None)
    if wy:
        try:
            if tos == "提案":
                Someone = MnTTa
            else:
                Someone = MnTSq
            id = request.REQUEST.get("id", "")
            if id:

                hyjc = MnTTHyjc.objects.get(value=id).text
            else:
                gb = MnTGlobal.objects.get(pk=1)
                hyjc = gb.dqhyjc
            page = request.REQUEST.get("page", "")
            if page:
                try:
                    page = int(page)
                except Exception as e:
                    page = 0
            else:
                page = 0
            iss = None
            try:
                cpp = 50

                filterstr = request.REQUEST.get("filter", "")
                bljg = request.REQUEST.get("bljg", "")
                from django.db.models import Q
                if filterstr and bljg:

                    count = Someone.objects.exclude(issueno="").exclude(issueno="").filter(
                        Q(biaoti__contains=filterstr.strip()) | Q(mname__contains=filterstr.strip()) | Q(
                            qkfy__icontains=filterstr.strip()) | Q(
                            yjhjy__icontains=filterstr.strip()) | Q(writer__icontains=filterstr.strip()), hyjc=hyjc,
                        admin_status=bljg).order_by('-submit_time').count()

                    iss = Someone.objects.exclude(issueno="").exclude(issueno="").filter(
                        Q(biaoti__contains=filterstr.strip()) | Q(mname__contains=filterstr.strip()) | Q(
                            qkfy__icontains=filterstr.strip()) | Q(
                            yjhjy__icontains=filterstr.strip()) | Q(writer__icontains=filterstr.strip()), hyjc=hyjc,
                        admin_status=bljg).order_by('-submit_time')[page * cpp:(page + 1) * cpp]


                elif filterstr and not bljg:
                    count = Someone.objects.exclude(issueno="").filter(
                        (Q(biaoti__icontains=filterstr.strip()) | Q(mname__icontains=filterstr.strip()) | Q(
                            qkfy__icontains=filterstr.strip()) | Q(
                            yjhjy__icontains=filterstr.strip()) | Q(writer__icontains=filterstr.strip())),
                        hyjc=hyjc).order_by('-submit_time').count()

                    iss = Someone.objects.exclude(issueno="").filter(
                        (Q(biaoti__icontains=filterstr.strip()) | Q(mname__icontains=filterstr.strip()) | Q(
                            qkfy__icontains=filterstr.strip()) | Q(
                            yjhjy__icontains=filterstr.strip()) | Q(writer__icontains=filterstr.strip())),
                        hyjc=hyjc).order_by('-submit_time')[page * cpp:(page + 1) * cpp]


                elif bljg and not filterstr:
                    count = Someone.objects.exclude(issueno="").filter(hyjc=hyjc, admin_status=bljg).order_by(
                        '-submit_time').count()
                    iss = Someone.objects.exclude(issueno="").filter(hyjc=hyjc, admin_status=bljg).order_by(
                        '-submit_time')[page * cpp:(page + 1) * cpp]

                else:
                    count = Someone.objects.exclude(issueno="").filter(hyjc=hyjc).order_by('-submit_time').count()
                    iss = Someone.objects.exclude(issueno="").filter(hyjc=hyjc).order_by('-submit_time')[
                          page * cpp:(page + 1) * cpp]

                if count % cpp == 0:

                    pages = count / cpp
                else:
                    pages = count / cpp + 1
                    # print iss.count()
                    # print iss.query
            except Exception as e:
                print e
            # iss = Someone.objects.all()
            isss = []
            if tos == "提案":
                for zis in iss:
                    sbiaoti = "%s..." % zis.biaoti[:14] if len(zis.biaoti) > 15 else zis.biaoti
                    bbiaoti = zis.biaoti
                    writer = GetAllName(zis.writer)
                    admin_status = zis.admin_status.text if zis.admin_status else ""
                    submit_time = zis.submit_time
                    hyjc = zis.hyjc
                    view_counts = zis.view_counts
                    agosubmit_time = zis.submit_time
                    submit_name = zis.submit_name
                    banlidanwei = "%s %s %s" % ("<code>主办:%s</code>" % ",".join(
                        map(lambda x: x.text, zis.zhuban.all())) if zis.zhuban.count() > 0 else "",
                                                "<code>会办:%s</code>" % ",".join(map(lambda x: x.text,
                                                                                    zis.huiban.all())) if zis.huiban.count() > 0 else "",
                                                "<code>合办:%s</code>" % ",".join(map(lambda x: x.text,
                                                                                    zis.heban.all())) if zis.heban.count() > 0 else "")

                    isss.append({
                        "id": zis.pk,
                        "issueno": zis.issueno,
                        "dafu": "有" if zis.yidafu else "无",
                        "sbiaoti": sbiaoti,
                        "bbiaoti": bbiaoti,
                        "writer": writer,
                        "hyjc": hyjc,
                        "submit_time": submit_time,
                        "admin_status": admin_status,
                        "admin_statusm": admin_status,
                        "admin_statusc": "",
                        "labelstyle": 'primary',
                        "view_counts": view_counts,
                        "agosubmit_time": agosubmit_time,
                        "submit_name": submit_name,
                        'banlidanwei': banlidanwei,
                    })
            else:
                for zis in iss:
                    sbiaoti = "%s..." % zis.biaoti[:14] if len(zis.biaoti) > 15 else zis.biaoti
                    bbiaoti = zis.biaoti
                    writer = GetAllName(zis.writer)
                    submit_time = zis.submit_time
                    hyjc = zis.hyjc
                    view_counts = zis.view_counts
                    agosubmit_time = zis.submit_time
                    submit_name = zis.submit_name
                    ass = zis.admin_status.all()
                    asss = map(mns, ass)

                    isss.append({
                        "id": zis.pk,
                        "issueno": zis.issueno,
                        "dafu": "有" if zis.yidafu else "无",
                        "sbiaoti": sbiaoti,
                        "bbiaoti": bbiaoti,
                        "writer": writer,
                        "hyjc": hyjc,
                        "submit_time": submit_time,
                        "admin_status": ("%s等" % asss[0]) if len(asss) > 1 else asss,
                        "admin_statusm": " ".join(asss) if asss else "",
                        "admin_statusc": ("%s个状态" % len(asss)) if len(asss) > 0 else "",
                        "labelstyle": 'warning' if len(asss) > 1 else "primary",
                        "view_counts": view_counts,
                        "agosubmit_time": agosubmit_time,
                        "submit_name": submit_name,
                    })
            feedback = {"data": isss, "count": count, "pages": pages}


        except Exception as e:
            print e
            feedback = {"result": False}
    else:
        feedback = {"result": False, "info": "no login"}
    return HttpResponse(json.dumps(feedback, cls=CJsonEncoder), content_type="application/json")


def issuedel(request, iid, tos):
    wy = request.session.get('wy', default=None)
    wy = MnTWy.objects.get(pk=wy)
    feedback = {"result": False}

    if wy:
        if wy.enable:
            if tos == "提案":
                someone = MnTTa
                try:
                    tis = someone.objects.get(pk=iid)
                    if tis and not tis.admin_status:
                        AddMind(wy.wyno, "您删除了%s:《%s》" % (tos, tis.biaoti), "/my_tl/")
                        tis.delete()
                        feedback['result'] = True
                except Exception as e:
                    # tis.delete()
                    feedback['result'] = True
                    print e

            else:
                someone = MnTSq
                try:
                    tis = someone.objects.get(pk=iid)
                    if tis and len(tis.admin_status.all()) == 0:
                        AddMind(wy.wyno, "您删除了%s:《%s》" % (tos, tis.biaoti), "/my_tl/")
                        tis.delete()
                        feedback['result'] = True
                except Exception as e:
                    pass
        else:
            return HttpResponseRedirect('/issue/sqmy/search/')
    return HttpResponse(json.dumps(feedback), content_type="application/json")


def liulanplus(i):
    i.view_counts += 1
    i.save()


def login(request):
    if request.session.get('wy', default=None):
        return HttpResponseRedirect("/")
    else:
        if request.method == 'POST':
            name = request.POST['name']
            password = request.POST['password']
            if name and password:
                wys = MnTWy.objects.all()
                flag = False
                try:
                    for wy in wys:
                        if "@" in name:
                            if name == wy.mailadd:
                                flag = True
                        elif len(name) == 11:
                            if name == wy.cellphone:
                                flag = True
                        else:
                            if name == wy.name:
                                flag = True
                        if flag:
                            m2 = hashlib.md5()
                            m2.update(password)
                            np = m2.hexdigest()
                            if np == wy.passwd:
                                request.session['wy'] = wy.id
                                wy.lastlogin = wy.logintime
                                wy.logintime = datetime.now()
                                if wy.netup:
                                    wy.netup += 1
                                else:
                                    wy.netup = 1
                                wy.save()
                                return HttpResponseRedirect("/")
                            break
                except Exception as e:
                    pass

            return render_to_response('login.html', {'alerterror': True},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', context_instance=RequestContext(request))


def GetGAllName(mis):
    names = []
    if mis.mno:
        if mis.grper == "个人":
            for x in mis.mno.split(','):
                names.append({"wyno": "非政协委员" if (not "-" in x) else x, "name": GetRealName(x)})
        else:
            for x in mis.mno.split(','):
                names.append({"wyno": "", "name": GetRealName(x)})

    else:

        for x in mis.writer.split():
            names.append({"wyno": "" if ("00000" in x) else x, "name": GetRealName(x)})

    return names


def GetAllName(name):
    names = []
    if ' ' in name:
        for x in name.split():
            names.append(GetRealName(x))
        names = " ".join(names)
    else:
        names = name
    return GetRealName(names)


def GetRealName(rname):
    if ('-' in rname) or ('00000' in rname):
        if '(' in rname:
            try:
                tmp = rname.split('(')
                rname = "%s(%s" % (MnTWy.objects.get(wyno=tmp[0]).name, tmp[1])
            except Exception as e:
                pass
        else:
            try:
                rname = MnTWy.objects.get(wyno=rname).name
            except Exception as e:
                pass

    return rname


def my_view(request):
    context = {'some_key': 'some_value'}

    static_html = 'static.html'
    import os
    if not os.path.exists(static_html):
        content = render_to_string('template.html', context)
        with open(static_html, 'w') as static_file:
            static_file.write(content)

    return render(request, static_html)


def makedoc(request, iid, tos):
    wy = request.session.get('wy', default=None)
    if wy:
        if tos == "提案":
            someone = MnTTa
        else:
            someone = MnTSq
        iss = someone.objects.get(pk=iid)
        if tos == "提案":
            if " " in iss.writer:
                writers = iss.writer.split(" ")[0]

            else:
                writers = iss.writer

            if '-' in writers:
                wr = MnTWy.objects.get(wyno=writers)
                name = wr.name
                cellphone = wr.cellphone
                zbwork = "%s %s" % (wr.workplace, wr.workpos)

            else:
                try:
                    wr = MnTWy.objects.get(name=iss.writer)
                    name = wr.name
                    cellphone = wr.cellphone
                    zbwork = "%s %s" % (wr.workplace, wr.workpos)

                except Exception as e:
                    name = iss.writer
                    cellphone = ""
                    zbwork = ""
        else:

            if iss.sqmy_zbname:
                name = iss.writer
                cellphone = iss.sqmy_contact
                zbwork = iss.sqmy_zbwork
            else:

                if '-' in iss.writer:
                    wr = MnTWy.objects.get(wyno=iss.writer)
                    name = wr.name
                    cellphone = wr.cellphone
                    zbwork = "%s %s" % (wr.workplace, wr.workpos)

                else:
                    try:
                        wr = MnTWy.objects.get(name=iss.writer)
                        name = wr.name
                        cellphone = wr.cellphone
                        zbwork = "%s %s" % (wr.workplace, wr.workpos)

                    except Exception as e:
                        name = iss.writer
                        cellphone = ""
                        zbwork = ""

        # static_html = 'xhzx/static/%s.html' % iss.pk
        # context = {"iss": iss, 'name': name, "cellphone": cellphone, "zbwork": zbwork}

        # import os
        # if not os.path.exists(static_html):
        #     content = render_to_string('issue/doc.html', context)
        #     with open(static_html, 'w') as static_file:
        #         static_file.write(content)
        return render_to_response('issue/doc.html',
                                  {"iss": iss, 'name': name, "cellphone": cellphone, "zbwork": zbwork})

    else:
        return HttpResponseRedirect("/login/")


def page_not_found(request):
    return render_to_response('Error/404.html')


def page_error(request):
    return render_to_response('Error/500.html')


def fengmian(request, iid):
    try:
        Issue = MnTTa.objects.get(pk=iid)
        if Issue:
            writers = Issue.mno.split(',')
            # writernames = ''
            # for writer in writers:
            # writernames += MnTWy.objects.get(pk=writer)
            try:
                workpos1 = ''
                workpos2 = ''
                writer1 = MnTWy.objects.get(wyno=writers[0])

                if len(writer1.workpos) > 30:
                    workpos1 = writer1.workpos[:30]
                    workpos2 = writer1.workpos[31:]
                else:
                    workpos1 = writer1.workpos

            except Exception as e:
                writer1 = {}
                writer1['name'] = writers[0]
            writer2 = ''
            writer3 = ''
            writerother = ''
            if len(writers) > 1:
                try:
                    writer2 = MnTWy.objects.get(wyno=writers[1])
                except Exception as e:
                    writer2 = {}
                    writer2['name'] = writers[1]
                if len(writers) >= 3:
                    try:
                        writer3 = MnTWy.objects.get(wyno=writers[2])
                    except Exception as e:
                        writer3 = {}
                        writer3['name'] = writers[2]
                if len(writers) > 3:

                    for x in writers[3:]:
                        try:

                            writerother = writerother + " " + ((MnTWy.objects.get(wyno=x))).name
                        except Exception as e:

                            writerother = writerother + " " + x

            return render_to_response('issue/detail.html',
                                      {'Issue': Issue, 'writer1': writer1, 'writer2': writer2, 'writer3': writer3,
                                       'workpos1': workpos1, 'workpos2': workpos2, 'writerothers': writerother})
    except Exception as e:
        return render_to_response('issue/detail.html', {'pname': '没有这个提案或社情民意'})


def GetName(mis):
    names = []
    for x in mis.writer.split():
        names.append(GetRealName(x))
    return names


def setnames(request):
    debug = False

    trs = "<tr><td>标题</td><td>作者</td><td>mno</td><td>mname</td></tr>"
    OBJ = MnTSq
    if debug:
        for x in OBJ.objects.all():
            if not x.mno:
                x.mname = (",".join(GetName(x))).replace("（", "(").replace("）", ")").replace("/", "")
                x.mno = x.writer.replace(" ", ",")
                x.save()
                trs += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (x.biaoti, x.writer, x.mno, x.mname)
    return HttpResponse('<table>%s</table>' % trs)


def getwynofromwynob(wynob):
    wyno = ''
    try:
        w = MnTWy.objects.get(wyno=wynob)
        wyno = w.wy_id
    except Exception as e:
        print e
    return wyno


def wynob2wyno(wynob, name):
    shuzu = wynob.split(',')
    names = name.split(',')
    newwyno = []
    newwynob = []
    newnames = []
    if len(shuzu) > 1:
        for x in range(len(shuzu)):
            wyno = getwynofromwynob(shuzu[x])
            if wyno:
                newwyno.append(wyno)
                newwynob.append(shuzu[x])
                newnames.append(names[x])
    else:
        newwyno.append(getwynofromwynob(shuzu[0]))
        newwynob.append(shuzu[0])
        newnames.append(names[0])
    data = {}
    data['wyno'] = ','.join(newwyno)
    data['wynob'] = ','.join(newwynob)
    data['names'] = ','.join(newnames)
    return data


def setwynobfortasq(request):
    if request.user.is_authenticated() and request.user.username in ['zhulielie', 'zll']:
        bootcss = '''<!DOCTYPE html>
    <html lang="zh-CN">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
        <title>Bootstrap 101 Template</title>

        <!-- Bootstrap -->
        <link href="http://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="//cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="//cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>
      <body>
        %s

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="http://cdn.bootcss.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
      </body>
    </html>'''
        debug = True

        trs = "<tr><td>序号</td><td>标题</td><td>时间</td><td>委员固定编号</td><td>委员姓名</td><td>委员编号</td><td>得分</td></tr>"
        OBJ = MnTTa
        if debug:
            import datetime
            cc = 0
            start_date = datetime.date(2016, 1, 1)
            clear = request.REQUEST.get('clear', '')

            if clear:
                Jiafenchi.objects.all().delete()

            ta = request.REQUEST.get('ta', '')
            tas = request.REQUEST.get('tas', '')
            sqs = request.REQUEST.get('sqs', '')
            tac = request.REQUEST.get('tac', '')
            sqtt = request.REQUEST.get('sqtt', '')
            sqc = request.REQUEST.get('sqc', '')
            if ta:
                tacount = 0
                for x in OBJ.objects.filter(submit_time__lte=start_date,issueno__contains='16-'):
                    tacount += 1
                    if x.mno:
                        x.mnob = x.mno
                        data = wynob2wyno(x.mno, x.mname)
                        if tas:
                            x.save()
                        if data['wyno'] and ',' not in data['wyno']:
                            trs += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td> - </td></tr>" % (tacount,
                                x.biaoti, x.submit_time, data['wyno'], data['names'], data['wynob'])
                            cc += 1
                            if tac:
                                try:
                                    Jiafenchi.objects.create(djf_issueno=x.issueno,
                                                             djf_tos=x.class_field,
                                                             djf_issueid=x.pk,
                                                             djf_issuebt=x.biaoti,
                                                             djf_wyno=data['wyno'],
                                                             djf_wynob=data['wynob'],
                                                             djf_wyname=data['names'],
                                                             djf_state=1,
                                                             djf_type=2 if (x.mno and ',' in x.mno) else 1,
                                                             djf_time=x.submit_time)
                                except Exception as e:
                                    print e
                                try:
                                    if x.admin_status.score != 0 :

                                        Jiafenchi.objects.create(djf_issueno=x.issueno,
                                                                 djf_tos=x.class_field,
                                                                 djf_issueid=x.pk,
                                                                 djf_issuebt=x.biaoti,
                                                                 djf_wyno=data['wyno'],
                                                                 djf_wynob=data['wynob'],
                                                                 djf_wyname=data['names'],
                                                                 djf_state=2,
                                                                 djf_type=2 if (x.mno and ',' in x.mno) else 1,
                                                                 djf_time=x.submit_time)
                                except Exception as e:
                                    pass
                trs += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td></td></tr>" % (cc,cc, cc, cc, cc, cc)
            sq = request.REQUEST.get('sq', '')
            if sq:
                sqcount = 0
                for x in MnTSq.objects.filter(submit_time__gte=start_date):
                    # if x.mno :
                    if True:
                        x.mnob = x.mno
                        data = wynob2wyno(x.mno, x.mname)
                        if sqs:
                            x.save()
                        ts = 0
                        for aaa in x.admin_status.all():
                            ts += aaa.score

                        if data['wyno']:
                            pass
                        else:
                            if sqtt:
                                data = {}
                                data['wyno'] = x.mno
                                data['names'] = x.mname
                                data['wynob'] = x.mnob

                        if data and  data['wyno']:
                            sqcount += 1
                            trs += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (sqcount,
                                x.biaoti, x.submit_time, data['wyno'], data['names'], data['wynob'], ts)
                            newstat = " ".join(map(lambda x: x.text, x.admin_status.all()))
                            scores = 0
                            for asa in x.admin_status.all():
                                scores += asa.score
                                if sqc:
                                    try:
                                        Jiafenchi.objects.create(djf_wyno=data['wyno'],
                                                                 djf_wynob=data['wynob'],
                                                                 djf_wyname=data['names'],
                                                                 djf_year='2016',
                                                                 djf_issuebt=x.biaoti,
                                                                 djf_issueno=x.issueno,
                                                                 djf_issueid=x.pk,
                                                                 djf_tos="社情民意",
                                                                 djf_date=x.submit_time,
                                                                 djf_detail="社情民意《%s》%s 状态由[] -> [%s]" % (
                                                                     x.biaoti, x.issueno,
                                                                     newstat),
                                                                 fenshu=scores
                                                                 )

                                    except Exception as e:
                                        print e

        tablehtml = '<table class="table table-striped"> %s</table>' % trs
        return HttpResponse(bootcss % tablehtml)
    else:
        return HttpResponseRedirect('/')

def helper_excle(request):
    if request.user.is_authenticated() and request.user.username in ['zhulielie', 'zll']:
        debug = True
        import xlrd
        data = xlrd.open_workbook('new.xls')
        table = data.sheets()[0]
        nrows = table.nrows

        trs = "<tr><th>序号</th><th>姓名</th><th>wyno</th><th>wynob</th><th>存在与否</th><th>excle委员性质</th><th>数据库委员性质</th><th>委员id</th></tr>"

        if debug:
            num = -1
            for i in range(nrows):
                num += 1
                if num == 0:
                    continue

                wyno = table.row(i)[0].value
                wynob = table.row(i)[2].value
                if str(wyno) != str(wynob):
                    wyno = str(wyno)[:-2]
                ex_xingzhi = table.row(i)[1].value
                wyname = table.row(i)[3].value
                try:
                    wyexisg = MnTWy.objects.get(wyno=wynob)
                    # wyexisg.wy_id = wyno
                    # wyexisg.save()
                except Exception as e:
                    print "%s:%s" % (wyno, str(e))
                    wyexisg = None
                    wyno = wynob
                    wy_id = wyno
                    name = wyname
                    race = table.row(i)[2].value
                    sex = 0 if str(table.row(i)[8].value) == "男" else 1
                    birth = table.row(i)[10].value
                    MnTWy.objects.create(wyno=wyno, wy_id=wy_id, name=name, race=race, sex=sex, birth=birth)

                trs += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                num, wyname, wyno, wynob, "存在" if wyexisg else "不存在", ex_xingzhi, "", wyexisg.wy_id if wyexisg else "")
        html = '<table class="table table-striped">%s</table>' % trs

        ds = MnTWy.objects.filter(wy_id__isnull=True)
        for s in ds:
            s.enable = False
            s.save()
        return render_to_response('helper.html', {'html': html})
    else:
        return HttpResponseRedirect('/')
