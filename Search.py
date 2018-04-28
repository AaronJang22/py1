import os
def recursive_search(path):
    files=os.listdir(path)
    for file in files:
        full_filename = os.path.join(path, file)
        if os.path.isdir(full_filename):
            recursive_search(full_filename)
        else:
            ext = os.path.splitext(full_filename)[1]
            size = os.path.getsize(full_filename)

            #print(fullpath)
            if():
                print(path)
                print(file)
                print(ext)
                print(size)
                print("=======")
            
            
def search(path): # non-recursive
    for (root, dirs, files) in os.walk(path):
        for file in files:
            fullpath = os.path.join(root,file)
            ext = os.path.splitext(fullpath)[1]
            size = os.path.getsize(fullpath)
            
            print(fullpath)
            print(path)
            print(file)
            print(ext)
            print(size)
            print("=======")
            
def main():
    path = os.getcwd()
    #search(path)
    recursive_search(path)

main()
