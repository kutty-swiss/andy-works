
Openvino stable diffusion example from hugging face:
https://huggingface.co/OpenVINO/stable-diffusion-v1-5-fp16-ov


Stable Diffusion Example from intel:
https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/sana-image-generation/sana-image-generation.ipynb


All OpenVino Python examples from Intel(Jupyter)
https://docs.openvino.ai/2025/get-started/learn-openvino/interactive-tutorials-python.html



General Notes:
https://huggingface.co/docs/diffusers/v0.12.0/en/stable_diffusion


https://github.com/intel/AI-PC_Notebooks/blob/main/LLM/01_native_gpu.ipynb



Very important finding:

To compare the package lists between your venv and system-wide Python environments and apply the venv packages to your system-wide Python, follow these steps:

List packages in the venv:
Activate your venv and run:

pip freeze > venv_requirements.txt
List packages in the system-wide Python:
Deactivate the venv and run:

pip freeze > system_requirements.txt
Compare the two files:
You can use a diff tool or simply view both files to identify differences.

Install missing packages in the system-wide Python:

pip install -r venv_requirements.txt

Alignment with Venv:
If there are still discrepancies between your system-wide Python and the venv, you can generate a requirements file from the venv and apply it to the system-wide Python:

bash
pip freeze > requirements.txt
pip install -r requirements.txt

