from .carinho import Carinho


def carinho(request):
    return {'carinho': Carinho(request)}

