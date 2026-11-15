import hashlib
from pathlib import Path

def get_hash_file(file_path,chunk_size=8192):
    hasher=hashlib.md5()
    #define hasher to calculate md5
    try:
        with open(file_path,"rb") as f:
        #open file in binary mode
            while chunk:=f.read(chunk_size):
                #read file in chunks
                hasher.update(chunk)
                 #update hash object with chunks 
        return hasher.hexdigest(),file_path
        #return hash value in hexadecimal format and file path
    except PermissionError:
        print(f"Access denided to {file_path.name}")
        return None
    except Exception as e:
        print(f"Error with {file_path.name}: {e}")
        return None

def find_duplicate_files(list_of_files):
    seen_duplicates={}
    #dictionary to store duplicate paths
    duplicates={}
    #dictionary to store duplicates
    for file_path in list_of_files:
        #check if file exists
        if not file_path.is_file():
            continue
        result=get_hash_file(file_path)
        #get hash value
        if result is None:
            #verify the value of result
            continue
        file_hash,file_path=result
        #get hash value and file path
        if file_hash in seen_duplicates:
            if file_hash not in duplicates:
                duplicates[file_hash]=[seen_duplicates[file_hash]]
                #initialize duplicates with first seen duplicate
            duplicates[file_hash].append(file_path)
            #add file path to duplicates
        else:
            seen_duplicates[file_hash]=file_path
            #1st seen of hash will be stored
    return duplicates
