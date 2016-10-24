from suds.client import Client

url = 'http://211.144.101.210/Services/AssessmentService.asmx?wsdl'
# url = 'http://www.webxml.com.cn/WebServices/TranslatorWebService.asmx?wsdl'
client = Client(url)
print client