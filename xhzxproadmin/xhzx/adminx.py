# -*-coding:utf-8 -*-
import xadmin
from django.utils.html import format_html
from xadmin import views
from xhzx.models import *


# from models import IDC, Host, MaintainLog, HostGroup, AccessRecord

class BaseSetting(object):
    enable_themes = False
    use_bootswatch = False


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    global_search_models = [MnTWy]
    # global_models_icon = {
    # Host: 'fa fa-laptop', IDC: 'fa fa-cloud'
    # }
    # menu_style = 'accordion'  # 'accordion'
    hidden_menu = True
    site_title = u'徐汇政协后台管理'
    site_footer = u'徐汇政协后台管理'
    # apps_icons ={ 'fa fa-laptop'}

    # def get_site_menu(self):
    # return (
    # {'title': '资料录入', 'icon': 'fa fa-table', 'perm': self.get_model_perm(Patient, 'change'), 'menus': (
    # {'title': Patient._meta.verbose_name, 'icon': 'fa fa-table',
    # 'url': self.get_model_url(Patient, 'changelist'),
    # 'perm': self.get_model_perm(Patient, 'change')},
    # {'title': Surgery._meta.verbose_name, 'icon': 'fa fa-table',
    # 'url': self.get_model_url(Surgery, 'changelist'),
    # 'perm': self.get_model_perm(Surgery, 'change')},
    # {'title': Mazui._meta.verbose_name, 'icon': 'fa fa-table',
    # 'url': self.get_model_url(Mazui, 'changelist'),
    # 'perm': self.get_model_perm(Mazui, 'change')},
    # {'title': Style._meta.verbose_name, 'icon': 'fa fa-table',
    # 'url': self.get_model_url(Style, 'changelist'),
    # 'perm': self.get_model_perm(Style, 'change')},
    # {'title': Mid._meta.verbose_name, 'icon': 'fa fa-table',
    # 'url': self.get_model_url(Mid, 'changelist'),
    # 'perm': self.get_model_perm(Mid, 'change')},
    # {'title': OldOperation._meta.verbose_name, 'icon': 'fa fa-table',
    #              'url': self.get_model_url(OldOperation, 'changelist'),
    #              'perm': self.get_model_perm(OldOperation, 'change')},
    #             {'title': Operation._meta.verbose_name, 'icon': 'fa fa-table',
    #              'url': self.get_model_url(Operation, 'changelist'),
    #              'perm': self.get_model_perm(Operation, 'change')},
    #             {'title': Clinexam._meta.verbose_name, 'icon': 'fa fa-table',
    #              'url': self.get_model_url(Clinexam, 'changelist'),
    #              'perm': self.get_model_perm(Clinexam, 'change')},
    #         )},
    #     )


xadmin.site.register(views.CommAdminView, GlobalSetting)


class ObjectInline(object):
    extra = 1
    style = 'tab'


# class MaintainInline(ObjectInline):
# model = PatientPics
# form_layout = (
# HTML('<button type="button" class="btn btn-primary btnstart" data-toggle="modal">打开扫描仪</button>'),
# HTML("<button type='button' class='btn btn-primary btnset' >选中</button>"), "type",
# HTML("<img src='' class='img-responsive  img'data-toggle='modal' alt='' style='width: 140px; height: 140px;'>"),
# InlineField('pic', readonly=True, css_class="hidden"),
# )

#
# class OpInline(ObjectInline):
# model = Operation

