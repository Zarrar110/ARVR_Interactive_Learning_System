# core_scripts/test_vpython.py
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from vpython import *

# sphere(color=color.cyan, radius=1)
box(pos=vector(2, 0, 0), color=color.orange)

while True:
    rate(30)