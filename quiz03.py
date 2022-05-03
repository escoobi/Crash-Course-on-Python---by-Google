filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
"""_Trabalhando com List e List Compression_
    Substitui as extensões .hpp por .h
"""
for w, x in enumerate(filenames):
    if x.endswith(".hpp"):
        filenames[w] = x.replace(".hpp", ".h")

print(filenames)             
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]