#
# class ClinexamInline(ObjectInline):
# model = Clinexam
# form_layout = (
# Fieldset(
# "检查记录",
# 'jcdate', 'mgd'
# , "shijianweizhi", ),
# Fieldset("",
# Row("qiujing_L_pon", "qiujing_R_pon"),
# Row("zhujing_L_pon", "zhujing_R_pon"),
# Row(PrependedText("zhujing_L", '左眼'), PrependedText("zhujing_R", '右眼')),
#                  Row(PrependedText("jiaozhengshili_L", '左眼'), PrependedText("jiaozhengshili_R", '右眼')),
#                  Row(PrependedText("sanguangdu_L", '左眼'), PrependedText("sanguangdu_R", '右眼')),
#                  Row(PrependedText("yg_L", '左眼'), PrependedText("yg_R", '右眼')),
#                  Row(PrependedText("qiujing_L", '左眼'), PrependedText("qiujing_R", '右眼')),
#                  Row(PrependedText("Jcsl_L", '左眼'), PrependedText("Jcsl_R", '右眼')),
#                  Row(PrependedText("but_L", '左眼'), PrependedText("but_R", '右眼')),
#                  Row(PrependedText("sch_L", '左眼'), PrependedText("sch_R", '右眼')),
#                  Row(PrependedText("yany_L", '左眼'), PrependedText("yany_R", '右眼')),
#                  Row(PrependedText("jmnpjs_L", '左眼'), PrependedText("jmnpjs_R", '右眼')),
#                  Row(PrependedText("ct_L", '左眼'), PrependedText("ct_R", '右眼')),
#                  Row(PrependedText("jmks_L", '左眼'), PrependedText("jmks_R", '右眼')),
#                  Row(PrependedText("jmksds_L", '左眼'), PrependedText("jmksds_R", '右眼')),
#                  Row(PrependedText("jmkf_L", '左眼'), PrependedText("jmkf_R", '右眼')),
#                  Row(PrependedText("jmkfds_L", '左眼'), PrependedText("jmkfds_R", '右眼')),
#                  Row(PrependedText("ubm_L", '左眼'), PrependedText("ubm_R", '右眼')),
#                  Row(PrependedText("jmygs_L", '左眼'), PrependedText("jmygs_R", '右眼')),
#                  Row(PrependedText("fjj_L", '左眼'), PrependedText("fjj_R", '右眼')),
#                  Row("yandi", "beizhu"),
#         ),
#
#     )
#
#
# class ClinexamAdmin(object):
#     form_layout = (
#         Fieldset("检查记录", 'jcdate')
#     )
#
#
# class OldOperationInline(ObjectInline):
#     model = OldOperation
#     # list_filter = ['name', 'sex', 'nianling', 'addr', 'gaoxy', 'Tangnb', 'guanxb', 'leifsgjy', 'hongblc', 'qinggy',
#     # 'putmy', 'yanws', 'shiwmbx', 'huangbbb', 'pzljishu', 'gxyyao', 'jtyao', 'knyao', 'diagnum', 'beizhu',
#     # 'niming', 'nianlingweizhi']
#
#
# class PatientAdmin(object):
#     search_fields = ['name', 'no']
#     list_filter = ['name', 'sex', 'nianling', 'addr', 'gaoxy', 'Tangnb', 'guanxb', 'leifsgjy', 'hongblc', 'qinggy',
#                    'putmy', 'yanws', 'shiwmbx', 'huangbbb', 'pzljishu', 'gxyyao', 'jtyao', 'knyao', 'diagnum', 'beizhu',
#                    'niming', 'nianlingweizhi']
#
#     grid_layouts = ('table', 'thumbnails')
#     list_bookmarks = [{'title': u"本市", 'query': {'islocalcity': True}},
#                       {'title': u"非本市", 'query': {'islocalcity': False}}, {'title': u"男", 'query': {'sex': 1}},
#                       {'title': u"女", 'query': {'sex': 0}}, ]
#
#     list_display = ['nameCac', 'sexCac', 'cellCac', 'birthCac', 'nianlingCac', 'sm']
#     exclude = ['niming', 'nianlingweizhi', 'nianling']
#
#     def sm(self, instance):
#         if instance.patientpics_set.all().count() > 0:
#             return format_html("<a href='/patient/detail/{0}/'>查看扫描件</a>".format(instance.pk))
#         return '无'
#
#     sm.short_description = '扫描件'
#     style_fields = {'sex': "radio-inline"}
#
#     def nianlingCac(self, instance):
#         # Md = globals()[instance.model_name]()
#         if instance.nianling == 0:
#             return "未填写"
#         else:
#             return instance.nianling
#
#     nianlingCac.short_description = '年龄'
#
#     def sexCac(self, instance):
#         # Md = globals()[instance.model_name]()
#         if not instance.sex:
#             return "女"
#         else:
#             return "男"
#
#     sexCac.short_description = '性别'
#
#     def cellCac(self, instance):
#         if not instance.cell:
#             return "未填写"
#         else:
#             return instance.cell
#
#     cellCac.short_description = '联系电话'
#
#     def nameCac(self, instance):
#         # Md = globals()[instance.model_name]()
#         if not instance.name:
#             return "未填写"
#         else:
#             return instance.name
#
#     nameCac.short_description = '姓名'
#
#     def birthCac(self, instance):
#         # Md = globals()[instance.model_name]()
#         if not instance.birth:
#             return "未填写"
#         else:
#             return instance.birth
#
#     birthCac.short_description = '生日'
#     form_layout = (
#
#         Fieldset('基本信息',
#                  Row('no', 'name', ),
#                  Row('sex', 'birth', ),
#                  Row('cell', 'diagnum'),
#                  Row('addr', 'islocalcity'),
#                  'beizhu',
#                  css_class='short_label'
#         ),
#         Inline(PatientPics),
#         Inline(Operation),
#         Inline(Clinexam),
#         Inline(OldOperation),
#
#         Fieldset('眼科病史',
#                  'qinggy',
#                  'putmy',
#                  'yanws',
#                  'shiwmbx',
#                  'huangbbb',
#                  css_class='short_label'
#         ),
#         Fieldset('特殊药物应用',
#                  'pzljishu',
#                  'gxyyao',
#                  'jtyao',
#                  'knyao',
#                  css_class='short_label'
#         ),
#         Fieldset('基础病史',
#                  'gaoxy',
#                  'Tangnb',
#                  'guanxb',
#                  'leifsgjy',
#                  'hongblc',
#                  css_class='accordion short_label '
#         ),
#     )
#     inlines = [MaintainInline, OpInline, ClinexamInline, OldOperationInline]
#
#
# class SurgeryAdmin(object):
#     pass
#
#
# class MazuiAdmin(object):
#     pass
#
#
# class StyleAdmin(object):
#     pass
#
#
# class MidAdmin(object):
#     pass
#
#
# class OldOperationAdmin(object):
#     pass
#
#
# class OperationAdmin(object):
#     pass
#
#
# class PatientPicsAdmin(object):
#     grid_layouts = ('table', 'thumbnails')
#
#
# class OCTTYPEAdmin(object):
#     pass
#
#
# xadmin.site.register(OCTType, OCTTYPEAdmin)
# xadmin.site.register(Patient, PatientAdmin)
# xadmin.site.register(PatientPics, PatientPicsAdmin)
# xadmin.site.register(Surgery, SurgeryAdmin)
# xadmin.site.register(Mazui, MazuiAdmin)
# xadmin.site.register(Style, StyleAdmin)
# xadmin.site.register(Mid, MidAdmin)
# xadmin.site.register(OldOperation, OldOperationAdmin)
# xadmin.site.register(Operation, OperationAdmin)
# xadmin.site.register(Clinexam, ClinexamAdmin)


