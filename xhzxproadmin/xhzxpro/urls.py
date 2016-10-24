# coding:utf-8
import django_url_framework
import xadmin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from xhzx import views

# from django.contrib.auth.views import login, logout
django_url_framework.site.autodiscover(settings.INSTALLED_APPS)
# urlpatterns = patterns('',
#                        url(r'^forgot-password/$',
#                            auth_views.forgot_password, name="forgot-password"),
#                        url(r'^password/change/$',
#                            auth_views.password_change,
#                            name='password_change'),
#                        url(r'^password/change/done/$',
#                            auth_views.password_change_done,
#                            name='password_change_done'),
#                        url(r'^resetpassword/$',
#                            auth_views.password_reset,
#                            name='password_reset'),
#                        url(r'^resetpassword/passwordsent/$',
#                            auth_views.password_reset_done,
#                            name='password_reset_done'),
#                        url(r'^reset/done/$',
#                            auth_views.password_reset_complete,
#                            name='password_reset_complete'),
#                        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
#                            auth_views.password_reset_confirm,
#                            name='password_reset_confirm'),
#                        )
# urlpatterns = patterns('',
#                        (r'^', include(django_url_framework.site.urls) ),
# )


urlpatterns = patterns('',
                       # Examples:
                        # url(r'^$', 'eyepro.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),

                       url(r'^zadmin/', include(xadmin.site.urls)),
                       url(r'^$', views.index),

                       url(r'^my_ta/$', views.myta, {"tos": "提案", "submit": False}),
                       url(r'^mysubmit_ta/$', views.myta, {"tos": "提案","submit": True}),
                       url(r'^my_sq/$', views.myta, {"tos": "社情民意", "submit": False}),
                       url(r'^mysubmit_sq/$', views.myta, {"tos": "社情民意", "submit": True}),

                       url(r'^sbm_ta/$', views.SubmitTa, {"tos": '提案'}),
                       url(r'^sbm_sq/$', views.SubmitTa, {"tos": '社情民意'}),

                       url(r'^sbmc_ta/$', views.SubmitTa_change, {"tos": '提案'}),
                       url(r'^sbmc_sq/$', views.SubmitTa_change, {"tos": '社情民意'}),

                       url(r'^tian_change/(?P<iid>\w+)/$', views.issue_change, {"tos": '提案'}),
                       url(r'^sqmy_change/(?P<iid>\w+)/$', views.issue_change, {"tos": '社情民意'}),
                       url(r'^sbm_ta/omore/88/$', views.redict,
                           {"tos": '提案', "mypath": "/my_ta/", "thispath": "/sbm_ta/", "ismine": True}),
                       url(r'^sbm_ta/omore/77/$', views.redict,
                           {"tos": '提案', "mypath": "/my_ta/", "thispath": "/sbm_ta/", "ismine": False}),
                       url(r'^sbm_sq/omore/88/$', views.redict,
                           {"tos": '社情民意', "mypath": "/my_sq/", "thispath": "/sbm_sq/", "ismine": True}),
                       url(r'^sbm_sq/omore/77/$', views.redict,
                           {"tos": '社情民意', "mypath": "/my_sq/", "thispath": "/sbm_sq/", "ismine": False}),

                       url(r'^mind/read/(?P<iid>\w+)/$', views.read, {"tos": '提醒', "dlt": False}),
                       url(r'^mind/del/(?P<iid>\w+)/$', views.read, {"tos": '提醒', "dlt": True}),
                       url(r'^mind/readall/$', views.readall, {"tos": '提醒', "rod": "已读"}),
                       url(r'^mind/deleteall/$', views.readall, {"tos": '提醒', "rod": "删除"}),

                       url(r'^my_nt/$', views.mynt, {"tos": '提醒'}),
                       url(r'^my_ad/$', views.myad, {"tos": '公告'}),
                       url(r'^my_tl/$', views.timeline, {"tos": '公告'}),

                       url(r'^wy/$', views.wy),

                       # url(r'^issue/tian/content/(?P<iid>\w+)/$', views.makedoc, {"tos": "提案"}),
                       url(r'^issue/sqmy/content/(?P<iid>\w+)/$', views.makedoc, {"tos": "社情民意"}),
                       url(r'^ad/detail/(?P<iid>\w+)/$', views.addetail),

                       url(r'^issue/tian/search/$', views.issue, {"tos": '提案'}),
                       url(r'^issue/sqmy/search/$', views.issue, {"tos": '社情民意'}),

                       url(r'^issue/tian/del/(?P<iid>\w+)/$', views.issuedel, {"tos": '提案'}),
                       url(r'^issue/sqmy/del/(?P<iid>\w+)/$', views.issuedel, {"tos": '社情民意'}),

                       url(r'^issue/tian/detail/(?P<iid>\w+)/$', views.issuedetail, {"tos": '提案'}),
                       url(r'^issue/sqmy/detail/(?P<iid>\w+)/$', views.issuedetail, {"tos": '社情民意'}),
                       url(r'^issue/tian/fengmian/(?P<iid>\w+)/$', views.fengmian),

                       url(r'^issue/tian/all/$', views.tianall, {"tos": '提案'}),
                       url(r'^issue/sqmy/all/$', views.tianall, {"tos": '社情民意'}),

                       url(r'^system/setpassword/$', views.system_setpassword),
                       url(r'^system/get/$', views.system_get),

                       url(r'^service/getadn/$', views.service_getadn),
                       url(r'^service/getsqtacount/$', views.service_getsqtacount),


                       url(r'^service/updatewy/$', views.service_updatewy),
                       url(r'^service/addwy/$', views.service_addwy),
                       url(r'^service/delwy/$', views.service_delwy),

                       url(r'^service/address/sqmy/$', views.adr_sqmy),
                       url(r'^service/address/tian/$', views.adr_tian),
                       url(r'^service/address/ads/$', views.adr_ads),
                       url(r'^service/setnames/$', views.setnames),



                       url(r'^helper/excle/$', views.helper_excle),



                       url(r'^login/$', views.login),
                       url(r'^logout/$', views.logout),
                       url(r'^createcsv/grta/$', views.createcsv, {"tos": "个人提案"}),
                       url(r'^createcsv/jtta/$', views.createcsv, {"tos": "集体提案"}),
                       url(r'^createcsv/sqmy/$', views.createcsv, {"tos": "社情民意"}),

                       url(r'^get/tazip/$', views.gettazip, {"tos": "个人提案"}),
                       url(r'^get/tian/$', views.getcsv, {"tos": "提案"}),
                       url(r'^get/sqmy/$', views.getcsv, {"tos": "社情民意"}),
                       ##########################

                       url(r'^taisok/$', views.taisok, {"tos": "个人提案"}),

                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
