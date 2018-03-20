import os
path=os.path.abspath('..')
for prefix,dirs,files in os.walk(path):
    print(f'{prefix}|-|{dirs}|-|{files}')
    for name in files:
        if name.endswith(".pyc"):
            filename=os.path.join(prefix,name)
            os.remove(filename)
