from pathlib import Path
import shutil
extension={
    "document":[".pdf",".docx",".txt",".doc"],
    "image":[".jpeg",".png",".jpg",".avif",".gif",".webp",".svg",".bmp",".ico"],
    "video":[".mp4",".mov",".mkv",".avi",".wmv"],
    "audio":[".mp3",".wave",".wav",".ogg",".m4a",".flac"],
    "archive":[".zip",".7z",".rar",".tar.gz",".tar",".tar.xz",".gz",".xz"],
    "script":[".py",".js",".html",".css",".php",".json"],
    "package":[".pkg",".deb",".rpm"]
}

def org_files(source_files,target_dir):
    """organize files in directories according to their extensions 
    and create directories if they don't exist"""
    base_dir=Path(target_dir)
    for item in source_files:
        #get files extension
        extension_item=item.suffix.lower()
        category="other"#default category
        #loop for getting category
        #exts:list of extensions
        #key:category
        for key, exts in extension.items():
            if extension_item in exts:
                category=key
                break
        #define target directory
        dest_dir=base_dir/category
        #create directory if it doesn't exist and parents exist
        dest_dir.mkdir(parents=True,exist_ok=True)
        #define final path of file
        dest_path=dest_dir/item.name
        #if a file with the same name already exists in the directory
        if dest_path.exists():
            counter=1
            while dest_path.exists():#loop until file doesn't exist
                new_name=f"{item.stem}_{counter}{item.suffix}"#create new name
                #define final path
                dest_path=dest_dir/new_name
                counter+=1

        try:
            #move file to directory
            shutil.move(item,dest_path)
            print(f"'{item.name}' moved to {category}")
        except Exception as e:
                print(f"Error for '{item.name}' : {e}")
if __name__ == "__main__":
    from Scanner import scan_directory
    
    chemin = input("Entrez le chemin du dossier à organiser : ").strip()
    
    #
    fichiers = scan_directory(chemin)
    
    if fichiers:
        confirmation = input("\nVoulez-vous lancer le classement ? (o/n) : ").strip().lower()
        if confirmation == 'o':
            # Étape 2 : On organise
            org_files(fichiers, chemin)
            print("\n🎉 Classement terminé avec succès !")
        else:
            print("Opération annulée.")