import os
from pathlib import Path

def generate_sidebar():
    base_folders = ['staff', 'player']
    lines = []

    for folder in base_folders:
        if not os.path.exists(folder):
            continue
            
        # Dossier principal (ex: STAFF)
        lines.append(f"* **{folder.upper()}**")
        
        # On scanne récursivement
        for root, dirs, files in os.walk(folder):
            # Trier pour garder un ordre alphabétique
            dirs.sort()
            files.sort()
            
            # Calculer l'indentation relative au dossier racine
            rel_path = os.path.relpath(root, folder)
            if rel_path == ".":
                depth = 1
            else:
                depth = rel_path.count(os.sep) + 2
            
            indent = "  " * (depth - 1)

            # Afficher le nom du dossier actuel comme une catégorie si ce n'est pas la racine
            if rel_path != ".":
                folder_name = os.path.basename(root).replace('-', ' ').title()
                lines.append(f"{indent}* **{folder_name}**")
                indent += "  "

            # Ajouter les fichiers .md
            for file in files:
                if file.endswith('.md') and file not in ['_sidebar.md', 'README.md']:
                    name = file[:-3].replace('-', ' ').title()
                    # Si c'est un fichier d'intro dans un sous-dossier
                    if name.lower() == 'index' or name.lower() == 'intro':
                        name = "Introduction"
                    
                    full_path = os.path.join(root, file).replace('\\', '/')
                    lines.append(f"{indent}* [{name}]({full_path})")

    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print("✅ _sidebar.md généré pour docsify-sidebar-collapse.")

if __name__ == "__main__":
    generate_sidebar()