class MnTWyAdmin(object):
    list_display = ['wyno', 'name', 'race', 'sex', "cellphone", "iswy", "enable",'lastlogin']
    search_fields = ['wyno','name','race','sex']
    list_filter = ['wyno','name','race','sex','enable','iswy']
    list_editable = ['iswy','enable']
    exclude = ['photo','passwd','lastedittime']
    list_bookmarks = [{'title': u"委员", 'query': {'iswy': 1}},
                      {'title': u"工作人员", 'query': {'iswy': 0}},
    ]


class MnTGlobalAdmin(object):
    list_display = ['dqhyjc','jjf_start']


class JiafenchiAdmin(object):
    list_display = ['djf_tos', 'djf_issueid', 'djf_issueno', 'issuebt', 'djf_state', 'djf_wyname', 'djf_type','fenshu'
                    ]

    def issuebt(self, instance):
        return format_html(
            "<a href='#'  data-toggle=\"tooltip\" data-placement=\"top\"  data-original-title=\"{0}\" target='_blank'>{1}</a>".format(
                instance.djf_detail, instance.djf_issuebt))

    issuebt.short_description = "文档标题"

    def block_extrabody(self, context, nodes):
        return """
        <script type="text/javascript">
        $(function(){
            $('[data-toggle="tooltip"]').tooltip()
       })
        </script>
        """
    ordering = ['-id']


class JianfenchiAdmin(object):
    list_display = ['id', 'djf_issueid', 'djf_issueno', 'djf_issuebt', 'djf_wyname', 'djf_type', 'djf_time', 'time']
    list_display_links = []
    ordering = ['-id']

