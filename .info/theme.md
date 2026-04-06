Voici un guide étape par étape pour utiliser le système de **Thèmes par Dossier** que nous avons configuré dans ton `index.html`.

---

# 🎨 Guide : Ajouter un Thème Personnalisé à un Dossier

Grâce au "Moteur d'Injection" présent dans ton fichier principal, tu peux changer l'apparence complète du wiki (couleurs, fond, animations) simplement en changeant de dossier.

### Étape 1 : Créer l'arborescence
Choisis le dossier que tu veux styliser. Par exemple, si tu veux un thème spécial pour tes documents "Légal", crée la structure suivante :

```text
/docs/
  index.html
  _sidebar.md
  /legal/
    ├── theme.html      <-- C'est ici que la magie opère
    ├── reglement.md
    └── conditions.md
```

### Étape 2 : Créer le fichier `theme.html`
Dans ce dossier, crée un fichier nommé exactement **`theme.html`**. 
*Docsify le cherchera automatiquement dès que tu cliqueras sur un lien situé dans ce dossier.*

### Étape 3 : Structure du fichier `theme.html`
Le fichier doit contenir deux parties :
1.  **`<style>`** : Pour changer les couleurs et cacher les éléments du thème par défaut.
2.  **`HTML`** : Pour ajouter des éléments visuels (particules, grilles, overlays).

Voici le squelette à copier-coller :

```html
<style>
  :root {
    /* 1. Change les couleurs principales ici */
    --bg-color: #000000;
    --text-color: #ffffff;
    --accent-color: #00ff00; /* Vert par exemple */
    --heading-color: #00ff00;
  }

  /* 2. Supprimer les bulles rouges du thème par défaut */
  .animated-background::before, 
  .animated-background::after {
    display: none !important;
  }

  /* 3. Ajouter ton propre fond à la place */
  .animated-background {
    background-color: var(--bg-color) !important;
    background-image: radial-gradient(#111 10%, transparent 10%);
    background-size: 20px 20px;
  }
</style>

<!-- 4. Ajouter des éléments HTML si besoin (facultatif) -->
<div class="mon-effet-special"></div>
```

### Étape 4 : Les variables importantes à modifier
Pour que ton thème soit cohérent, modifie ces variables dans ton bloc `<style>` :

| Variable | Utilité |
| :--- | :--- |
| `--bg-color` | La couleur de fond de la page. |
| `--accent-color` | La couleur des liens, des boutons et de la barre de scroll. |
| `--heading-color` | La couleur des titres (H1, H2, H3). |
| `--nav-hover-bg` | La couleur de survol dans la barre latérale. |

### Étape 5 : Comment "nettoyer" le thème précédent ?
Comme ton `index.html` possède des animations de fond (les cercles rouges flous), il est **crucial** de les désactiver dans ton `theme.html` pour qu'ils ne se mélangent pas à ton nouveau design.

Utilise toujours ce code dans ton `theme.html` :
```css
.animated-background::before, 
.animated-background::after {
  display: none !important; /* Tue les cercles rouges */
}
```

---

### 💡 Astuces Avancées

*   **Héritage :** Si tu crées un `theme.html` dans le dossier `/boutique/`, tous les sous-dossiers comme `/boutique/items/` et `/boutique/grades/` utiliseront aussi ce thème, sauf si tu recrées un autre `theme.html` spécifique dans l'un d'eux.
*   **Images de fond :** Tu peux utiliser une image au lieu d'une couleur :
    ```css
    .animated-background {
      background: url('branding/mon-image.jpg') center/cover no-repeat !important;
    }
    ```
*   **Tester rapidement :** Pas besoin de redémarrer Docsify. Modifie le `theme.html`, sauvegarde, et rafraîchis ta page sur le navigateur.
