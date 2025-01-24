#!/usr/bin/env python3

import re

def validar_correo(correo: str):
    regex = "[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}"
    if re.findall(regex, correo):
        return "El correo ingresado es válido"
    else:
        return "El correo ingresado es invalido"

print(validar_correo("soporte@hack4u.io"))