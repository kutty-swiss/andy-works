import os
import time
from datetime import datetime
from PIL import Image
import openvino_genai
import random  # For generating random seeds


# Constants
MODEL_PATH = "/home/andy/models/stable-diffusion-v1-5-int8-ov"
DEVICE = 'GPU'  # Use 'GPU' or 'CPU'
WIDTH = 512
HEIGHT = 512
NUM_INFERENCE_STEPS = 15
CFG_SCALE = 7.5  # Classifier-Free Guidance Scale

PROMPT = (
    "a luxury designer building, professional architectural photography, f/12, modern aesthetics, "
    "masterpiece of form and function, intricate detailing, sharp focus, natural lighting, "
    "dark blue sky at dusk, photorealistic, octane render, HDR imaging, ultra-high resolution (8k), high contrast"
)

NEGATIVE_PROMPT = (
    "unrealistic features, cartoon-like appearance, digital art styles, bad proportions, deformed shapes, "
    "low-quality textures, blurry edges, worst quality output"
)


def generate_unique_filename(base_dir="~/Pictures", base_name="openvino_generated_image", seed=None, extension=".bmp"):
    """
    Generate a unique filename by appending the seed to the base name.
    """
    if seed is None:
        raise ValueError("Seed must be provided for generating a unique filename.")
    base_dir = os.path.expanduser(base_dir)
    return os.path.join(base_dir, f"{base_name}_seed_{seed}{extension}")


def log_execution_time(start_time, end_time):
    """
    Log the execution time in both minutes and seconds.
    """
    duration_seconds = end_time - start_time
    duration_minutes = duration_seconds / 60

    print(f"Start Time: {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"End Time: {datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Duration: {duration_seconds:.2f} seconds ({duration_minutes:.2f} minutes)")


def print_input_table(model_path, device, width, height, steps, cfg_scale, prompt, negative_prompt, seed):
    """
    Print input parameters in a table-like format.
    """
    print("\nInput Parameters:")
    print("-" * 80)
    print(f"{'Parameter':<20} | {'Value'}")
    print("-" * 80)
    print(f"{'Model Path':<20} | {model_path}")
    print(f"{'Device':<20} | {device}")
    print(f"{'Width':<20} | {width}")
    print(f"{'Height':<20} | {height}")
    print(f"{'Steps':<20} | {steps}")
    print(f"{'CFG Scale':<20} | {cfg_scale}")
    print(f"{'Prompt':<20} | {prompt}")
    print(f"{'Negative Prompt':<20} | {negative_prompt}")
    print(f"{'Seed':<20} | {seed}")
    print("-" * 80)


def main():
    # Generate a random seed for variability
    seed = random.randint(0, 2**32 - 1)

    # Start timing
    start_time = time.time()
    
    # Print start time before image generation begins
    print(f"Image generation started at: {datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')}")

    # Generate unique output file name using the seed
    output_file = generate_unique_filename(seed=seed)

    # Print input parameters as a table
    print_input_table(
        model_path=MODEL_PATH,
        device=DEVICE,
        width=WIDTH,
        height=HEIGHT,
        steps=NUM_INFERENCE_STEPS,
        cfg_scale=CFG_SCALE,
        prompt=PROMPT,
        negative_prompt=NEGATIVE_PROMPT,
        seed=seed
    )

    # Initialize the pipeline
    pipe = openvino_genai.Text2ImagePipeline(MODEL_PATH, DEVICE)

    # Generate the image with the random seed
    image_tensor = pipe.generate(
        PROMPT,
        negative_prompt=NEGATIVE_PROMPT,
        width=WIDTH,
        height=HEIGHT,
        num_inference_steps=NUM_INFERENCE_STEPS,
        num_images_per_prompt=1,
        seed=seed  # Pass the random seed here
    )

    # Save the generated image
    Image.fromarray(image_tensor.data[0]).save(output_file)
    print(f"Image saved to: {output_file}")

    # End timing and log execution time
    end_time = time.time()
    log_execution_time(start_time, end_time)


if __name__ == "__main__":
    main()
