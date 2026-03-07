import os
from pathlib import Path

def generate_sidebar():
    sidebar_content = []
    # On définit l'ordre des dossiers racines
    base_folders = ['staff', 'player']
    
    for folder in base_folders:
        folder_path = Path(folder)
        if not folder_path.exists():
            continue
            
        sidebar_content.append(f"* **{folder.upper()}**")
        
        # On parcourt de manière récursive
        for root, dirs, files in os.walk(folder):
            files.sort()
            # Calcul de l'indentation basé sur la profondeur relative
            rel_path = Path(root).relative_to(Path(folder).parent)
            depth = len(rel_path.parts) - 1
            indent = "  " * depth

            # Si on est dans un sous-dossier (pas à la racine du dossier staff/player)
            if root != folder:
                folder_name = Path(root).name.replace('-', ' ').title()
                sidebar_content.append(f"{indent}* **{folder_name}**")
                indent += "  "

            for file in files:
                if file.endswith('.md') and file not in ['_sidebar.md', 'README.md']:
                    full_path = Path(root) / file
                    # Formatage du nom : supprime .md, remplace tirets par espaces
                    display_name = file[:-3].replace('-', ' ').title()
                    if display_name.lower() == 'readme':
                        display_name = "Introduction"
                    
                    # Transformation du chemin en format URL (slashs)
                    url_path = str(full_path).replace('\\', '/')
                    sidebar_content.append(f"{indent}  * [{display_name}]({url_path})")

    # Écriture finale
    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sidebar_content))

if __name__ == "__main__":
    generate_sidebar()
