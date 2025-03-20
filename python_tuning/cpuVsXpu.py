import torch
import time

size = 1000  # You can increase this to 5000 or 10000 for better comparisons

# Ensure PyTorch recognizes the XPU device
if not torch.xpu.is_available():
    print("XPU is not available! Make sure Intel PyTorch is installed correctly.")
    exit()

print("Torch Version:", torch.__version__)

# ✅ CPU Test
cpu_tensor = torch.randn(size, size, device="cpu")  # Directly on CPU
start = time.time()
cpu_result = cpu_tensor @ cpu_tensor  # Matrix multiplication
cpu_time = time.time() - start
print("CPU Time:", cpu_time)

# ✅ XPU Test (Intel GPU)
xpu_tensor = torch.randn(size, size, device="xpu")  # Directly on XPU
start = time.time()
xpu_result = xpu_tensor @ xpu_tensor  # Matrix multiplication
xpu_time = time.time() - start
print("XPU Time:", xpu_time)

# ✅ Speedup Calculation
if xpu_time > 0:  # Avoid division by zero
    print(f"Speedup: {cpu_time / xpu_time:.2f}x 🚀")
else:
    print("XPU execution time is too small to measure accurately!")

