#!/usr/bin/python3
import dis
import marshal
if __name__ == "__main__":
    filename = "/tmp/hidden_4.pyc"
    with open(filename, "rb") as f:
        f.read(16) 
        code = marshal.load(f)
    names = set()
    for const in code.co_consts:
        if isinstance(const, type(code)):
            names.update(const.co_names)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
