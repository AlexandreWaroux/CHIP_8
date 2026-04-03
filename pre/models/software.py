class Software:
    @staticmethod
    def create(path, data:str):
        with open(file=path, mode="+wb") as fp:
            bynary_data = bytes.fromhex(data)
            fp.write(bynary_data)

