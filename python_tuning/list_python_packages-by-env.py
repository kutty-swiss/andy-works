import subprocess
import os

# Define the virtual environments and their corresponding requirements.txt files
venvs = [
    {
        "env": "/home/andy/Easy-Diffusion-Linux/easy-diffusion/installer_files/env/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/easy-diffusion_requirements.txt"
    },
    {
        "env": "/home/andy/ComfyUI/venv/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/comfyui_requirements.txt"
    },
    {
        "env": "/home/andy/stable-diffusion-webui/Automatic1111_env/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/Automatic1111_requirements.txt"
    },
    {
        "env": "/home/andy/stable-diffusion-webui-forge/venv/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/forge_requirements.txt"
    },
    {
        "env": "/home/andy/stable-diffusion-reforge/venv/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/reforge_requirements.txt"
    },
    {
        "env": "/snap/openvino-ai-plugins-gimp/current/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/openvino_gimp_requirements.txt"
    },
    {
        "env": "/home/andy/openvino_env/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/openvino_requirements.txt"
    },
    {
        "env": "/home/andy/llm-cpp/bin/activate",
        "requirements": "/home/andy/Github-Workspaces/andy-works/python_tuning/ipexllm_requirements.txt"
    }
]

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(
        ['bash', '-c', command],  # Ensure bash is used for the command
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout

def get_installed_packages(venv_path):
    """Get installed packages in the virtual environment."""
    # Use bash to run the source command and pip list
    command = f"source {venv_path} && pip list --format=freeze"
    installed_packages = run_command(command)
    return set(installed_packages.splitlines())

def read_requirements(requirements_file):
    """Read the requirements from the requirements.txt file."""
    with open(requirements_file, 'r') as f:
        return set(f.read().splitlines())

def compare_and_generate_requirements():
    all_installed_packages = {}  # To store installed packages for all venvs
    all_requirements = {}  # To store requirements for all venvs

    # Step 1: Get installed packages for each venv
    for venv in venvs:
        venv_name = os.path.basename(venv["env"])
        installed = get_installed_packages(venv["env"])
        all_installed_packages[venv_name] = installed

        # Get the packages required from the requirements.txt
        required = read_requirements(venv["requirements"])
        all_requirements[venv_name] = required

    # Step 2: Combine all unique requirements across venvs
    all_unique_requirements = set()

    for venv_name, installed in all_installed_packages.items():
        required = all_requirements[venv_name]
        all_unique_requirements.update(installed)

    # Step 3: Remove common packages across all environments (if any)
    common_packages = set.intersection(*all_installed_packages.values()) if len(all_installed_packages) > 1 else set()
    all_unique_requirements -= common_packages

    # Step 4: Generate the final `requirements.txt` for non-conflicting, combined packages
    with open("combined_requirements.txt", "w") as f:
        for package in sorted(all_unique_requirements):
            f.write(package + "\n")

    print("Combined requirements have been written to 'combined_requirements.txt'.")
    print("You can install them system-wide using: pip install -r combined_requirements.txt")

if __name__ == "__main__":
    compare_and_generate_requirements()
