# -*-coding:utf-8 -*-
from __future__ import unicode_literals

# from audit_log.models.managers import AuditLog
#
# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
# * Make sure each model has one field with primary_key=True
# * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from xhzxpro.settings import CURYEAR

shifou = ((1, u'是'), (0, u'否'))
from django.db import models


class MnTBljg_sqmy(models.Model):
    value = models.IntegerField(primary_key=True, verbose_name="值")
    sort = models.IntegerField(verbose_name="排序", blank=True)
    score = models.IntegerField(verbose_name="分数", blank=True, default=0)
    text = models.CharField(max_length=15, verbose_name="办理结果")
    hide = models.BooleanField(verbose_name="隐藏", default=False)

    class Meta:
        db_table = 'mn_t_bljg_sqmy'
        verbose_name = u"社情民意选项"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text


class MnTZbdw(models.Model):
    value = models.IntegerField(primary_key=True, verbose_name="值")
    sort = models.IntegerField(verbose_name="排序", blank=True)
    text = models.CharField(max_length=15, verbose_name="显示名称")
    hide = models.BooleanField(verbose_name="隐藏", default=False)

    class Meta:
        managed = False
        db_table = 'mn_t_t_tazbdw'
        verbose_name = u"提案主办单位"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text


class MnTZwh(models.Model):
    value = models.IntegerField(primary_key=True, verbose_name="值")
    text = models.CharField(max_length=15, verbose_name="专委会名")

    class Meta:
        managed = False
        db_table = 'mn_t_zwh'
        verbose_name = u"专委会"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text

class MnTBljg_tian(models.Model):
    value = models.IntegerField(primary_key=True, verbose_name="值")
    sort = models.IntegerField(verbose_name="排序", blank=True)
    score = models.IntegerField(verbose_name="分数", blank=True, default=0)
    text = models.CharField(max_length=15, verbose_name="办理结果")
    hide = models.BooleanField(verbose_name="隐藏", default=False)

    class Meta:
        managed = False
        db_table = 'mn_t_bljg_tian'
        verbose_name = u"提案办理选项"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text

class MnTAd(models.Model):
    name = models.CharField(db_column='Name', max_length=255, verbose_name="标题名称")
    docname = models.CharField(db_column='Docname', max_length=128, blank=True, verbose_name="文档名")
    enable = models.BooleanField(default=True, verbose_name="可见")
    content = models.TextField("内容", blank=False)
    submit_time = models.DateTimeField("上传时间", auto_now_add=True)
    class Meta:
        db_table = 'mn_t_ad'
        verbose_name = u"公告"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MnTTHyjc(models.Model):
    value = models.IntegerField(primary_key=True,blank=True)
    text = models.CharField(max_length=14,blank=True)
    sort = models.IntegerField(blank=True)
    type = models.CharField(max_length=8,blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_t_hyjc'
        verbose_name = u"会议届次"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text

class MnTAnswer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wyno = models.CharField(max_length=11, verbose_name="委员Number")
    name = models.CharField(max_length=16, blank=True, verbose_name="委员名")
    articleid = models.BigIntegerField(verbose_name="提案ID")
    type = models.IntegerField(verbose_name="类型")
    content = models.CharField(max_length=1600, blank=True, verbose_name="内容")
    important = models.IntegerField(blank=True, null=True, verbose_name="")
    visible = models.IntegerField(blank=True, null=True, verbose_name="仅作者可见")
    sub_time = models.DateTimeField(auto_now_add=True, verbose_name="提交时间")

    class Meta:
        managed = False
        db_table = 'mn_t_answer'
        verbose_name = u"评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.wyno


class MnTGlobal(models.Model):
    select_type = models.IntegerField(null=True, blank=True, verbose_name="预留")
    swf_answer_folder = models.CharField(max_length=30, blank=True, verbose_name="区政府会议届次")
    swf_issue_folder = models.CharField(max_length=30, blank=True, verbose_name="预留")
    autosubmit_start = models.BooleanField(default=False, verbose_name="自动上传")
    jjf_start = models.BooleanField( default=False, verbose_name="加减分系统")
    score_url = models.CharField(max_length=64, blank=True, verbose_name="加减分系统Url")
    search_ti_all = models.CharField(max_length=6, blank=True, verbose_name="预留")
    cur_year = models.CharField(max_length=30, verbose_name="当前年份")
    # time.strftime("%Y", time.localtime())

    panfu = models.CharField(max_length=2, blank=True, verbose_name="盘符")
    dqhyjc = models.CharField(max_length=15, blank=True, verbose_name="会议届次前缀 中文")
    dqhyjc_en = models.CharField(max_length=4, blank=True, verbose_name="会议届次前缀")
    year = models.CharField(max_length=8, blank=True, verbose_name="年前缀")

    class Meta:
        managed = False
        db_table = 'mn_t_global'
        verbose_name = u"全局参数"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "设置"


class MnTGov(models.Model):
    value = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=14)
    sort = models.IntegerField()
    type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'mn_t_gov'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text


