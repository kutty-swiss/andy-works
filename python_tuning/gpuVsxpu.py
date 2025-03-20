import time

size = 1000

# CPU Test
cpu_tensor = torch.randn(size, size)
start = time.time()
cpu_result = cpu_tensor @ cpu_tensor
print("CPU Time:", time.time() - start)

# XPU Test
xpu_tensor = cpu_tensor.to("xpu")
start = time.time()
xpu_result = xpu_tensor @ xpu_tensor
print("XPU Time:", time.time() - start)
