# -*-coding:utf-8 -*-
__author__ = 'memorism'
from django_url_framework import ActionController
from xhzx.models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect


class MnTIssueController(ActionController):
    def edit(self, request, id=None):
        return {}

    def remove(self, request, id):
        return {}

    def detail(self, request, id):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        try:
            Issue = MnTTa.objects.get(pk=id)
            if Issue:
                writers = Issue.writer.split()
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

                except:
                    writer1 = {}
                    writer1['name'] = writers[0]
                writer2 = ''
                writer3 = ''
                writerother = ''
                if len(writers) > 1:
                    try:
                        writer2 = MnTWy.objects.get(wyno=writers[1])
                    except:
                        writer2 = writers[1]
                    if len(writers) >= 3:
                        try:
                            writer3 = MnTWy.objects.get(wyno=writers[2])
                        except:
                            writer3 = writers[2]
                    if len(writers) > 3:

                        for x in writers[3:]:
                            try:

                                writerother = writerother + " " +( (MnTWy.objects.get(wyno=x))).name
                            except:

                                writerother = writerother + " " + x

                return {'Issue': Issue, 'writer1': writer1, 'writer2': writer2, 'writer3': writer3,
                        'workpos1': workpos1, 'workpos2': workpos2, 'writerothers': writerother}
        except:
            return {'pname': '没有这个提案或社情民意'}

        return {}


def index(self, request):
    # return {'xx': Patient.objects.all()[0].patientpics_set.all()}

    return {}