class MnTGroup(models.Model):
    value = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=14)
    sort = models.IntegerField()
    type = models.CharField(max_length=8)
    sqmy = models.IntegerField()
    sqmy_sort = models.IntegerField()
    ta = models.IntegerField()
    ta_sort = models.IntegerField()
    meeting = models.IntegerField()
    meeting_sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mn_t_group'
        verbose_name = u"组"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text


class MnTTa(models.Model):
    issueno = models.CharField(max_length=30, blank=True, verbose_name="编号")
    hyjc = models.CharField(max_length=15, blank=True, verbose_name="会议届次")
    submit_time = models.DateTimeField(verbose_name="提交时间", auto_now_add=True)
    submit_wyno = models.CharField(max_length=16, blank=True, verbose_name="提交者编号")
    submit_name = models.CharField(max_length=8, blank=True, verbose_name="提交人名")
    class_field = models.CharField(db_column='class', max_length=10,
                                   blank=True, default="提案",
                                   verbose_name="提案")  # Field renamed because it was a Python reserved word.
    grper = models.CharField(max_length=10, blank=True, verbose_name="个人或集体",
                             choices=(("个人", "个人"), ("集体", "集体")))
    writer = models.CharField(max_length=80, blank=True, verbose_name="作者")
    biaoti = models.CharField(max_length=160, blank=True, verbose_name="标题")
    guanjian = models.CharField(max_length=160, blank=True, verbose_name="关键词")

    qkfy = models.TextField(blank=True, verbose_name="情况反映")
    yjhjy = models.TextField(blank=True, verbose_name="意见和建议")
    chengbandanwei = models.CharField(max_length=100, blank=True, verbose_name="承办单位")

    tashort = models.CharField(max_length=400, blank=True, verbose_name="简介")
    tafilename = models.CharField(max_length=80, blank=True, verbose_name="文件名")
    finish = models.IntegerField(blank=True, null=True, verbose_name="转换完成", choices=shifou, default=1)
    confirm = models.IntegerField(blank=True, null=True, verbose_name="发布", choices=shifou, default=1)
    confirm_time = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    reconfirmnames = models.CharField(max_length=80, blank=True, verbose_name="分类",
                                      choices=map(lambda x: (x, x), ["A","B", "C",  "D"]))  # bo_type
    filegov = models.IntegerField(blank=True, null=True, verbose_name="")
    filesort = models.CharField(max_length=16, blank=True, verbose_name="类型",
                                choices=map(lambda x: (x, x), ["党派团体", "个人联名"]))  # filesort


    filetogovs = models.CharField(max_length=100, blank=True, verbose_name="建议承办单位")
    asfinish = models.IntegerField(blank=True, null=True, verbose_name="答复转换完成", choices=shifou, default=1)
    answer_time = models.DateTimeField(blank=True, null=True, verbose_name="答复时间")
    asfilename = models.CharField(max_length=80, blank=True, verbose_name="答复文件名")
    view_counts = models.BigIntegerField(blank=True, null=True, default=0, verbose_name="浏览次数")
    fandui_counts = models.BigIntegerField(blank=True, null=True, default=0, verbose_name="支持次数")
    zhichi_counts = models.BigIntegerField(blank=True, null=True, default=0, verbose_name="反对次数")
    state = models.IntegerField("状态", default=0)
    docx = models.IntegerField("docx格式", default=0)
    banliriqi = models.CharField("办理日期", default="", max_length=32, blank=True)
    banlijieguo = models.CharField("办理结果", default="", max_length=64, blank=True)
    banlidafu = models.TextField("办理答复", null=True, blank=True)
    fenguan = models.CharField("分管领导", max_length=16, blank=True, default="")
    banlichengbandanwei = models.CharField("办理承办单位", default="", max_length=64, blank=True)
    yidafu = models.BooleanField("已答复", default=False)
    lajiafen = models.BooleanField("立案加分", default=False)
    admin_status = models.ForeignKey(MnTBljg_tian, verbose_name="办理状态", blank=True, null=True)

    zhuban = models.ManyToManyField(MnTZbdw, verbose_name="主办", blank=True, null=True,related_name="zhuban")
    huiban = models.ManyToManyField(MnTZbdw, verbose_name="会办", blank=True, null=True, related_name="huiban")
    heban = models.ManyToManyField(MnTZbdw, verbose_name="合办", blank=True, null=True, related_name="heban")
    mno = models.CharField(max_length=64, verbose_name="作者固定编号", blank=True, null=True)
    mnob = models.CharField(max_length=64, verbose_name="作者编号", blank=True, null=True)
    mname = models.CharField(max_length=64, verbose_name="作者姓名", blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mn_t_ta'
        verbose_name = u"提案"
        verbose_name_plural = verbose_name

    def delete(self, *args, **kwargs):
        mnostr = self.mno
        mnobstr = self.mnob
        mnamestr = self.mname
        if "," in self.mno:
            if len(self.mno.split(',')) > 3:
                mnostr = ",".join((self.mno.split(','))[:3])
                mnobstr = ",".join((self.mnob.split(','))[:3])
                mnamestr = ",".join((self.mname.split(','))[:3])
        Jianfenchi.objects.create(djf_issueno=self.issueno,
                                  djf_issueid=self.pk,
                                  djf_wyno=mnostr,
                                  djf_wynob=mnobstr,
                                  djf_issuebt=self.biaoti,
                                  djf_wyname=mnamestr,
                                  djf_type=2 if (self.mno and "," in self.mno) else 1,
                                  djf_time=self.submit_time)
        super(MnTTa, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):


        mnostr = self.mno
        mnobstr = self.mnob
        mnamestr = self.mname
        if "," in self.mno:
            if len(self.mno.split(',')) > 3:
                mnostr = ",".join((self.mno.split(','))[:3])
                mnobstr = ",".join((self.mnob.split(','))[:3])
                mnamestr = ",".join((self.mname.split(','))[:3])

        if  not self.lajiafen and  self.admin_status:


            Jiafenchi.objects.create(djf_issueno=self.issueno,
                                     djf_tos=self.class_field,
                                     djf_issueid=self.pk,
                                     djf_issuebt=self.biaoti,
                                     djf_wyno=mnostr,
                                     djf_wynob=mnobstr,
                                     djf_wyname=mnamestr,
                                     djf_state=2,
                                     djf_type=2 if (self.mno and ',' in self.mno) else 1,
                                     djf_time=self.submit_time)
            self.lajiafen = True


        else:
            if self.lajiafen and not self.admin_status:
                Jianfenchi.objects.create(djf_issueno=self.issueno,
                                          djf_issueid=self.pk,
                                          djf_wyno=mnostr,
                                          djf_wynob=mnobstr,
                                          djf_issuebt=self.biaoti,
                                          djf_wyname=mnamestr,
                                          djf_type=2 if (self.mno and "," in self.mno) else 1,
                                          djf_time=self.submit_time)
                self.lajiafen = False
        super(MnTTa, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.biaoti


class MnTSq(models.Model):
    issueno = models.CharField(max_length=30, blank=True, verbose_name="编号")
    hyjc = models.CharField(max_length=15, blank=True, verbose_name="会议届次")
    submit_time = models.DateTimeField(verbose_name="提交时间", auto_now_add=True)
    submit_wyno = models.CharField(max_length=16, blank=True, verbose_name="提交者编号")
    submit_name = models.CharField(max_length=8, blank=True, verbose_name="提交人名")
    class_field = models.CharField(db_column='class', max_length=10,
                                   blank=True, default="社情民意",
                                   verbose_name="社情民意")  # Field renamed because it was a Python reserved word.
    grper = models.CharField(max_length=10, blank=True, verbose_name="个人")
    writer = models.CharField(max_length=80, blank=True, verbose_name="作者")
    biaoti = models.CharField(max_length=160, blank=True, verbose_name="标题")
    guanjian = models.CharField(max_length=160, blank=True, verbose_name="关键词")

    qkfy = models.TextField(blank=True, verbose_name="情况反映")
    yjhjy = models.TextField(blank=True, verbose_name="意见和建议")
    sqmy_contact = models.CharField(max_length=255, blank=True, verbose_name="执笔人联系电话")
    sqmy_zbname = models.CharField(max_length=16, blank=True, verbose_name="执笔人姓名")
    sqmy_zbwork = models.CharField(max_length=255, blank=True, verbose_name="执笔人工作单位和职务")
    chengbandanwei = models.CharField(max_length=100, blank=True, verbose_name="承办单位")

    tashort = models.CharField(max_length=400, blank=True, verbose_name="简介")
    tafilename = models.CharField(max_length=80, blank=True, verbose_name="文件名")
    finish = models.IntegerField(blank=True, null=True, verbose_name="转换完成", choices=shifou, default=1)
    confirm = models.IntegerField(blank=True, null=True, verbose_name="发布", choices=shifou, default=1)
    confirm_time = models.DateTimeField(blank=True, null=True, verbose_name="发布时间")
    reconfirmnames = models.CharField(max_length=80, blank=True, verbose_name=" ")
    filegov = models.IntegerField(blank=True, null=True, verbose_name="")
    filesort = models.CharField(max_length=10, blank=True, verbose_name="")
    filetogovs = models.CharField(max_length=100, blank=True, verbose_name="建议承办单位")
    asfinish = models.IntegerField(blank=True, null=True, verbose_name="答复转换完成", choices=shifou, default=1)
    answer_time = models.DateTimeField(blank=True, null=True, verbose_name="答复时间")
    asfilename = models.CharField(max_length=80, blank=True, verbose_name="答复文件名")
    view_counts = models.BigIntegerField(blank=True, null=True, default=0, verbose_name="浏览次数")
    fandui_counts = models.BigIntegerField(blank=True, null=True, default=0, verbose_name="支持次数")
    zhichi_counts = models.BigIntegerField(blank=True, null=True, default=0, verbose_name="反对次数")
    state = models.IntegerField("状态", default=0)
    docx = models.IntegerField("docx格式", default=0)
    plus = models.BooleanField("答复是docx格式", default=False)
    banliriqi = models.CharField("办理日期", default="", max_length=32)
    banlijieguo = models.CharField("办理结果", default="", max_length=64)
    banlidafu = models.TextField("办理答复", blank=True, null=True)
    banlichengbandanwei = models.CharField("办理承办单位", default="", max_length=64)
    yidafu = models.BooleanField("已答复", default=0)
    sq_chuli = models.IntegerField("处理", default=0, blank=True, choices=((0, u'留存'), (1, u'移交转办')))
    admin_status = models.ManyToManyField(MnTBljg_sqmy, verbose_name="办理状态", blank=True, null=True)
    mno = models.CharField(max_length=64, verbose_name="作者固定编号", blank=True, null=True)
    mnob = models.CharField(max_length=64, verbose_name="作者编号", blank=True, null=True)
    mname = models.CharField(max_length=64, verbose_name="作者姓名", blank=True, null=True)
    curstat = models.TextField(verbose_name="当前状态", default="", blank=True)
    curscore = models.IntegerField(verbose_name="当前分数", default=0, blank=True)

    class Meta:
        # managed = False
        db_table = 'mn_t_sq'
        verbose_name = u"社情民意"
        verbose_name_plural = verbose_name

    def delete(self, *args, **kwargs):
        if self.grper == '个人':
            Jiafenchi.objects.create(djf_wyno=self.mno,
                                         djf_wynob=self.mnob,
                                         djf_wyname=self.mname,
                                         djf_year=CURYEAR,
                                         djf_issuebt=self.biaoti,
                                         djf_issueno=self.issueno,
                                         djf_issueid=self.pk,
                                         djf_tos="社情民意",
                                         djf_date=self.submit_time,
                                         djf_detail="社情民意《%s》%s 被删除了" % (
                                             self.biaoti, self.issueno),
                                         fenshu=0 - self.curscore
                                         )
        super(MnTSq, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.biaoti


from django.db.models.signals import m2m_changed


def handle_flow(sender, instance, *args, **kwargs):
    if kwargs['action'] in ["post_add"]:
        if len(instance.admin_status.all()) > 0 and instance.grper == "个人":
            newstat = " ".join(map(lambda x: x.text, instance.admin_status.all()))
            if instance.curstat != newstat:
                scores = 0
                for asa in instance.admin_status.all():
                    scores += asa.score
                Jiafenchi.objects.create(djf_wyno=instance.mno,
                                         djf_wynob=instance.mnob,
                                         djf_wyname=instance.mname,
                                         djf_year=CURYEAR,
                                         djf_issuebt=instance.biaoti,
                                         djf_issueno=instance.issueno,
                                         djf_issueid=instance.pk,
                                         djf_tos="社情民意",
                                         djf_date=instance.submit_time,
                                         djf_detail="社情民意《%s》%s 状态由[%s] -> [%s]" % (
                                             instance.biaoti, instance.issueno,
                                             instance.curstat, newstat),
                                         fenshu=scores - instance.curscore
                                         )
                fenshu = scores - instance.curscore
                instance.curscore = fenshu
                print instance.curscore
                instance.curstat = newstat
                instance.save()

    if kwargs['action'] in ["post_clear"]:
        if len(instance.admin_status.all()) > 0:

            newstat = " ".join(map(lambda x: x.text, instance.admin_status.all()))
        else:
            newstat = ""

        if instance.curstat != newstat:
            scores = 0
            # for asa in instance.admin_status.all():
            #     scores += asa.score
            Jiafenchi.objects.create(djf_wyno=instance.mno,
                                     djf_wynob=instance.mnob,
                                     djf_wyname=instance.mname,
                                     djf_year=CURYEAR,
                                     djf_issuebt=instance.biaoti,
                                     djf_issueno=instance.issueno,
                                     djf_issueid=instance.pk,
                                     djf_tos="社情民意",
                                     djf_date=instance.submit_time,
                                     djf_detail="社情民意《%s》%s 状态由[%s] -> [%s]" % (
                                         instance.biaoti, instance.issueno,
                                         instance.curstat, newstat),
                                     fenshu=0 - instance.curscore
                                     )
            instance.curscore = 0
            print instance.curscore
            instance.curstat = newstat
            instance.save()


m2m_changed.connect(handle_flow, sender=MnTSq.admin_status.through)
class MnTJiebie(models.Model):
    value = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'mn_t_jiebie'
        verbose_name = u"界别"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text


class MnTLevel(models.Model):
    comment = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_level'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.comment


class MnTLog(models.Model):
    log_msg = models.CharField("日志内容", max_length=256)
    objid = models.BigIntegerField("对象id")
    objname = models.CharField("对象名称", max_length=16)
    log_type = models.CharField("日志类型", choices=(('ERROR', u'ERROR'), ('INFO', u'INFO')), max_length=16)
    log_time = models.DateTimeField("时间", auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'mn_t_log'
        verbose_name = u"日志"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.log_msg


class MnTMeeting(models.Model):
    # id = models.IntegerField(primary_key=True)  # AutoField?
    no = models.CharField(max_length=20, blank=True,verbose_name="会议名称")
    place = models.CharField(max_length=100, blank=True,verbose_name="会议地点")
    type = models.CharField(max_length=20, blank=True,verbose_name="类型")
    zbdw = models.CharField(max_length=5, blank=True,verbose_name="主办单位")
    hyjc = models.CharField(max_length=12, blank=True,verbose_name="会议届次")
    time = models.DateTimeField(blank=True, null=True,verbose_name="时间")
    content = models.CharField(max_length=255, blank=True,verbose_name="内容")
    everyone = models.IntegerField(blank=True, null=True,verbose_name="全体会议")
    sub_wyno = models.CharField(max_length=16, blank=True,verbose_name="提交人")
    sub_time = models.DateTimeField(blank=True, null=True,verbose_name="提交时间")
    finished = models.IntegerField(blank=True, null=True,verbose_name="会议完结")
    comment = models.CharField(max_length=60, blank=True,verbose_name="注释")

    class Meta:
        db_table = 'mn_t_meeting'
        verbose_name = u"会议"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.no


class MnTMeetingCopy(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    no = models.CharField(max_length=20, blank=True)
    place = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=20, blank=True)
    men_type = models.CharField(max_length=20, blank=True)
    zbdw = models.CharField(max_length=5, blank=True)
    member = models.TextField(blank=True)
    flag = models.CharField(max_length=8, blank=True)
    came = models.TextField(blank=True)
    absence = models.TextField(blank=True)
    late = models.TextField(blank=True)
    hyjc = models.CharField(max_length=12, blank=True)
    time = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=255, blank=True)
    comment = models.CharField(max_length=60, blank=True)
    everyone = models.IntegerField(blank=True, null=True)
    sub_wyno = models.CharField(max_length=16, blank=True)
    sub_time = models.DateTimeField(blank=True, null=True)
    finished = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mn_t_meeting_copy'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.no


class MnTMeetingDetail(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    wyno = models.CharField(max_length=16, blank=True)
    mid = models.CharField(max_length=8, blank=True)
    ncj = models.IntegerField(blank=True, null=True)
    nqj = models.IntegerField(blank=True, null=True)
    ycj = models.IntegerField(blank=True, null=True)
    yqx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mn_t_meeting_detail'
        verbose_name = u"会议"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.wyno


class MnTMeetingType(models.Model):
    value = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=14)
    sort = models.IntegerField()
    type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'mn_t_meeting_type'
        verbose_name = u"会议类型"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text


class MnTMsg(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    msg = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_msg'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MnTMsgType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=60, blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_msg_type'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MnTNotice(models.Model):
    type = models.IntegerField("类型")
    text = models.TextField("内容")
    time = models.DateTimeField(auto_now_add=True)
    wyno = models.CharField("委员编号", max_length=16)
    detail = models.CharField("详情页", max_length=64)
    unread = models.BooleanField("未读", default=True)
    enable = models.BooleanField("存着", default=True)

    class Meta:
        managed = False
        db_table = 'mn_t_notice'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text


class MnTParty(models.Model):
    value = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=15)

    class Meta:
        managed = False
        verbose_name = u'党派'
        verbose_name_plural = verbose_name
        db_table = 'mn_t_party'

    def __unicode__(self):
        return self.text


class MnTPersonal(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    wyid = models.IntegerField()
    select_type = models.IntegerField()
    session = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mn_t_personal'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MnTPm(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content = models.CharField(max_length=255)
    from_field = models.CharField(db_column='from', max_length=20,
                                  blank=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=20, blank=True)
    time = models.DateTimeField()
    check = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mn_t_pm'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MnTSurvey(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    men_type = models.CharField(max_length=20)
    men = models.CharField(max_length=255)
    time = models.DateTimeField()
    content = models.CharField(max_length=255)
    comment = models.CharField(max_length=60, blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_survey'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MnTSurveyType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=25)
    comment = models.CharField(max_length=60, blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_survey_type'
        verbose_name = u"MnTSurveyType"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class MnTSyslog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    actiong = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(blank=True, null=True)
    act_id = models.CharField(max_length=8, blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_syslog'
        verbose_name = u"系统日志"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.actiong


#
# class MnTTSqmy(models.Model):
#     value = models.IntegerField(primary_key=True)
#     text = models.CharField(max_length=14)
#     sort = models.IntegerField()
#     type = models.CharField(max_length=8)
#
#     class Meta:
#         managed = False
#         db_table = 'mn_t_t_sqmy'
#         verbose_name = u"社情民意组织集体"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.text


# class MnTTZbdw(models.Model):
#     value = models.IntegerField(primary_key=True)
#     text = models.CharField(max_length=14)
#     sort = models.IntegerField()
#     type = models.CharField(max_length=8)
#
#     class Meta:
#         managed = False
#         db_table = 'mn_t_t_zbdw'
#         verbose_name = u"主办单位"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.text


class MnTTips(models.Model):
    name = models.CharField(max_length=16, blank=True)
    wyno = models.CharField(max_length=16, blank=True)
    tips = models.CharField(max_length=255, blank=True)
    meeting = models.TextField(blank=True)
    notice = models.TextField(blank=True)
    ta = models.CharField(max_length=255, blank=True)
    sqmy = models.CharField(max_length=255, blank=True)
    iswy = models.IntegerField(db_column='IsWy', blank=True, null=True)  # Field name made lowercase.
    mcounts = models.IntegerField()
    acounts = models.IntegerField()
    adur_list = models.TextField(blank=True, verbose_name="公告查看列表")

    class Meta:
        managed = False
        db_table = 'mn_t_tips'
        verbose_name = u"提示"
        verbose_name_plural = verbose_name

        # def __unicode__(self):
        # return "{wyno} {wyname}".format(wyno=self.wyno,wyname=self.name)


class MnTUserlog(models.Model):
    uid = models.CharField(max_length=16, blank=True)
    message = models.CharField(max_length=1024, blank=True)
    logger = models.CharField(max_length=255, blank=True)
    level = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mn_t_userlog'
        verbose_name = u"委员日志"
        verbose_name_plural = verbose_name

        # def __unicode__(self):
        # return "{wyno} {wyname}".format(wyno=self.wyno,wyname=self.name)


class MnTWy(models.Model):
    photo = models.CharField(max_length=16, blank=True, null=True, verbose_name="照片")
    wyno = models.CharField(max_length=255, blank=True, verbose_name="委员编号", null=True)
    wy_id = models.CharField(max_length=8, blank=True, verbose_name="委员id", null=True)
    name = models.CharField(max_length=10, blank=True, verbose_name="姓名")
    race = models.CharField(max_length=10, blank=True, verbose_name="民族", null=True)
    sex = models.IntegerField(blank=True, null=True, verbose_name="性别", choices=((1, "女"), (0, "男")), default=1)
    birth = models.DateField(blank=True, null=True, verbose_name="生日", auto_now_add=True)
    party = models.ForeignKey(MnTParty, null=True, blank=True, verbose_name="党派", related_name="party1")
    party2 = models.ForeignKey(MnTParty, null=True, blank=True, verbose_name="第二党派", related_name="party2")
    jiebie = models.ForeignKey(MnTJiebie, blank=True, null=True, verbose_name="界别")
    zwh = models.ForeignKey(MnTZwh, blank=True, null=True, verbose_name="专委会")
    zwh2 = models.ForeignKey(MnTZwh, blank=True, null=True, verbose_name="第二专委会", related_name="seczwh")
    exewy = models.BooleanField(blank=True, verbose_name="常务委员", default=False)
    workpos = models.CharField(max_length=100, blank=True, null=True, verbose_name="工作单位")
    workplace = models.CharField(max_length=60, blank=True, null=True, verbose_name="工作单位地址")
    workzip = models.CharField(max_length=6, blank=True, null=True, verbose_name="工作单位邮编")
    workphone = models.CharField(max_length=12, blank=True, null=True, verbose_name="工作电话")
    homeplace = models.CharField(max_length=60, blank=True, null=True, verbose_name="家庭住址")
    homezip = models.CharField(max_length=6, blank=True, null=True, verbose_name="家庭住址邮编")
    homephone = models.CharField(max_length=12, blank=True, null=True, verbose_name="家庭电话")
    cellphone = models.CharField(max_length=11, blank=True, verbose_name="手机")
    mailadd = models.CharField(max_length=40, blank=True, null=True, verbose_name="电子邮件地址")
    edu = models.CharField(max_length=40, blank=True, null=True, verbose_name="学历")
    grade = models.CharField(max_length=40, blank=True, null=True, verbose_name="学位")
    profpos = models.CharField(max_length=40, blank=True, null=True, verbose_name="职称")
    natplace = models.CharField(max_length=20, blank=True, null=True, verbose_name="籍贯")
    netup = models.IntegerField(blank=True, null=True, verbose_name="登录次数")
    logintime = models.DateTimeField(blank=True, null=True,verbose_name="登录时间")
    lastlogin = models.DateTimeField(blank=True, null=True, verbose_name="上次登录时间")
    bz = models.CharField(max_length=100, blank=True, null=True, verbose_name="备注")
    passwd = models.CharField(max_length=60, blank=True, null=True, verbose_name="密码")
    level = models.IntegerField(blank=True, null=True, verbose_name="级别")
    type = models.IntegerField(blank=True, null=True, verbose_name="类型")
    cpucardid = models.CharField(db_column='CpuCardId', max_length=8, null=True,
                                 verbose_name="卡ID")  # Field name made lowercase.
    needatt = models.IntegerField(db_column='Needatt', default=True)  # Field name made lowercase.
    levelwut = models.IntegerField(db_column='Levelwut', default=False)  # Field name made lowercase.
    levelwus = models.IntegerField(db_column='Levelwus', default=False)  # Field name made lowercase.
    hasuserinfo = models.IntegerField(db_column='Hasuserinfo', default=True)  # Field name made lowercase.
    levelmodifyuserinfo = models.BooleanField(db_column='LevelModifyuserinfo',
                                              default=False, verbose_name="修改用户资料")  # Field name made lowercase.
    levelad = models.BooleanField(db_column='LevelAD', default=True)  # Field name made lowercase.
    levelmeeting = models.IntegerField(db_column='LevelMeeting', default=True)  # Field name made lowercase.
    iswy = models.BooleanField(db_column='IsWY', default=True, verbose_name="委员")  # Field name made lowercase.
    enable = models.BooleanField(verbose_name="启用", default=True)
    lastedittime = models.DateTimeField(verbose_name="最后一次修改信息的时间",blank=True)

    class Meta:
        managed = False
        db_table = 'mn_t_wy'
        verbose_name = u"委员信息"
        verbose_name_plural = verbose_name

    def getnamebyuno(self, uno):
        get = MnTWy.objects.filter(wyno=uno)
        if (get):
            return get.name

    def __unicode__(self):
        return "{wyno} {wyname}".format(wyno=self.wyno, wyname=self.name)


class Jianfenchi(models.Model):
    djf_issueno = models.CharField(max_length=16, verbose_name="文档编号",blank=True)
    djf_issueid = models.CharField(max_length=16, verbose_name="文档Id")
    djf_wyno = models.CharField(max_length=128, verbose_name="委员固定编号")
    djf_wynob = models.CharField(max_length=128, verbose_name="委员编号")
    djf_issuebt = models.CharField(max_length=256, verbose_name="文档标题")
    djf_wyname = models.CharField(max_length=32, verbose_name="委员姓名")
    djf_type = models.SmallIntegerField(verbose_name="类型", default=1, choices=((1, u'个人提案'), (2, u'联名提案')))
    djf_time = models.DateTimeField(verbose_name="文档提交的时间", null=True)
    time = models.DateTimeField(verbose_name="待减分时间", auto_now_add=True)

    class Meta:
        db_table = 'mn_t_jianfenchi'
        verbose_name = u"减分池"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s: %s待减分" % (self.time, self.djf_wyname)


class Jiafenchi(models.Model):
    djf_tos = models.CharField(max_length=16, verbose_name="提案或者社情民意", default="提案")
    djf_issueid = models.CharField(max_length=16, verbose_name="文档Id")
    djf_issueno = models.CharField(max_length=16, verbose_name="文档编号", null=True,blank=True)
    djf_issuebt = models.CharField(max_length=256, verbose_name="文档标题")
    djf_wyno = models.CharField(max_length=128, verbose_name="委员固定编号")
    djf_wynob = models.CharField(max_length=128, verbose_name="委员编号")
    djf_wyname = models.CharField(max_length=32, verbose_name="委员姓名")
    djf_state = models.SmallIntegerField(verbose_name="状态", default=1, choices=((1, u'已提交'), (2, u'已提交的被立案')))
    djf_type = models.SmallIntegerField(verbose_name="类型", default=1, choices=((1, u'个人'), (2, u'联名')))
    djf_time = models.DateTimeField(verbose_name="文档提交的时间", null=True,blank=True)
    djf_year = models.CharField(max_length=8, verbose_name="考核所属年份", null=True,blank=True)
    djf_date = models.DateField(verbose_name="文档提交的日期", null=True,blank=True)
    djf_detail = models.CharField(max_length=256, verbose_name="加分详情",blank=True, null=True)
    time = models.DateTimeField(verbose_name="待加分时间", auto_now_add=True,blank=True)
    fenshu = models.IntegerField(verbose_name="待加分", null=True,blank=True)

    class Meta:
        db_table = 'mn_t_jiafenchi'
        verbose_name = u"加分池"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s: %s 因如下原因待%s %s分:%s" % (
            self.time, self.djf_wyname, "加" if self.fenshu >= 0 else "减", self.fenshu, self.djf_detail)


class Jjfenjilu(models.Model):
    djf_detail = models.CharField(max_length=256, verbose_name="加分详情", null=True)
    time = models.DateTimeField(verbose_name="得分时间", auto_now_add=True)

    class Meta:
        verbose_name = u"得分记录"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s: %s得分 %s分" % (self.time, self.djf_detail)


class AutoSubmit(models.Model):
    pro_tano= models.CharField(max_length=16, blank=True, verbose_name="编号")
    pro_title= models.CharField(max_length=128, blank=True, verbose_name="标题")
    pro_qkfy= models.TextField(blank=True, verbose_name="情况反映")
    pro_yjhjy= models.TextField(blank=True, verbose_name="意见和建议")
    pro_cbdw= models.CharField(max_length=32, blank=True, verbose_name="主办")
    pro_type=  models.CharField(max_length=32, blank=True, verbose_name="类型",
                                choices=map(lambda x: (x, x), ["党派团体", "个人联名"]))  # filesort
    pro_acceptdate= models.CharField(max_length=32, verbose_name="提交时间")
    pro_hebandw= models.CharField(max_length=32, blank=True, verbose_name="合办")
    pro_huibandw= models.CharField(max_length=32, blank=True, verbose_name="会办")
    pro_leader= models.CharField(max_length=32, blank=True, verbose_name="分管领导")
    pro_bo_type= models.CharField(max_length=64, blank=True, verbose_name="分类",
                                      choices=map(lambda x: (x, x), ["财政经济类","城市建设和管理类", "教科文卫体类",  "综合类"]))
    pro_partyindex= models.CharField(max_length=32, blank=True, verbose_name="会议届次")
    zz_name=models.CharField(max_length=64, blank=True, verbose_name="作者姓名")
    zz_tell1= models.CharField(max_length=16, blank=True, verbose_name="作者联系电话1")
    zz_tell2= models.CharField(max_length=16, blank=True, verbose_name="作者联系电话2")
    zz_gzdw= models.CharField(max_length=80, blank=True, verbose_name="作者工作单位")
    zz_zwh= models.CharField(max_length=32, blank=True, verbose_name="作者专委会")
    zz_jb= models.CharField(max_length=32, blank=True, verbose_name="作者界别")
    zz_dp= models.CharField(max_length=32, blank=True, verbose_name="作者党派")
    sendto = models.BooleanField(verbose_name="已向上提交",default=False)
    class Meta:
        verbose_name = u"自动提交"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "%s:《%s》, %s" % (self.pro_tano, self.pro_title,"已提交" if self.sendto else "未提交")

