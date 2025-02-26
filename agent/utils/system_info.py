import platform
import os

def get_system_name():
    """
    Get the normalized name of the current operating system.
    Returns 'windows', 'darwin', 'linux', or the platform name in lowercase.
    """
    system = platform.system().lower()
    return system

def get_username() -> str:
    return os.getlogin()

def get_machine_id() -> str:
    return platform.node()