class MnTTZbdwAdmin(object):
    pass


class JjfenjiluAdmin(object):
    list_display = ['time', 'djf_detail']


class MnTAdAdmin(object):
    exclude = ['submit_time', 'docname']
    list_display = ['name', 'content_sm', 'submit_time', "enable"]
    search_list = ['name', 'content']

    def content_sm(self, instance):
        if instance.content:
            return format_html("<a href='/ad/detail/%s/' title='%s'>%s...</a>" % (
                instance.pk, instance.content,
                instance.content[:15] if len(instance.content) > 15 else instance.content))
        else:
            return ""

    content_sm.short_description = "内容"




class MnTTHyjcAdmin(object):
    list_btns = [{'url': '/', 'title': 'asdasdasdas'}]
    pass


class MnTTBljgAdmin(object):
    pass


class MnTPartyAdmin(object):
    pass


from xadmin.plugins.actions import act_fabu, act_ta_download, act_tadoc_download, act_sqdoc_download, \
    act_sqctdoc_download,cleardafu,autosubmit,act_sq_download,act_meeting_download


def replacename(on):
    if (('(' in on) or (')' in on)):
        return on

    else:
        tmp = MnTWy.objects.filter(wyno=on)
        if tmp:
            return tmp[0].name + ' '
        else:
            return on + ' '


