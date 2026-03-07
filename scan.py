import os

def generate_sidebar():
    wiki_path = 'wiki'  # Le dossier source
    sidebar_lines = []
    
    if not os.path.exists(wiki_path):
        print(f"❌ Erreur : Le dossier '{wiki_path}' est introuvable à la racine.")
        return

    print(f"📂 Analyse du dossier : {wiki_path}")

    for root, dirs, files in os.walk(wiki_path):
        # Trier pour l'ordre alphabétique
        dirs.sort()
        files.sort()

        # Calcul de la profondeur par rapport au dossier wiki
        rel_path = os.path.relpath(root, wiki_path)
        
        if rel_path == ".":
            depth = 0
        else:
            depth = rel_path.count(os.sep) + 1
            # On ajoute le nom du dossier comme un titre de catégorie
            folder_name = os.path.basename(root).replace('-', ' ').title()
            indent = "  " * (depth - 1)
            sidebar_lines.append(f"{indent}* **{folder_name}**")

        indent = "  " * depth
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                # On ne veut pas afficher README dans le nom, mais "Introduction"
                display_name = file.replace('.md', '').replace('-', ' ').title()
                if display_name.lower() == 'readme':
                    display_name = "Introduction"
                
                # Le chemin doit inclure 'wiki/' pour que Docsify le trouve
                full_path = os.path.join(root, file).replace('\\', '/')
                sidebar_lines.append(f"{indent}  * [{display_name}]({full_path})")

    if not sidebar_lines:
        print("⚠️ Aucun fichier .md trouvé dans le dossier wiki.")
        return

    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sidebar_lines))
    
    print("✅ _sidebar.md généré avec succès à partir du dossier wiki.")

if __name__ == "__main__":
    generate_sidebar()
