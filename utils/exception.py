# class BaseException(Exception):
#     message = "An unknown exception occurred."
#     code = 100001
#
#     def __init__(self, message: str = None, **kwargs: dict):
#         self.kwargs = kwargs
#
#         if 'code' not in self.kwargs:
#             pass
#
#         if not message:
#             pass

class NovaException(Exception):
    pass