from xadmin.layout import Main, Side, Fieldset
class MnTTaAdmin(object):
    exclude = ['hyjc', 'submit_wyno', 'submit_name', 'submit_time', 'class_field', 'grper', 'writer', 'guanjian',
               'filegov', 'fandui_counts', 'zhichi_counts', 'state', 'docx', 'banliriqi', 'banlijieguo',
               'banlidafu', 'yidafu', 'banlichengbandanwei', 'chengbandanwei', 'tashort', 'tafilename', 'confirm_time',
               'confirm', 'finish', 'filetogovs', 'asfinish', 'answer_time', 'asfilename', 'view_counts','heban','filesort','lajiafen']

    list_filter = ['biaoti', 'issueno', 'writer', 'submit_time', 'finish', 'asfinish', 'confirm', 'grper', 'hyjc']
    search_fields = ['id','biaoti', 'issueno', 'writer', 'tashort', 'guanjian']
    list_display = ['issueno', 'biaoti_set', 'admin_status', 'mname',
                    'print_set', 'online_set', "reconfirmnames", "zhuban", "huiban", 'onekey']

    form_layout = (
            Main(
                Fieldset('基本信息',
                         'zhuban',
                         'huiban',
                ),

            ),
            Side(
                Fieldset('编号 ',
                         'reconfirmnames',
                         'fenguan',
                         'admin_status'
                ),
                Fieldset('提案相关',
                         'issueno',
                         'biaoti',
                ),
                Fieldset('作者信息',
                         'mno',
                         'mname',
                ),
            )
        )


    show_all_rel_details = False
    list_editable = ['confirm', 'issueno', 'biaoti', 'admin_status',  "reconfirmnames"]
    list_per_page = 100
    style_fields = {'huiban': 'm2m_transfer','heban': 'm2m_transfer','zhuban': 'm2m_transfer'}
    def confirm_set(self, instance):

        return "是" if instance.confirm else "否"

    confirm_set.short_description = "已发布"


    # def reconfirmnames_(self,instance):
    #     if instance.reconfirmnames == "财政经济类":
    #         flag = 'A'
    #     elif instance.reconfirmnames == "城市建设和管理类":
    #         flag = 'B'
    #     elif instance.reconfirmnames == "教科文卫体类":
    #         flag = 'C'
    #     elif instance.reconfirmnames == "综合类":
    #         flag = 'D'
    #     else:
    #         flag =""
    #     return  flag
    #
    # reconfirmnames_.short_description = "类别"
    def block_extrabody(self, context, nodes):
        return """
        <script type="text/javascript">
        $(function(){

            $(".onekey").on("click",function(){
                iid = $(this).attr('zdata')
                ibt = $(this).attr('zdatabt')
                swal({   title: "警告",
                 text: "确定要提交 《" + ibt +"》 提案吗?",
                 type: "warning",
                 showCancelButton: true,
                 confirmButtonColor: "#DD6B55",
                 confirmButtonText: "确定",
                 cancelButtonText: "取消",
                 closeOnConfirm: false },
                 function(){


                $.get("/taisok/",{id:iid},function(data){
                if(data.data){
                    if(data.msg)
                        sweetAlert("成功", data.msg, "success");
                    }
                else
                {
                    if(data.msg){
                        errtext = data.msg
                    }
                    else
                        errtext = "必须的选项还没有全部选择"
                    sweetAlert("错误", errtext, "error");
                }
                })
                 });
            })
        })
        </script>
        """
    def biaoti_set(self, instance):
        newbiaoti = format_html(
            "<span title='标题:\n\t\t{0}\n关键词:\n\t\t{1}\n简介:\n\t\t{2}\n_________________________________________\n提交人:\t\t{3} {4}\n提交时间:\t{5}\n转换完成:\t{6}\n答复转换完成:\t{7}'>{8}</span> ".format(
                instance.biaoti,
                instance.guanjian if instance.guanjian else "无",
                instance.tashort if instance.tashort else "无",
                instance.submit_wyno,
                instance.submit_name,
                instance.submit_time,
                "是" if instance.finish else "否",
                "是" if instance.asfinish else "否",
                instance.biaoti if len(instance.biaoti) < 10 else (
                    (instance.biaoti)[0:10] + "...")))
        return newbiaoti

    biaoti_set.short_description = "标题"
    list_display_links = ['biaoti_set']
    def guanjian_set(self, instance):
        newguanjian = format_html(
            "<span title='{0}'>{1}</span> ".format(instance.guanjian,
                                                   instance.guanjian if len(instance.guanjian) < 10 else (
                                                       (instance.guanjian)[0:10] + "...")))
        return newguanjian

    guanjian_set.short_description = "关键词"

    def writer_set(self, instance):
        writer = instance.writer
        tmp = ''
        bflag = False
        if ' ' in writer:
            tmp = writer.replace("（", "(").replace("）", ")").split(' ')
        elif '(' in writer:
            tmp = writer.replace("（", "(").replace("）", ")").split('(')
            bflag = True
        else:
            return replacename(writer)

        neww = ''
        if not bflag:
            for ot in tmp:
                neww += replacename(ot)
        else:
            tmpint = 1
            for f in tmp:
                if tmpint == 1:
                    neww = replacename(f)
                else:
                    neww = neww + "(" + replacename(f)
                tmpint += 1

        return neww
        # tmp = writer.Split('(');
        # names = string.Empty
        # for t in tmp:
        #     if ')' in t:
        #         names = names + '(' + (t);
        #     else:
        #         names += UController.GetUnameByUno(t) + " ";
        #
        # return names.Replace(" ","");

    writer_set.short_description = "作者"
    def tashort_set(self, instance):
        newtashort = format_html(
            "<span title='{0}'>{1}</span> ".format(instance.tashort,
                                                   instance.tashort if len(instance.tashort) < 10 else (
                                                       (instance.tashort)[0:10] + "...")))
        return newtashort

    tashort_set.short_description = "简介"

    def print_set(self, instance):
        return format_html("<a href='/issue/tian/fengmian/{0}/' target='_blank'>打印</a>".format(instance.pk))

    print_set.short_description = "打印封面"


    def online_set(self, instance):
        return format_html(
            "<a href='/issue/tian/detail/{0}/' target='_blank'>在线查看</a>".format(
                instance.pk))

    online_set.short_description = "查看文档"

    def onekey(self, instance):
        return format_html(
            "<a class='onekey btn-primany' zdata='%s' zdatabt='%s' ><i class='fa fa-cloud-upload'></i></a>" % (
                instance.pk, instance.biaoti))

    onekey.short_description = "一键上传"
    def download_set(self,instance):

        return format_html("<a href='/static:/4634.zip' target='_blank'>下载</a>")

    download_set.short_description = "下载"

    def writer_set(self, instance):
        writer = instance.writer
        tmp = ''
        bflag = False
        if ' ' in writer:
            tmp = writer.replace("（", "(").replace("）", ")").split(' ')
        elif '(' in writer:
            tmp = writer.replace("（", "(").replace("）", ")").split('(')
            bflag = True
        else:
            return replacename(writer)

        neww = ''
        if not bflag:
            for ot in tmp:
                neww += replacename(ot)
        else:
            tmpint = 1
            for f in tmp:
                if tmpint == 1:
                    neww = replacename(f)
                else:
                    neww = neww + "(" + replacename(f)
                tmpint += 1

        return neww
        # tmp = writer.Split('(');
        # names = string.Empty
        # for t in tmp:
        #     if ')' in t:
        #         names = names + '(' + (t);
        #     else:
        #         names += UController.GetUnameByUno(t) + " ";
        #
        # return names.Replace(" ","");

    # writer_set.short_description = "作者"

    actions = [act_fabu, act_ta_download, act_tadoc_download,cleardafu,autosubmit]

    list_export_enable = False

