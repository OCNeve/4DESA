class CustomMessage:
    @staticmethod
    def get(status, message, data=None):
        return {"status": status, "message": message, "data": data}

class CustomResponse:
    @staticmethod
    def get(token, message=None):
        return {"token": token, "message": message}