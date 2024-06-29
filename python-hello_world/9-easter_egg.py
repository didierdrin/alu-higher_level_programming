#!/usr/bin/python3
import this as t
doc_file = str(t.__doc__)
cleaned_txt = doc_file.replace("\n", "")
print(f"{cleaned_txt[:-4]}")
