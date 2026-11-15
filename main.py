import json
from pathlib import Path
from Organizer import org_files
from Scanner import scan_directory
from reporter import prepare_data,save_report
from duplicate_finder import find_duplicate_files

def main():
    source_input=input("Entre path to your directory : ").strip()

    #1. Scan directory
    files=scan_directory(source_input)

    if not files:
        print("\nNo files found or invalid path. End of program.")
        return
    print(f"\nNumber of files in '{source_input}' is {len(files)}")

    #initialize global report
    global_report={
        "Directory_analyzed":str(Path(source_input).resolve()),
        "Number_of_files":len(files),
        "Actions":{}
    }

    #2. Organize files
    choice_org=input("\nDo you want to organise files with their extensions ? (o/n) : ").strip().lower()
    if choice_org=='o':
        org_files(files,source_input)
        global_report["Actions"]["Organize_files_with_extensions"]=True
    else:
        global_report["Actions"]["Organize_files_with_extensions"]=False

    #3. duplicate files
    choice_dup=input("\nDo you want to find duplicate files ? (o/n) : ").strip().lower()
    if choice_dup=='o':
        actual_files=scan_directory(source_input)
        duplicate_dict=find_duplicate_files(actual_files)
        if duplicate_dict:
            print(f"\nNumber of duplicate files is {len(duplicate_dict)}")
            clean_dup_dict=prepare_data(duplicate_dict)
            global_report["Duplicate_files"]=clean_dup_dict
        else:
            print("\nNo duplicate files found.")
            global_report["Duplicate_files"]={}
        global_report["Actions"]["Find_duplicate_files"]="Done"
    else:
        global_report["Actions"]["Find_duplicate_files"]="Ignored"

    #4. Save report
    save_report(global_report,filename="smart_file_manager.json")

if __name__=="__main__":
    main()