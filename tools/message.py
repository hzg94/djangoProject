from django.http import JsonResponse
class Class_message:
    def __init__(self):
        self.status = 200
        self.message = ""
    def get_message(self, message: str, status: int, result: dict):
        return JsonResponse({
            "message": message,
            "result": result
        }, status=status)
    def warn_message(self, message: str):
        return JsonResponse({
            "message:": message,
            "result": {}
        }, status=502)