import os
os.remove("testing.txt")
with open('testing.txt', 'a') as file:
            file.write("sam\n")
a=1
b=1
c=1
if a==b:
    b=2
    c=3
print(c)
# with open("testing.txt", "r") as f:

#     lines = f.readlines()

# with open("testing.txt", "w") as f:

#     for line in lines:

#         if line.strip("\n") != "b":

#             f.write(line)