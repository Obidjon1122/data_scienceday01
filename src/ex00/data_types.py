def data_types():
    a=1
    b="salom"
    c=3.00
    d=True
    f=[]
    g={}
    h=()
    i={"apple"}

    print("["
          +type(a).__name__+", "
          +type(b).__name__+", "
          +type(c).__name__+", "
          +type(d).__name__+", "
          +type(f).__name__+", "
          +type(g).__name__+", "
          +type(h).__name__+", "
          +type(i).__name__+"]")

if __name__ == '__main__':
    data_types()