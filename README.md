# AI Image Generator for AMD (DirectML)
![Image générée par le script](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/156_stable_diffusion_2/stable-diffusion-2-1-example.png)
*(Image d'exemple d'une génération avec Stable Diffusion 2.1)*

Un projet de scripts Python simples et efficaces pour générer des images avec **Stable Diffusion**, spécifiquement optimisé pour les **GPU AMD sous Windows** grâce à DirectML.

Ce projet permet aux utilisateurs de cartes graphiques AMD de profiter de la génération d'images sans matériel NVIDIA, en proposant des scripts pour différentes versions de Stable Diffusion.

## ✨ Points Forts

*   🚀 **Compatible AMD** : Utilise DirectML pour exploiter votre GPU AMD.
*   🐍 **Simple Python** : Des scripts uniques, faciles à comprendre et à modifier.
*   🎨 **Multi-Modèles** : Inclus des scripts pour **Stable Diffusion 1.5** et **2.1**.
*   💾 **Optimisé pour les faibles VRAM** : Fonctionne sur des cartes avec 6 Go de VRAM ou plus.
*   🖼️ **Facile à Personnaliser** : Modifiez les prompts, la taille, et d'autres paramètres en quelques secondes.

## 🛠️ Prérequis

*   **Windows 10 ou 11**
*   **Python 3.9** ou plus récent
*   **Un GPU AMD** avec les pilotes Adrenalin à jour
*   **Git** (pour cloner le dépôt)

## ⚙️ Installation

Suivez ces étapes pour configurer l'environnement et installer les dépendances.

1.  **Cloner ce dépôt**
    ```bash
    git clone https://github.com/laurentvv/amd-ai-image-generator.git
    cd amd-ai-image-generator
    ```

2.  **Créer un environnement virtuel** (fortement recommandé)
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Installer les dépendances**
    Vous pouvez installer les dépendances manuellement ou utiliser le fichier `requirements.txt` inclus.
    
    *Avec `requirements.txt` (recommandé) :*
    ```bash
    pip install -r requirements.txt
    ```
    
    *Ou manuellement :*
    ```bash
    pip install optimum[onnxruntime] onnxruntime-directml diffusers transformers accelerate
    ```

## 🚀 Utilisation

Choisissez le script correspondant au modèle que vous souhaitez utiliser.

### Génération avec Stable Diffusion 1.5 (Rapide, 512x512)

Idéal pour des générations rapides et des styles artistiques variés.

```bash
python generate_sd15.py
```
*   **Modèle utilisé :** `CompVis/stable-diffusion-v1-4`
*   **Résolution par défaut :** 512x512
*   **Fichier de sortie :** `output_sd15.png`

### Génération avec Stable Diffusion 2.1 (Détaillé, 768x768)

Parfait pour des images plus réalistes et plus détaillées.

```bash
python generate_sd21.py
```
*   **Modèle utilisé :** `RedbeardNZ/stable-diffusion-2-1-base` (miroir communautaire)
*   **Résolution par défaut :** 768x768
*   **Fichier de sortie :** `output_sd21.png`

**Note :** La première exécution de chaque script téléchargera et convertira son modèle respectif. Soyez patient, les prochaines fois seront beaucoup plus rapides.

## 🎛️ Personnalisation

Vous pouvez facilement modifier l'un ou l'autre des scripts pour changer la sortie.

*   `prompt` : La description de l'image que vous voulez générer.
*   `negative_prompt` : Ce que vous voulez éviter dans l'image.
*   `width` & `height` : La résolution (respectez 512x512 pour SD 1.5 et 768x768 pour SD 2.1 pour de meilleurs résultats).
*   `num_inference_steps` : Nombre d'étapes de génération (entre 20 et 50 est un bon point de départ).
*   `guidance_scale` : À quel point le modèle doit suivre le prompt (entre 7 et 10 est courant).

## 💡 Notes sur la Performance

*   Les `TracerWarning` et `[W:onnxruntime:...]` dans la console sont des messages normaux et n'indiquent pas d'erreur.
*   Les messages `Some nodes were not assigned to the preferred execution providers` signifient que le système optimise intelligemment en envoyant les calculs lourds au GPU AMD et les petites tâches au CPU.

## 🤝 Remerciements

Ce projet est rendu possible grâce au travail incroyable de la communauté open-source :

*   **[Hugging Face Diffusers](https://github.com/huggingface/diffusers)**
*   **[Optimum](https://github.com/huggingface/optimum)**
*   **[Stability AI](https://stability.ai/)**
*   **[RedbeardNZ](https://huggingface.co/RedbeardNZ)** (pour le miroir du modèle SD 2.1)
*   **[laurentvv](https://github.com/laurentvv/ai-image-generator-pytorch)** (pour le projet original)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.