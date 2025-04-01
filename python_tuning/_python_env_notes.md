
python3.10 -m venv ~/venv_310
source ~/venv_310/bin/activate


pip install --upgrade pip
pip install pillow wheel setuptools openvino-genai==2025.0.0 diffusers
pip install optimum[intel]

to install openvino dependencies:
==================================
pip install -r https://raw.githubusercontent.com/openvinotoolkit/openvino.genai/refs/heads/master/samples/deployment-requirements.txt