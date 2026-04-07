<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Générateur de Webhook - Règlement</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #313338;
            color: #dbdee1;
            padding: 20px;
            display: flex;
            justify-content: center;
        }
        .container {
            background-color: #2b2d31;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            max-width: 500px;
            width: 100%;
        }
        h2 { color: #f2f3f5; margin-top: 0; text-align: center; }
        label { display: block; margin-top: 15px; font-size: 14px; font-weight: bold; color: #b5bac1; }
        input {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            background-color: #1e1f22;
            border: 1px solid #1e1f22;
            color: #dbdee1;
            border-radius: 4px;
            box-sizing: border-box;
            outline: none;
        }
        input:focus { border-color: #5865F2; }
        button {
            width: 100%;
            background-color: #5865F2;
            color: white;
            border: none;
            padding: 12px;
            margin-top: 25px;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.2s;
        }
        button:hover { background-color: #4752C4; }
        #status { text-align: center; margin-top: 15px; font-weight: bold; }
        .success { color: #57F287; }
        .error { color: #ED4245; }
    </style>
</head>
<body>

<div class="container">
    <h2>📡 Envoi du Règlement</h2>
    
    <label for="webhookUrl">URL du Webhook Discord *</label>
    <input type="url" id="webhookUrl" placeholder="https://discord.com/api/webhooks/..." required>

    <label for="serverName">Nom du Serveur</label>
    <input type="text" id="serverName" placeholder="Ex: MonSuperServeur (remplacera %server_name%)">

    <label for="avatarUrl">URL de l'icône (Avatar)</label>
    <input type="url" id="avatarUrl" placeholder="https://lien-vers-image.png">

    <button onclick="sendWebhook()">Envoyer le règlement sur Discord</button>
    <p id="status"></p>
</div>

<script>
    const payloadBase = {
        "content": null,
        "embeds": [
            {
                "title": "⚖️ Partie 6 : Sanctions & Procédures (1/2)",
                "description": "**Article A : Types de Sanctions**\n- Avertissement oral ou écrit\n- Suppression de message\n- Mute temporaire (texte ou vocal)\n- Déconnexion forcée d’un salon vocal\n- Restriction temporaire de salons\n- Kick du serveur\n- Ban temporaire ou permanent\n- Selon gravité, sanction directe possible sans avertissement\n\n**Article B : Récidive & Aggravation**\n- Récidive → sanctions plus lourdes\n- Comportement provocateur ou toxique → aggravation immédiate\n- Contournement de sanction (multi-comptes, VPN, salons abusifs) → ban permanent",
                "color": 14425151
            },
            {
                "title": "⚖️ Partie 6 : Sanctions & Procédures (2/2)",
                "description": "**Article C : Respect des décisions du Staff**\n- Décisions du staff respectées\n- Pas de pression, menace ou tentative d’influencer\n- Insulte ou manque de respect = faute grave\n- Refus de coopérer en ticket ou vocal → sanction\n\n**Article D : Contestation d’une sanction**\n- Contestation possible uniquement en ticket privé\n- Demande agressive, mensongère ou provocante → fermeture immédiate\n- Décision finale = staff\n\n**Article E : Multi-comptes & Contournements**\n- Multi-comptes pour troll, contournement ou espionnage → ban\n- Nouveau compte pendant un ban → sanction définitive",
                "color": 14425151
            },
            {
                "title": "⚠️ Partie 6 : Infractions majeures",
                "description": "- Contenu NSFW, pornographique, gore ou +18 → ban direct\n- Harcèlement, menaces, intimidation → ban direct\n- Racisme, homophobie, xénophobie, sexisme → ban direct\n- Escroquerie, phishing, arnaques, malware → ban direct\n- Diffusion d’informations personnelles (doxxing) → ban direct\n- Raid ou tentative de raid → ban direct",
                "color": 14425151
            },
            {
                "title": "🛡️ Partie 6 : Pouvoirs de l’Équipe Staff",
                "description": "- Modifier ou supprimer tout message jugé inapproprié\n- Intervenir en vocal à tout moment\n- Appliquer des sanctions même si la règle n’est pas écrite\n- Protéger les membres si situation toxique/dangereuse\n- Prendre des décisions rapides pour préserver la sécurité du serveur\n- Modération au cas par cas pour un environnement sain",
                "color": 14425151
            },
            {
                "title": "🤝 Partie 7 : Partenariats, Contenus Externes & Vie Privée",
                "description": "**Article A : Partenariats**\n- Ouvrir un ticket pour toute demande de partenariat\n- Fournir toutes les infos nécessaires (serveur, projet, lien, objectifs)\n- Pas de pub ou liens hors ticket validé\n- Partenariats officiels annoncés par staff après validation\n\n**Article B : Contenus externes**\n- Liens fiables et sûrs\n- Interdit : virus, malware, cracks, NSFW, gore, contenus illégaux\n- Médias respectent règles des messages et salons textuels\n\n**Article C : Vie privée**\n- Pas de partage d’informations personnelles en public ou privé\n- Ne pas demander d’infos personnelles aux autres\n- Partage sans consentement sanctionnable et signalable aux autorités si nécessaire",
                "color": 14425151
            },
            {
                "title": "📌 Partie 7 : Contenus liés au serveur et conseils",
                "description": "**Article D : Conseils pour sécurité et respect**\n- Vérifier la provenance des liens ou fichiers avant de partager\n- Signaler au staff tout comportement suspect ou dangereux\n- Respecter la vie privée et la sécurité des autres membres",
                "color": 14425151
            },
            {
                "title": "📝 Note finale & Pouvoirs du staff",
                "description": "📌 Le règlement est considéré comme lu et approuvé par tous les membres.\n\n💡 Pour plus de détails ou mises à jour, consultez : [Règlement complet en ligne](https://solus.lifestealmc.fr/#/docs/Discord/Reglement)\n\n⚠️ Pouvoirs & Autorité du Staff\n- Convocations en vocal pour éclaircir une situation, refus → sanction\n- Staff peut supprimer, censurer ou modifier tout message non conforme\n- Déplacements, mute, deaf dans les salons vocaux si situation l’exige\n- Changement de pseudo si inapproprié\n- Tentative de raid Discord = ban définitif\n- Décisions du staff non négociables\n- Contestation de sanction uniquement en privé, jamais publiquement\n- Le staff peut enregistrer toute conversation vocale, partage d’écran ou autre média, avec ou sans raison.\n\n\nMerci de respecter ces règles pour garder notre communauté sécurisée et agréable !",
                "color": 14425151
            }
        ],
        "username": "Règlement de %server_name%",
        "attachments": []
    };

    async function sendWebhook() {
        const webhookUrl = document.getElementById('webhookUrl').value.trim();
        let serverName = document.getElementById('serverName').value.trim();
        const avatarUrl = document.getElementById('avatarUrl').value.trim();
        const statusEl = document.getElementById('status');

        if (!webhookUrl) {
            statusEl.textContent = "Veuillez entrer une URL de Webhook valide.";
            statusEl.className = "error";
            return;
        }

        if (!serverName) serverName = "Serveur Inconnu"; // Valeur par défaut

        // Copie profonde du payload pour ne pas modifier l'original
        const payload = JSON.parse(JSON.stringify(payloadBase));

        // Remplacement du nom
        payload.username = payload.username.replace("%server_name%", serverName);

        // Ajout de l'avatar si renseigné
        if (avatarUrl) {
            payload.avatar_url = avatarUrl;
        }

        statusEl.textContent = "Envoi en cours...";
        statusEl.className = "";

        try {
            const response = await fetch(webhookUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (response.ok) {
                statusEl.textContent = "✅ Règlement envoyé avec succès !";
                statusEl.className = "success";
            } else {
                statusEl.textContent = "❌ Erreur lors de l'envoi (Statut: " + response.status + ")";
                statusEl.className = "error";
            }
        } catch (error) {
            statusEl.textContent = "❌ Erreur réseau. Vérifiez l'URL.";
            statusEl.className = "error";
        }
    }
</script>

</body>
</html>
