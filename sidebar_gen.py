import os

# Configuration : Dossiers à ignorer
IGNORED_DIRS = {'.git', '.github', 'assets', 'images', 'img', 'node_modules'}
# Fichiers à ignorer (On ignore README.md ici car on le traite manuellement pour l'Accueil)
IGNORED_FILES = {'_sidebar.md', '_navbar.md', 'index.html', 'generate_sidebar.py', '.nojekyll', 'CNAME'}

def get_clean_name(name):
    """Transforme 'guide-anti-phishing.md' en 'Guide Anti Phishing'"""
    name = os.path.splitext(name)[0]
    name = name.replace('-', ' ').replace('_', ' ')
    return name.title()

def get_emoji(name):
    """Ajoute un émoji selon le nom du dossier ou du fichier"""
    name = name.lower()
    if 'discord' in name: return '🌐 '
    if 'minecraft' in name: return '⛏️ '
    if 'reglement' in name: return '📜 '
    if 'securite' in name: return '🛡️ '
    if 'design' in name: return '🎨 '
    if 'utilisateurs' in name or 'ecosysteme' in name: return '🚀 '
    return ''

def generate_markdown(start_path, output_file):
    lines = []
    
    # 1. FORCER L'ACCUEIL EN PREMIER
    lines.append('* [🏠 Accueil](README.md)\n')

    # 2. PARCOURIR LES DOSSIERS
    for root, dirs, files in os.walk(start_path):
        # Filtrage
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in IGNORED_DIRS]
        files = [f for f in files if not f.startswith('.') and f not in IGNORED_FILES and f.lower() != 'readme.md']
        
        # Tri alphabétique
        dirs.sort()
        files.sort()

        # Calcul de la profondeur
        rel_root = os.path.relpath(root, start_path)
        if rel_root == '.':
            depth = 0
        else:
            depth = rel_root.count(os.sep) + 1
        
        indent = '  ' * depth
        
        # Gestion du titre du dossier (Section)
        if root != start_path:
            folder_name = os.path.basename(root)
            clean_folder = get_clean_name(folder_name)
            emoji = get_emoji(folder_name)
            lines.append(f'\n{indent[:-2]}* **{emoji}{clean_folder}**\n')

        # Ajout des fichiers .md
        for file in files:
            if file.endswith('.md'):
                # Priorité au règlement à la racine
                if file == 'reglement.md' and root == start_path:
                    # On l'insère juste après l'accueil
                    lines.insert(1, f'* [📜 Règlement](reglement.md)\n')
                    continue

                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, start_path).replace('\\', '/')
                
                display_name = get_clean_name(file)
                emoji = get_emoji(file)
                
                lines.append(f'{indent}* [{emoji}{display_name}]({rel_path})\n')

    # Écriture du fichier
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__ == "__main__":
    print("🚀 Génération de la sidebar Solus Wiki...")
    generate_markdown('.', '_sidebar.md')
    print("✅ Terminé ! _sidebar.md est prêt.")
