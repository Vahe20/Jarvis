import psutil


def diagnose_pc():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    return f"нагрузка процессора: {cpu}%, нагрузка оперативной памяти: {ram}%"
