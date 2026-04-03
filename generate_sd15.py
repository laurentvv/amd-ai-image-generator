# AI Image Generator with PyTorch pour AMD sur Windows (DirectML)
# Nécessite: optimum[onnxruntime] et onnxruntime-directml

from optimum.onnxruntime import ORTStableDiffusionPipeline
import torch # On garde torch pour le générateur, même si le calcul se fait ailleurs

# Configuration v1.4 (identique à l'original)
model_id = "CompVis/stable-diffusion-v1-4"
prompt = "cyberpunk neon city, rain, wet pavement reflections, Blade Runner style, 8k, cinematic"
negative_prompt = "blurry, low quality, ugly, deformed, bad anatomy"

# --- CHANGEMENT CLÉ ---
# On utilise ORTStableDiffusionPipeline au lieu de StableDiffusionPipeline
# Le provider "DmlExecutionProvider" indique d'utiliser DirectML (et donc le GPU AMD)
print("Chargement du modèle et conversion pour DirectML (peut prendre du temps la première fois)...")
pipe = ORTStableDiffusionPipeline.from_pretrained(
    model_id,
    provider="DmlExecutionProvider",  # 🔥 C'EST LA LIGNE MAGIQUE POUR AMD !
)

# Les optimisations VRAM sont gérées différemment par ONNX Runtime,
# mais le pipeline est déjà assez efficace. On peut essayer si besoin :
# pipe.enable_model_cpu_offload() # Fonctionne différemment, peut ne pas être nécessaire

print("Modèle chargé. Génération de l'image...")

# Génération (le générateur n'est plus lié à un device "cuda")
generator = torch.Generator().manual_seed(42)
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    width=512,
    height=512,
    num_inference_steps=50,
    guidance_scale=7.5,
    generator=generator,
).images[0]

# Sauvegarde
output_path = "output_amd_directml.png"
image.save(output_path)
print(f"✅ Image générée avec succès : {output_path}")