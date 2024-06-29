#!/usr/bin/python3
import this as t
doc_file = str(t.__doc__).strip()
print(f"{doc_file[:-4]}")
