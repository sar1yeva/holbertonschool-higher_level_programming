#!/usr/bin/python3
import marshal
def find_names(code):
    names = set(code.co_names)
    for const in code.co_consts:
        if isinstance(const, type(code)):
            names.update(find_names(const))
    return names

if __name__ == "__main__":
    filename = "/tmp/hidden_4.pyc"

    with open(filename, "rb") as f:
        f.read(16)  # header-i keç
        code = marshal.load(f)

    all_names = find_names(code)
    
    for name in sorted(all_names):
        if not name.startswith("__"):
            print(name)
