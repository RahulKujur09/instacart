import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from src.configs import load_config

config = load_config()

print(config["app"]["name"])
print(config["spark"]["master"])
print(config["paths"]["bronze"])