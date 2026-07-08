import psutil


def check_cpu():

    return {
        "cpu_percent": psutil.cpu_percent()
    }


def check_memory():

    memory = psutil.virtual_memory()

    return {
        "memory_percent": memory.percent,
        "available_gb": round(
            memory.available / 1024**3,
            2
        )
    }