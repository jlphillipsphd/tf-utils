import tensorflow as tf
from . import devices

def create_strategy(devices):
    ids = [device_id(device) for device in devices]
    if len(devices) == 1:
        return tf.distribute.OneDeviceStrategy(ids[0])
    return tf.distribute.MirroredStrategy(ids)

def cpu(index: int=0):
    cpus = devices.select_cpu(index)
    return create_strategy(cpus)

def gpu(indices: int=None, cpu_index=0, use_dynamic_memory=False):
    gpus = devices.select_gpu(indices, cpu_index, use_dynamic_memory)
    return create_strategy(gpus)