from src.config.tokens import private_data as pd

prefijo = "!"
DEBUGGING = 0
if DEBUGGING == 1:
    token = pd.token_debug
if DEBUGGING == 0:
    token = pd.token