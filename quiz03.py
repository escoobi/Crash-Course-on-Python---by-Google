filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
for w, x in enumerate(filenames):
    if x.endswith(".hpp"):
        filenames[w] = x.replace(".hpp", ".h")

print(filenames)             
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]