import sys
import os

# Agregamos la raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sum import suma

def test_suma():
    assert suma(2, 3) == 5
