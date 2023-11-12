class ErrorHttp401(Exception):
    def exception_401(self):
        raise ErrorHttp401('Cliente não autenticado')