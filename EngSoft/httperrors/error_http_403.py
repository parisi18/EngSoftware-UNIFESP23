class ErrorHttp403(Exception):
    def exception_403(self):
        raise ErrorHttp403('Usuário sem permissão de acesso')