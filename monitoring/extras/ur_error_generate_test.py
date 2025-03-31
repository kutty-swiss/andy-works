import os
import torch
import numpy as np
import intel_extension_for_pytorch as ipex

def print_separator():
    print("-" * 50)

# Print environment variables
print("Environment Variables:")
print("PYTHONPATH : " + os.environ.get("PYTHONPATH", "Not set"))
print("LD_LIBRARY_PATH : " + os.environ.get("LD_LIBRARY_PATH", "Not set"))
print("PATH : " + os.environ.get("PATH", "Not set"))
print_separator()

# Print library versions
print("Library Versions:")
print("torch.__version__ : " + torch.__version__)
print("ipex.__version__ : " + ipex.__version__)
try:
    import oneccl_bindings_for_pytorch as ccl
    print("oneccl_bindings_for_pytorch.__version__ : " + ccl.__version__)
except ImportError:
    print("oneccl_bindings_for_pytorch not installed")
try:
    import openvino
    print("openvino.__version__ : " + openvino.__version__)
except ImportError:
    print("openvino not installed")
try:
    import oneapi
    print("oneapi.__version__ : " + oneapi.__version__)
except ImportError:
    print("oneapi not installed")
try:
    import ipex_llm
    print("ipex_llm.__version__ : " + ipex_llm.__version__)
except ImportError:
    print("ipex_llm not installed")
try:
    import openvino_genai
    print("openvino_genai.__version__ : " + openvino_genai.__version__)
except ImportError:
    print("openvino-genai not installed")
print_separator()

# Check if XPU is available
if torch.xpu.is_available():
    print("torch.xpu.is_available() : True")
    device = torch.xpu.current_device()
    props = torch.xpu.get_device_properties(device)
    print(f"Device: {props.name}")

    # Correctly handle the dictionary returned by get_device_capability
    capabilities = torch.xpu.get_device_capability(device)
    print(f"Device Capabilities=========================================: {capabilities}")
else:
    print("XPU is not available")

# Try creating tensor and converting to FP16 on XPU
t = torch.tensor([1.0, 2.0, 3.0], device="xpu", dtype=torch.float32)

try:
    print("Attempting to convert tensor to float16 on xpu...")
    t_fp16 = t.to(torch.float16)
    print(f"Converted tensor: {t_fp16}")
except RuntimeError as e:
    print(f"RuntimeError during conversion: {e}")
    print_separator()
    print("Workaround: Creating a new float16 tensor on CPU first, then moving to xpu")
    try:
        t_fp16 = torch.tensor(t.cpu().numpy(), dtype=torch.float16, device="xpu")
        print(f"FP16 tensor on xpu: {t_fp16.cpu()}")  # Print from CPU to avoid issues
    except RuntimeError as e:
        print(f"Workaround failed: {e}")

print_separator()
print("Testing float16 tensor creation before moving to xpu")
try:
    t = torch.tensor([0], dtype=torch.float16).to("xpu")
    print(f"Single value FP16 tensor on xpu: {t.cpu()}")
except RuntimeError as e:
    print(f"Error creating FP16 tensor before moving to xpu: {e}")

try:
    print_separator()
    print("Attempting to convert to bfloat16 on xpu...")
    t_bf16 = t.to(torch.bfloat16)
    print(f"Converted to bfloat16: {t_bf16.cpu()}")
except RuntimeError as e:
    print(f"RuntimeError during bfloat16 conversion: {e}")
    print("bfloat16 might not be supported on xpu.")
