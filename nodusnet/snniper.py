# snniper.py
def Attr(cls):
    model= cls.__name__
    return cls.__doc__.replace(model,"").replace("(","").replace(")","").replace(" ","").split(",")

def get_filename(filename):
    return filename.upper()