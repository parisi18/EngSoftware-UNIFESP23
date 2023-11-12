class ErrorHttp400(Exception):
    def exception_400(self):
        raise ErrorHttp400('Requisição mal formatada')