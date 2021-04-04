from functools import wraps
import time


def timer(func):
    """helper function to estimate view execution time"""

    @wraps(func)  # used for copying func metadata
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)
        
        duration = (time.time() - start) * 1000
        print(f'Method {func.__name__} takes {duration:.2f} ms')
        return result
    return wrapper