class MnTSqAdmin(object):
    exclude = ['hyjc', 'submit_wyno', 'submit_name', 'submit_time', 'class_field', 'grper', 'writer', 'guanjian',
               'filesort', 'reconfirmnames', 'sq_chuli', 'filegov', 'fandui_counts', 'zhichi_counts', 'state', 'docx',
               'banliriqi', 'banlijieguo', 'banlidafu', 'yidafu', 'banlichengbandanwei', 'chengbandanwei',
               'tashort', 'tafilename', 'confirm_time', 'confirm', 'finish', 'filetogovs', 'asfinish', 'answer_time',
               'asfilename', 'view_counts']

    list_filter = ['biaoti', 'issueno','grper', 'writer', 'submit_time', 'finish', 'asfinish', 'confirm', 'hyjc','admin_status']
    search_fields = ['biaoti', 'issueno', 'writer']
    list_display = ['issueno', 'biaoti_set', 'mname','admin_status',
                    'online_set']
    list_per_page = 200
    list_editable = ['confirm', 'issueno', 'biaoti']
    show_all_rel_details = False
    style_fields = {'admin_status': 'm2m_transfer'}
    def confirm_set(self, instance):

        return "是" if instance.confirm else "否"

    confirm_set.short_description = "已发布"

    def biaoti_set(self, instance):
        newbiaoti = format_html(
            "<span title='标题:\n\t\t{0}\n关键词:\n\t\t{1}\n简介:\n\t\t{2}\n_________________________________________\n提交人:\t\t{3} {4}\n提交时间:\t{5}\n转换完成:\t{6}\n答复转换完成:\t{7}'>{8}</span> ".format(
                instance.biaoti,
                instance.guanjian if instance.guanjian else "无",
                instance.tashort if instance.tashort else "无",
                instance.submit_wyno,
                instance.submit_name,
                instance.submit_time,
                "是" if instance.finish else "否",
                "是" if instance.asfinish else "否",
                instance.biaoti if len(instance.biaoti) < 10 else (
                    (instance.biaoti)[0:10] + "...")))
        return newbiaoti

    biaoti_set.short_description = "标题"
    list_display_links = ['biaoti_set']

    def guanjian_set(self, instance):
        newguanjian = format_html(
            "<span title='{0}'>{1}</span> ".format(instance.guanjian,
                                                   instance.guanjian if len(instance.guanjian) < 10 else (
                                                       (instance.guanjian)[0:10] + "...")))
        return newguanjian

    guanjian_set.short_description = "关键词"

    def tashort_set(self, instance):
        newtashort = format_html(
            "<span title='{0}'>{1}</span> ".format(instance.tashort,
                                                   instance.tashort if len(instance.tashort) < 10 else (
                                                       (instance.tashort)[0:10] + "...")))
        return newtashort

    tashort_set.short_description = "简介"

    def online_set(self, instance):
        return format_html(
            "<a href='/issue/sqmy/detail/{0}/'  data-toggle=\"tooltip\" data-placement=\"top\"  data-original-title=\"{1}\" target='_blank'>在线查看</a>".format(
                instance.pk, "办理状态: [ %s ]" % (" ".join(map(lambda x: x.text, instance.admin_status.all())))))

    online_set.short_description = "查看文档"

    def block_extrabody(self, context, nodes):
        return """
        <script type="text/javascript">
        $(function(){
            $('[data-toggle="tooltip"]').tooltip()
       })
        </script>
        """

    def onekey(self, instance):
        return format_html("<a class='onekey btn-primany' ><i class='fa fa-cloud-upload'></i></a>".format(instance.pk))

    onekey.short_description = "一键上传"

    def download_set(self, instance):

        return format_html(
            "<a href='/static/4634.zip' target='_blank'>下载</a>")

    download_set.short_description = "下载"

    def writer_set(self, instance):
        writer = instance.writer
        tmp = ''
        bflag = False
        if ' ' in writer:
            tmp = writer.replace("（", "(").replace("）", ")").split(' ')
        elif '(' in writer:
            tmp = writer.replace("（", "(").replace("）", ")").split('(')
            bflag = True
        else:
            return replacename(writer)

        neww = ''
        if not bflag:
            for ot in tmp:
                neww += replacename(ot)
        else:
            tmpint = 1
            for f in tmp:
                if tmpint == 1:
                    neww = replacename(f)
                else:
                    neww = neww + "(" + replacename(f)
                tmpint += 1

        return neww
        # tmp = writer.Split('(');
        # names = string.Empty
        # for t in tmp:
        #     if ')' in t:
        #         names = names + '(' + (t);
        #     else:
        #         names += UController.GetUnameByUno(t) + " ";
        #
        # return names.Replace(" ","");

    # writer_set.short_description = "作者"

    actions = [act_fabu, act_sqdoc_download, act_sqctdoc_download,act_sq_download]


