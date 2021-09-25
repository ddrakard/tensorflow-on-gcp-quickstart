import logging
import os
import sys

from contextlib import contextmanager

import tensorflow as tf


def print_environment_variable(name):
    if name in os.environ:
        print(name + ': ' + os.environ[name])
    else:
        print(name + ' not set')


def print_diagnostic_info():
    print_environment_variable('AIP_MODEL_DIR')
    print_environment_variable('AIP_CHECKPOINT_DIR')
    print_environment_variable('AIP_TENSORBOARD_LOG_DIR')
    print('Tensorflow version: ' + tf.__version__)
    print(
        'Tensorflow built with GPU support: '
        + str(tf.test.is_built_with_gpu_support()))
    print(
        'Tensorflow built with CUDA support: '
        + str(tf.test.is_built_with_cuda()))
    print('GPUs available:')
    print(str(tf.config.list_physical_devices('GPU')))


@contextmanager
def with_vertex_cloud_output_logging(pause_for_logs_output = True):
    logging.basicConfig()
    # Print statements on Google cloud output as level INFO
    logging.getLogger().setLevel(logging.INFO)
    yield
    print('Finished, flushing print buffer and logs. Goodbye.', flush=True)
    for __ in range(5):
        print('', flush=True)
    for logger in [
            logging.debug, logging.info, logging.warning, logging.error,
            logging.critical]:
        logger('Flushing logs.')
        for __ in range(5):
            logger('')
    logging.shutdown()


if __name__ == '__main__':
    with with_vertex_cloud_output_logging():
        print_diagnostic_info()
        print('Python version')
        print(sys.version)

