#

import os

os.chdir(r"C:\Users\user\Downloads")

with open("rosalind_dna.txt") as f:
    a = f.readline()

print(a.count("A"), a.count("C"), a.count("G"), a.count("T"))


### after making folder, move to py file ### 

# file_name = os.listdir(".")
# from shutil import move
# for name in file_name[3:]:
#     a, b, c = name.split(".")
#     os.mkdir(a+b)
    
#     with open("C:/Users/user/Desktop/workspace/rosalind/solution/"+a+b+"/README.md", "w") as f:
#         f.write("plz write the description")
    
#     move("C:/Users/user/Desktop/workspace/rosalind/solution/"+name, "C:/Users/user/Desktop/workspace/rosalind/solution/"+a+b+"/"+name)
    



