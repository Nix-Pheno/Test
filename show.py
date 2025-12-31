import os

present = os.path.join(os.path.join(os.environ['USERPROFILE'],'DESKTOP'))

print(present)

i = 1

for i in range(200):
    new = 'Muhehehehe'+ str(i)
    f_path = os.path.join(present, new)
    os.mkdir(f_path)
    
    i += 1
