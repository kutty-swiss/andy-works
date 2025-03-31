Notes for setting up ForgeUi:
=============================

git clone https://github.com/lllyasviel/stable-diffusion-webui-forge ForgeUi
cd ForgeUI
./webui.sh

You need to edit the following files:
====================================
1) /home/andy/ForgeUI/backend/memory_management.py

def should_use_bf16(device=None, model_params=0, prioritize_performance=True, manual_cast=False):
    return False

def should_use_fp16(device=None, model_params=0, prioritize_performance=True, manual_cast=False):
    return False    

def get_torch_device():
    return torch.device("cpu")

 2) /home/andy/ForgeUI/webui-user.sh

 export COMMANDLINE_ARGS="--ckpt-dir /home/andy/models/image-models/stable-diffusion \
--lora-dir /home/andy/models/image-models/lora \
--vae-dir /home/andy/models/image-models/vae \
--embeddings-dir /home/andy/models/image-models/embeddings \
--controlnet-dir /home/andy/models/image-models/controlnet --lowram"  


ForgeUI Desktop: 
==============

Paths:
/home/andy/.local/share/applications/ForgeUI.desktop
/home/andy/Desktop/ForgeUI.desktop

[Desktop Entry]
Version=1.0
Type=Application
Name=Forge
Exec=/home/andy/ForgeUI/webui.sh
Icon=/home/andy/Pictures/reforge.webp
Terminal=true
Categories=Graphics;
StartupWMClass=Forge
