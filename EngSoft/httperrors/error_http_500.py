class ErrorHttp500(Exception):
    def exception_500(request):
        raise ErrorHttp500("Erro interno no servidor")