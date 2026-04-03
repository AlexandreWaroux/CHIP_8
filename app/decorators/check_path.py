from functools import wraps
import os
def check_path(fc):
    


    @wraps(fc)
    def _(*args, **kwargs):
        if 'path' in kwargs and not os.path.exists(kwargs.get('path')):
            print(f"\033[31;1m Path {kwargs.get('path')} does not exist \033[0m")
            exit(1)
        return fc(*args, **kwargs)
    return _