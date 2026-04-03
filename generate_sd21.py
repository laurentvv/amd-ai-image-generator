# AI Image Generator with PyTorch pour AMD sur Windows (DirectML)
# Modèle : Stable Diffusion 2.1

from optimum.onnxruntime import ORTStableDiffusionPipeline
import torch

# --- MODÈLE SD 2.1 CORRECT ---
model_id = "RedbeardNZ/stable-diffusion-2-1-base"

prompt = "a majestic lion roaring on a rocky outcrop, savanna sunset, photorealistic, 8k"
negative_prompt = "blurry, low quality, ugly, deformed, bad anatomy, cartoon, painting"

print("Chargement du modèle SD 2.1 et conversion pour DirectML...")
print(f"Vérification du modèle à l'URL : https://huggingface.co/{model_id}")

pipe = ORTStableDiffusionPipeline.from_pretrained(
    model_id,
    provider="DmlExecutionProvider",
)

print("Modèle SD 2.1 chargé. Génération de l'image...")

# Génération
generator = torch.Generator().manual_seed(42)
image = pipe(
    prompt=prompt,
    negative_prompt=negative_prompt,
    width=768,  # Résolution native de SD 2.1
    height=768, # Résolution native de SD 2.1
    num_inference_steps=50,
    guidance_scale=7.5,
    generator=generator,
).images[0]

# Sauvegarde
output_path = "output_amd_sd2-1.png"
image.save(output_path)
print(f"✅ Image SD 2.1 générée avec succès : {output_path}")