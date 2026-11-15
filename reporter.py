import json
from pathlib import Path

def prepare_data(duplicate_dict):
    """convert objects path of duplicate dictionary to string
    to be accepted by json"""
    clean_report={}
    for file_hash,paths_list in duplicate_dict.items():
        clean_paths=[str(p) for p in paths_list]
        clean_report[file_hash]=clean_paths
    return clean_report

def save_report(report,filename="report_file_manager.json"):
    """take a dictionary clean and save it in a json file"""
    try:
        with open(filename,"w",encoding="utf-8") as f:
            #json.dump convert dictionary to json to be written in json file
            #indent=4 to format json in human readable way
            #ensure_ascii=False to write non ascii characters
            json.dump(report,f,indent=4,ensure_ascii=False)
            print(f"Report saved in {filename}")
    except Exception as e:
        print(f"Error while saving the report {filename}: {e}")
if __name__ == "__main__":
    # Simulation d'un faux dictionnaire avec des objets Path
    fake_duplicates = {
        "d41d8cd98f...": [Path("C:/test/image1.png"), Path("C:/test/copie/image1.png")]
    }
    
    print("Avant conversion (objets Path) :")
    print(fake_duplicates)
    
    report_ready = prepare_data(fake_duplicates)
    
    print("\nAprès conversion (chaînes de caractères) :")
    print(report_ready)

    # Simulation de données de rapport globales
    donnees_test = {
        "statistiques": {
            "total_fichiers_scannes": 10,
            "doublons_detectes": 1
        },
        "doublons_details": report_ready # On intègre nos doublons convertis
    }
    
    print("\nSauvegarde du rapport en cours...")
    save_report(donnees_test)