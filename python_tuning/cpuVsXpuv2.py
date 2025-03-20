import torch
import time

size = 10000  # Increase size for a meaningful test
iterations = 5  # Run multiple times to average out anomalies

if not torch.xpu.is_available():
    print("XPU is not available! Ensure Intel PyTorch is installed correctly.")
    exit()

print("Torch Version:", torch.__version__)

# ✅ Warm-up
torch.randn(size, size, device="xpu")  # Warm-up allocation
torch.xpu.synchronize()  # Ensure GPU is ready

# ✅ CPU Test
cpu_times = []
for _ in range(iterations):
    cpu_tensor = torch.randn(size, size, device="cpu")
    start = time.time()
    cpu_result = cpu_tensor @ cpu_tensor
    cpu_times.append(time.time() - start)

cpu_avg_time = sum(cpu_times) / iterations
print(f"Average CPU Time: {cpu_avg_time:.6f} sec")

# ✅ XPU Test
xpu_times = []
for _ in range(iterations):
    xpu_tensor = torch.randn(size, size, device="xpu")  # Directly allocate on XPU
    torch.xpu.synchronize()  # Ensure no previous work interferes
    start = time.time()
    xpu_result = xpu_tensor @ xpu_tensor
    torch.xpu.synchronize()  # Wait for XPU to finish before timing
    xpu_times.append(time.time() - start)

xpu_avg_time = sum(xpu_times) / iterations
print(f"Average XPU Time: {xpu_avg_time:.6f} sec")

# ✅ Speedup Calculation
if xpu_avg_time > 0:
    print(f"Speedup: {cpu_avg_time / xpu_avg_time:.2f}x 🚀")
else:
    print("XPU execution time is too small to measure accurately!")
