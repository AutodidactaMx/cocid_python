def fondo_amarillo(texto):
    return '\x1b[0;39;43m' + texto


def fondo_rojo(texto):
    return '\033[41m' + texto


def fondo_verde(texto):
    return '\033[42m' + texto


def fondo_azul(texto):
    return '\033[44m' + texto


def fondo_restablecer(texto):
    return '\033[0m' + texto
