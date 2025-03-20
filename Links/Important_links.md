
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

https://github.com/openvinotoolkit/openvino.genai/tree/master/samples/python/image_generation


Very important:
https://github.com/openvinotoolkit/openvino.genai?tab=readme-ov-file#openvino-genai-samples

#Download and convert to OpenVINO dreamlike-anime-1.0 model
optimum-cli export openvino --model dreamlike-art/dreamlike-anime-1.0 --weight-format fp16 dreamlike_anime_1_0_ov/FP16

#You can also use INT8 hybrid quantization to further optimize the model and reduce inference latency
optimum-cli export openvino --model dreamlike-art/dreamlike-anime-1.0 --weight-format int8 --dataset conceptual_captions dreamlike_anime_1_0_ov/INT8

https://github.com/openvinotoolkit/openvino.genai/raw/master/src/docs/openvino_genai.svg


https://github.com/openvinotoolkit/openvino_notebooks/tree/latest/notebooks/stable-diffusion-text-to-image

https://user-images.githubusercontent.com/29454499/260981188-c112dd0a-5752-4515-adca-8b09bea5d14a.png


https://docs.openvino.ai/2025/openvino-workflow-generative/inference-with-optimum-intel.html

How to install intel pytorch extension installation:
====================================================

2.1. Install Driver
sudo apt-get install intel-opencl-icd

2.2 Install python packages

https://pytorch-extension.intel.com/installation?platform=gpu&version=v2.5.10%2Bxpu&os=linux%2Fwsl2&package=pip

python -m pip install torch==2.5.1+cxx11.abi torchvision==0.20.1+cxx11.abi torchaudio==2.5.1+cxx11.abi intel-extension-for-pytorch==2.5.10+xpu oneccl_bind_pt==2.5.0+xpu --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/

Sanity Test
python -c "import torch; import intel_extension_for_pytorch as ipex; print(torch.__version__); print(ipex.__version__); [print(f'[{i}]: {torch.xpu.get_device_properties(i)}') for i in range(torch.xpu.device_count())];"


Ensure All Required Libraries Are Installed
Make sure you have Intel oneAPI Level-Zero and OpenCL runtimes installed, as they are critical for GPU operations. Run:


sudo apt update && sudo apt upgrade -y
sudo apt install intel-oneapi-runtime-compilers intel-oneapi-runtime-opencl intel-level-zero-gpu