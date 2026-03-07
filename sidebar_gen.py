import os

def generate_sidebar():
    sidebar_content = "* [🏠 Accueil](README.md)\n"
    # Dossiers à ignorer
    ignore_list = ['.github', '.git', 'node_modules', '_']
    
    # 1. Traiter les fichiers à la racine (Priorité au Règlement)
    root_files = [f for f in os.listdir('.') if f.endswith('.md') and f not in ['README.md', '_sidebar.md']]
    if 'reglement.md' in root_files:
        sidebar_content += "* [📜 Règlement](reglement.md)\n"
        root_files.remove('reglement.md')
    
    for file in sorted(root_files):
        title = file.replace('.md', '').replace('-', ' ').title()
        sidebar_content += f"* [{title}]({file})\n"

    # 2. Parcourir les dossiers (Discord, Minecraft, etc.)
    for root, dirs, files in sorted(os.walk('.')):
        # Filtrer les dossiers à ignorer
        dirs[:] = [d for d in dirs if d not in ignore_list and not d.startswith('.')]
        
        folder_name = os.path.basename(root)
        if folder_name == '' or folder_name == '.':
            continue

        # Titre de la section (Dossier)
        section_title = folder_name.replace('-', ' ').upper()
        sidebar_content += f"\n**{section_title}**\n"
        
        for file in sorted(files):
            if file.endswith('.md') and file != 'README.md':
                file_path = os.path.join(root, file).replace('\\', '/')
                title = file.replace('.md', '').replace('-', ' ').title()
                sidebar_content += f"  * [{title}]({file_path})\n"

    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        f.write(sidebar_content)

if __name__ == "__main__":
    generate_sidebar()
