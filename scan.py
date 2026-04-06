import os

def generate_sidebar():
    docs_folder = 'docs'
    # Le fichier _sidebar.md doit être DANS le dossier docs pour fonctionner
    output_file = os.path.join(docs_folder, '_sidebar.md')
    
    if not os.path.exists(docs_folder):
        print(f"Erreur : Le dossier '{docs_folder}' est introuvable.")
        return

    lines = []

    for root, dirs, files in os.walk(docs_folder):
        # On ignore les dossiers cachés (commençant par .)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        dirs.sort()
        files.sort()

        # Chemin relatif par rapport à 'docs'
        rel_path = os.path.relpath(root, docs_folder)
        
        # Calcul précis de la profondeur
        if rel_path == '.':
            depth = 0
        else:
            depth = rel_path.count(os.sep) + 1

        # 1. Gestion du Titre du dossier (uniquement si on n'est pas à la racine)
        if rel_path != '.':
            folder_name = os.path.basename(root).replace('-', ' ').replace('_', ' ').title()
            # On met le dossier en GRAS, et il n'est PAS un lien
            lines.append(f"{'  ' * (depth - 1)}* **{folder_name}**")

        # 2. Gestion des fichiers .md
        for file in files:
            if file.endswith('.md') and file not in ['_sidebar.md', '_navbar.md']:
                
                # Nom propre pour l'affichage
                display_name = file.replace('.md', '').replace('-', ' ').replace('_', ' ').title()
                if display_name.lower() == 'readme':
                    display_name = "Introduction"

                # Création du lien relatif (ex: "tuto/installation.md")
                # Important : ne doit pas commencer par "docs/"
                link_path = os.path.join(rel_path, file).replace('\\', '/')
                if link_path.startswith('./'):
                    link_path = link_path[2:]

                # On indente le fichier pour qu'il soit bien SOUS le dossier
                lines.append(f"{'  ' * depth}* [{display_name}]({link_path})")

    # Écriture du fichier
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

if __name__ == "__main__":
    generate_sidebar()
    print("✅ Sidebar générée proprement dans docs/_sidebar.md")
