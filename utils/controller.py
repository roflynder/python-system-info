import psutil


def get_cpu_load() -> float:
    return psutil.cpu_percent()

def get_memory_load() -> float:
    return psutil.virtual_memory().percent

def get_all_info() -> dict:
    return dict({
        "cpu_usage": get_cpu_load(),
        "memory_usage": get_memory_load()
    })