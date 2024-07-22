from stable_diffusion_pytorch import pipeline

prompts = ["a cat playing computer game"]
images = pipeline.generate(prompts)
images[0].save('output.jpg')