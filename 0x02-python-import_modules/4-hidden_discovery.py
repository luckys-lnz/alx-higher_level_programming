#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names_defined by hidden_4 module."""
    import hidden_4

    names_defined = dir(hidden_4)
    for i in names_defined:
        if i[:2] != "__":
            print(i)
