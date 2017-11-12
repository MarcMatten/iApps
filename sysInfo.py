import psutil

def getCPU():
    return psutil.cpu_percent(interval=0.5)