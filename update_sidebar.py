import os

def generate_sidebar(startpath):
    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        # On écrit d'abord le lien vers l'accueil
        f.write('* [Accueil](/)\n')
        
        for root, dirs, files in os.walk(startpath):
            # On ignore les dossiers cachés (.git, etc) et le dossier docsify
            dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]
            
            level = root.replace(startpath, '').count(os.sep)
            indent = '  ' * level
            
            # Titre du dossier (sauf pour la racine)
            if root != startpath:
                folder_name = os.path.basename(root).replace('-', ' ').title()
                f.write(f'{indent}* **{folder_name}**\n')
            
            subindent = '  ' * (level + 1)
            for file in files:
                if file.endswith('.md') and file != '_sidebar.md' and file != '_navbar.md' and file != 'README.md':
                    # Nom joli pour le fichier
                    name = os.path.splitext(file)[0].replace('-', ' ').title()
                    # Chemin relatif
                    path = os.path.join(root, file).replace('\\', '/')
                    path = path.replace(startpath + '/', '')
                    
                    f.write(f'{subindent}* [{name}]({path})\n')

    print("✅ _sidebar.md a été mis à jour avec succès !")
    print("✨ N'oublie pas de rafraîchir ta page web.")

# Lancer le script dans le dossier actuel
if __name__ == "__main__":
    generate_sidebar('.')
