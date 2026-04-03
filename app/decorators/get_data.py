from functools import wraps
def get_data(fc):
    @wraps(fc)
    def _(*args,**kwargs):
        path = kwargs.get('path')
        try:
            with open(file=path, mode="rb")as fp:
                rom = fp.read()
                kwargs['rom']=rom
                return fc(*args,**kwargs)
        except Exception as e:
            print(f"\33[31;1m Failed to read {path}\033[0m")
            print(e)
            exit(1)
    return _