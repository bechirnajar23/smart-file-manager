from pathlib import Path
def scan_directory(source):
    """verify if a path exists or no ,
    explore recursively directories (even sub directories...) , 
    filter files and collect files from these directories"""
    parent_dir=Path(source)
    #verify if a path exists or no
    if (parent_dir.exists() and parent_dir.is_dir()):
        files_list=[]
        #explore recursively directories
        #rglob("*") signify "recursive glob"
        for item in parent_dir.rglob("*"):
            #filter keep only files
            if item.is_file():
                files_list.append(item)
        return files_list
    else:
        print("Directory Not found")
        return None

if __name__=="__main__":
    path=input("entre path to your directory : ").strip()
    files=scan_directory(path)
    print(files)
    print(f"\nNumber of files in '{path}' is {len(files)}")

