For sd next, be default it installs pytorch with gpu support but ak10 does not support

Solution:
=========
pip list | grep xpu
pip list | grep torch
pip install --upgrade pip
pip uninstall torch torchvision torchaudio pytorch-triton-xpu
pip install torch==2.2.2 torchvision==0.17.2 --index-url https://download.pytorch.org/whl/cpu

To run:
=======
~/sdnext/webui.sh --lowvram


To work with Venv:
================
source ~/sdnext/venv/bin/activate


CPU version of torch
====================

python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
python -m pip install intel-extension-for-pytorch
python -m pip install oneccl_bind_pt --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/cpu/us/

Details : https://pytorch-extension.intel.com/installation?platform=cpu&version=v2.6.0%2Bcpu&os=linux%2Fwsl2&package=pip

-----------------------------------------------------------------------------------------------------------------------------------
 


-----------------------------------------------------------------------------------------------------------------------------------
Image Prompt:
============

Positive Prompt:
a designer building. architectural photography, f/12, luxury, aesthetically pleasing form and function, masterpiece, best quality, very high intricate detailing, sharp focus, natural lighting, slightly dark blue sky, (((photorealistic))), octane render, HDR, 8k, high contrast, 

Negative Prompt:
((unrealistic)), painting, ((cartoon)), digital art, (bad anatomy), deformed, low quality, worst quality, ((bad edges)), blur

Seed: 3163416539

CFG Scale : 7.5

Steps : 20 OR 30

Sampler : DPM++ *M Karras
## Additional Notes

### Troubleshooting
If you encounter issues with PyTorch installation or compatibility, ensure the following:
1. Verify your Python version is compatible with the specified PyTorch version.
2. Check your system's hardware (CPU/GPU) and install the appropriate PyTorch build.
3. Use `pip cache purge` to clear any cached packages if installation errors persist.

### Useful Commands
- **Check Installed Packages:**
    ```bash
    pip list | grep <package_name>
    ```
- **Uninstall Specific Packages:**
    ```bash
    pip uninstall <package_name>
    ```
- **Activate Virtual Environment:**
    ```bash
    source <path_to_venv>/bin/activate
    ```

### References
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [Intel PyTorch Extensions](https://pytorch-extension.intel.com/installation)

### Example Image Prompt
For generating high-quality architectural renders, you can experiment with the following parameters:
- **Positive Prompt:** 
    ```text
    a futuristic skyscraper, ultra-modern design, photorealistic, HDR, 8k resolution, intricate details, sharp focus, natural lighting, cinematic atmosphere
    ```
- **Negative Prompt:** 
    ```text
    cartoonish, unrealistic, low quality, blurry, distorted, overexposed
    ```
- **Seed:** `1234567890`
- **CFG Scale:** `8.0`
- **Steps:** `25`
- **Sampler:** `Euler a`

Feel free to tweak these values to suit your creative needs.