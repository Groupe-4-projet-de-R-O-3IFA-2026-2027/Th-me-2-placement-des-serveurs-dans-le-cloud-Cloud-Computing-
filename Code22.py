import pulp

# 1. Définir les serveurs disponibles
serveurs = {
    "A": {"ram": 16, "cpu": 8, "cout": 10},
    "B": {"ram": 8, "cpu": 4, "cout": 6},
    "C": {"ram": 32, "cpu": 16, "cout": 18}
}

# 2. Définir les applications à héberger
applications = {
    "App1": {"ram": 8, "cpu": 4},
    "App2": {"ram": 4, "cpu": 2},
    "App3": {"ram": 12, "cpu": 6},
    "App4": {"ram": 6, "cpu": 2}
}
