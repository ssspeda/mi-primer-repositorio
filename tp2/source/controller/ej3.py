"""En este archivo se debe importar el archivo:
- ./controller.py
- ../util.py as util
- ../data/database.py as database
- ../tests/test_config.py as test_config
- ../tests/load_tests/ddos_simulation.py as ddos_simulation
- ../../main.py as main

Los imports deben hacerse de forma tal que funcionen con el siguiente
comando (estando parados dentro de la carpeta practico_02):
$PATH$/practico_02> python -m source.controller.ejercicio_03
"""

# Completar

# NO MODIFICAR - INICIO
import main
from source import util
from source.data import database
from source.controller import controller
from config import test_config
from tests.load_tests import ddos_simulation


assert main.name == "main"
assert util.name == "util"
assert database.name == "database"
assert controller.name == "controller"
assert test_config.name == "test_config"
assert ddos_simulation.name == "ddos_simulation"
# NO MODIFICAR - FIN

# Este es el último ejercicio del TP2