class MnTBljg_sqmyAdmin(object):
    list_filter = ['text']
    search_fields = ['text']
    list_display = ['text', 'sort', 'score', 'hide']
    exclude = ['value']
    # list_bookmarks = [{'title': u"社情民意", 'query': {'class_field': '社情民意'}},
    #                   {'title': u"提案", 'query': {'class_field': '提案'}},
    # ]

    list_editable = ['value']
    list_editable = ['text', 'score']
    ordering = ['sort']


xadmin.site.register(MnTBljg_sqmy, MnTBljg_sqmyAdmin)


class MnTBljg_tianAdmin(object):
    list_filter = ['text']
    search_fields = ['text']
    list_display = ['text', 'sort', 'score', 'hide']
    # list_bookmarks = [{'title': u"社情民意", 'query': {'class_field': '社情民意'}},
    #                   {'title': u"提案", 'query': {'class_field': '提案'}},
    # ]
    exclude = ['value']
    ordering = ['sort']

    list_editable = ['text', 'score']

class MnTLogAdmin(object):
    list_display = ['','']

class MnTATAdmin(object):
    list_display = ['sendto','pro_cbdw','pro_tano','pro_title','pro_acceptdate','zz_name','zz_tell1']
    list_filter = ['pro_acceptdate','pro_cbdw']
    search_fields = ['pro_tano','pro_title','zz_name']
    list_display_links = ['pro_tano']

def wyno_to_name(wyno):
        try:
            return MnTWy.objects.get(wyno=wyno).name
        except:
            return '查无此人'
class MnTMeetingAdmin(object):
    list_display = ['no','place','content','time','yuhui']
    list_filter = ['time','hyjc']
    list_display_links = []


    def yuhui(self,instance):
        return ",".join(map(lambda x: wyno_to_name(x.wyno), MnTMeetingDetail.objects.filter(mid=instance.pk)))
    yuhui.short_description = u'到会人'
    actions=[act_meeting_download]

xadmin.site.register(MnTBljg_tian, MnTBljg_tianAdmin)
xadmin.site.register(MnTGlobal, MnTGlobalAdmin)
xadmin.site.register(MnTLog,MnTLogAdmin )
xadmin.site.register(AutoSubmit, MnTATAdmin)
xadmin.site.register(MnTParty, MnTPartyAdmin)
xadmin.site.register(MnTWy, MnTWyAdmin)
xadmin.site.register(MnTZbdw, MnTTZbdwAdmin)
xadmin.site.register(MnTAd, MnTAdAdmin)
xadmin.site.register(MnTTHyjc, MnTTHyjcAdmin)
xadmin.site.register(MnTTa, MnTTaAdmin)
xadmin.site.register(MnTSq, MnTSqAdmin)
xadmin.site.register(Jiafenchi, JiafenchiAdmin)
xadmin.site.register(Jianfenchi, JianfenchiAdmin)
xadmin.site.register(Jjfenjilu, JjfenjiluAdmin)
xadmin.site.register(MnTMeeting, MnTMeetingAdmin)







