import psutil
import GPUtil as gu

def show_gpu_temp():   
        
    gpu = gu.getGPUs()[0]
    return gpu.temperature


def show_cpu_freq():

    current_freq, _, _ = psutil.cpu_freq()
    return current_freq

def show_cpu_perecent():
    
    cpu_perecent = psutil.cpu_percent()
    return cpu_perecent

def cpu_core_count():
    cpu_cores = psutil.cpu_count()
    return cpu_cores

def show_memory_info():
    total_memory, available_memory, percent, used_memory, free_memory = psutil.virtual_memory()
    return percent

