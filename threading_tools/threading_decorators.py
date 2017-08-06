import threading
import multiprocessing


def threaded_fn(func):
    """
    A decorator for any function that needs to be run on a separate thread
    """
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


def process_fn(func):
    """
    A decorator for any function that needs to be run on a separate process
    """
    def wrapper(*args, **kwargs):
        process = multiprocessing.Process(target=func, args=args, kwargs=kwargs)
        process.start()
        return process
    return wrapper
