import os
sd=input("shutdown computer?(yes/no):")
if sd =='no':
    exit()
else:
    os.system("shutdown /s /t 1")