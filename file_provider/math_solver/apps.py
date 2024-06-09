import threading
from django.apps import AppConfig
# from .async_util import async_run_solution


class MathSolverConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'math_solver'

    # def ready(self) -> None:
    #     t = threading.Thread(target=async_run_solution)
    #     t.daemon = True
    #     t.start()