import platform
import os

def get_system_name() -> str:
    return platform.system().lower()

def get_username() -> str:
    return os.getlogin()

def get_machine_id() -> str:
    return platform.node()
