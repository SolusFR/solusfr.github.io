const fs = require('fs');
const path = require('path');

const docsDir = './docs'; // Dossier contenant vos fichiers .md
const sidebarFile = './_sidebar.md';

function generateSidebar(dir, indent = '') {
    let content = '';
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            content += `${indent}* **${file.toUpperCase()}**\n`;
            content += generateSidebar(filePath, indent + '  ');
        } else if (file.endsWith('.md') && file !== '_sidebar.md') {
            const name = file.replace('.md', '');
            content += `${indent}* [${name}](${filePath.replace(/\\/g, '/')})\n`;
        }
    });
    return content;
}

const sidebarContent = `* [Accueil](README.md)\n\n` + generateSidebar(docsDir);
fs.writeFileSync(sidebarFile, sidebarContent);
console.log('✅ _sidebar.md généré avec succès !');

