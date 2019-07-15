from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class SimpleMiddleware(MiddlewareMixin):
    # def __call__(self, *args, **kwargs):
    #     return HttpResponse("helloword")
    def peocess_request(self,request):
        return self.get_response(request)
    def process_responce(self,request,responce):
        print("处理了响应")
        ua=request.headers.get("User-Agent")
        print("当前访问工具为",ua)
        if ua.__contains__("python"):
            return HttpResponse('非法请求')
        else:
            return responce

