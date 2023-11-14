class ErrorHttp404(Exception):
    def exception_404(self):
        raise ErrorHttp404('Recurso não encontrado')