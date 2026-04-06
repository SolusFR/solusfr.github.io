import os

def generate_sidebar():
    base_folder = 'docs'
    if not os.path.exists(base_folder):
        print(f"Le dossier '{base_folder}' n'existe pas.")
        return

    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        # On parcourt le contenu de 'docs' sans écrire le nom du dossier parent
        for root, dirs, files in os.walk(base_folder):
            files.sort()
            dirs.sort() # Trier aussi les dossiers
            
            # Calcul de la profondeur par rapport au dossier 'docs'
            # Si root == 'docs', rel_path est '.', donc la profondeur est 0
            rel_path = os.path.relpath(root, base_folder)
            if rel_path == '.':
                depth = 0
            else:
                depth = rel_path.count(os.sep) + 1
            
            indent = '  ' * depth
            
            # Si on n'est pas à la racine de 'docs', on écrit le nom du sous-dossier
            if root != base_folder:
                folder_name = os.path.basename(root).replace('-', ' ').title()
                f.write(f'{indent}* **{folder_name}**\n')
                indent += '  ' # On indente les fichiers à l'intérieur de ce dossier

            # Ajout des fichiers
            for file in files:
                # On ignore _sidebar.md et éventuellement les README de la racine si nécessaire
                if file.endswith('.md') and file != '_sidebar.md':
                    path = os.path.join(root, file).replace('\\', '/')
                    
                    # Nettoyage du nom du fichier pour l'affichage
                    name = file.replace('.md', '').replace('-', ' ').title()
                    if name.lower() == 'readme': 
                        name = "Introduction"
                        
                    f.write(f'{indent}* [{name}]({path})\n')

if __name__ == "__main__":
    generate_sidebar()
    print("Sidebar générée avec succès !")
