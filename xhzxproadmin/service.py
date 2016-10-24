# -*-coding:utf-8 -*-
import win32serviceutil
import win32service
import win32event
import subprocess  
class TimeoutError(Exception):  
    pass  
    
    
    
def command(cmd, timeout=60):  
    """执行命令cmd，返回命令输出的内容。 
    如果超时将会抛出TimeoutError异常。 
    cmd - 要执行的命令 
    timeout - 最长等待时间，单位：秒 
    """  
    flag = True
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)  
    t_beginning = time.time()  
    seconds_passed = 0  
    while True:  
        if p.poll() is not None:  
            break  
        seconds_passed = time.time() - t_beginning  
        if timeout and seconds_passed > timeout:  
            p.terminate()  
            raise TimeoutError(cmd, timeout)  
            flag = False
        time.sleep(0.1)  
    return flag
class PythonService(win32serviceutil.ServiceFramework):
    """
    Usage: 'PythonService.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
    Options for 'install' and 'update' commands only:
     --username domain\username : The Username the service is to run under
     --password password : The password for the username
     --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
     --interactive : Allow the service to interact with the desktop.
     --perfmonini file: .ini file to use for registering performance monitor data
     --perfmondll file: .dll file to use when querying the service for
       performance data, default = perfmondata.dll
    Options for 'start' and 'stop' commands only:
     --wait seconds: Wait for the service to actually start or stop.
                     If you specify --wait with the 'stop' option, the service
                     and all dependent services will be stopped, each waiting
                     the specified period.
    """
    # 服务名
    _svc_name_ = "MnosPrintService"
    # 服务显示名称
    _svc_display_name_ = "Mnos Print Service"
    # 服务描述
    _svc_description_ = "Mnos Print Service."
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.isAlive = True
    def _getLogger(self):
        import logging
        import os
        import inspect
        logger = logging.getLogger('[MnosService]')
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
    def SvcDoRun(self):
        self.logger.error("服务启动了.")
        import os, sys, time, django
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xhzxpro.settings")
        django.setup()
        from xhzx.models import MnTTa, MnTAd, MnTLog
        from django.db.models import Q
        while self.isAlive:
            try:
                # MnTLog.objects.create(log_msg="轮询开始")
                Ads = MnTAd.objects.filter(finished=0)
                for entry in Ads:
                    # MnTLog.objects.create(log_msg=("%s" % entry.docname))
                    flag = command("D:\\FlashPaper2.2\\FlashPrinter.exe D:\\xhzx\\ad\\%s.%s -o D:\\xhzx\\ad\\%s.swf" % (
                        entry.docname, entry.docx, entry.docname),timeout = 10)
                    if flag:
                        entry.finished = 1
                        entry.save()
                        MnTLog.objects.create(
                            log_msg="转换完成",
                            log_type='INFO', objid=entry.id, objname='公告')
                Issues = MnTTa.objects.filter(Q(finish=0) | Q(asfinish=1))
                for entry in Issues:
                    # MnTLog.objects.create(log_msg=("%s" % entry.tafilename))
                    if entry.finish == 0:
                        tdoc = 'doc'
                        if entry.docx == 1:
                            tdoc = 'docx'
                        flag = command("D:\\FlashPaper2.2\\FlashPrinter.exe  D:\\xhzx\\done\\%s.%s -o  D:\\xhzx\\done\\%s.swf" % (
                            entry.tafilename, tdoc, entry.tafilename),timeout = 10)
                        if flag:
                            entry.finish = 1
                            entry.save()
                            MnTLog.objects.create(log_msg=" 转换完成", log_type='INFO',
                                                  objid=entry.id, objname=entry.class_field)
                    if entry.asfinish == 1:
                        adoc = 'doc'
                        if entry.asdocx == 1:
                            adoc = 'docx'
                        flag = command("D:\\FlashPaper2.2\\FlashPrinter.exe  D:\\xhzx\\done\\%s.%s -o  D:\\xhzx\\done\\%s.swf" % (
                            entry.asfilename, adoc, entry.asfilename),timeout = 10)
                        if flag:
                            entry.asfinish = 0
                            entry.save()
                            MnTLog.objects.create(log_msg="答复转换完成",
                                                  log_type='INFO', objid=entry.id,
                                                  objname=entry.class_field)
            except Exception as e:
                try:
                    MnTLog.objects.create(log_msg=("%s:%s" % ('异常', str(e))), log_type='ERROR')
                except:
                    self.logger.error("%s:%s" % ('异常', str(e)))
            time.sleep(10)
            # win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
    def SvcStop(self):
        # 先告诉SCM停止这个过程 
        self.logger.error("服务停止.")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # 设置事件 
        win32event.SetEvent(self.hWaitStop)
        self.isAlive = False
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)