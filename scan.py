import os

def generate_sidebar():
    base_folder = 'docs'
    if not os.path.exists(base_folder):
        print(f"Le dossier '{base_folder}' n'existe pas.")
        return

    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(base_folder):
            # Trier pour avoir un ordre alphabétique
            files.sort()
            dirs.sort()
            
            # On calcule le chemin relatif par rapport à 'docs'
            # C'est l'étape CRUCIALE pour que les liens fonctionnent
            rel_root = os.path.relpath(root, base_folder)
            
            if rel_root == '.':
                depth = 0
            else:
                depth = rel_root.count(os.sep) + 1
            
            indent = '  ' * depth
            
            # Si on est dans un sous-dossier, on écrit son nom
            if rel_root != '.':
                folder_name = os.path.basename(root).replace('-', ' ').title()
                f.write(f'{indent}* **{folder_name}**\n')
                indent += '  '

            # Ajout des fichiers
            for file in files:
                if file.endswith('.md') and file != '_sidebar.md':
                    # On crée le chemin relatif au dossier docs
                    # Exemple: au lieu de 'docs/tuto.md', on veut 'tuto.md'
                    full_path = os.path.join(rel_root, file).replace('\\', '/')
                    
                    # Si le fichier est à la racine, relpath peut mettre './'
                    if full_path.startswith('./'):
                        full_path = full_path[2:]

                    # Nom affiché
                    name = file.replace('.md', '').replace('-', ' ').title()
                    if name.lower() == 'readme': 
                        name = "Introduction"
                        
                    f.write(f'{indent}* [{name}]({full_path})\n')

if __name__ == "__main__":
    generate_sidebar()
    print("Sidebar générée sans le préfixe 'docs/' dans les liens.")
