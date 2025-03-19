## Building and Running Llama.cpp for Intel GPUs
Custom compiling Llama.cpp allows for optimized performance tailored to your specific hardware, enabling faster inference and better resource utilization.

### Clone or Update the Repository
```bash
cd /home/andy/
rm -rf /home/andy/llama.cpp
git clone https://github.com/ggerganov/llama.cpp.git /home/andy/llama.cpp
```

### Prepare the Build Directory
```bash
cd /home/andy/llama.cpp
rm -rf build  # Clean up any existing build
mkdir build && cd build
```

### Configure the Build with CMake
Run the following command to configure the build with Intel GPU support and MKL integration:
```bash
cmake .. \
    -DCMAKE_C_COMPILER=$(which icx) \
    -DCMAKE_CXX_COMPILER=$(which icpx) \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_PREFIX_PATH="/opt/intel/oneapi" \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DGGML_NATIVE=ON \
    -DGGML_AVX2=ON \
    -DGGML_AVX512=ON \
    -DGGML_FP16=ON \
    -DGGML_INT8=ON \
    -DGGML_MEMORY_OPTIMIZE=ON \
    -DGGML_SYCL=ON \
    -DGGML_SYCL_DEVICE=SYCL0 \
    -DGGML_SYCL_DEVICE_ARCH=GEN12LP \
    -DGGML_SYCL_TARGET=INTEL \
    -DGGML_SYCL_LEVEL_ZERO=ON \
    -DGGML_MKL=ON \
    -DGGML_USE_MKL=ON \
    -DGGML_OPENBLAS=ON \
    -DGGML_OPENVINO=ON \
    -DGGML_OPENVINO_BNNS=ON \
    -DGGML_OPENVINO_VPU=ON \
    -DGGML_OPENVINO_USE_INT8=ON \
    -DGGML_VULKAN=ON \
    -DGGML_OPENCL=ON \
    -DGGML_OPENCL_TARGET=intel_gpu \
    -DGGML_OPENCL_USE_ADRENO_KERNELS=OFF \
    -DGGML_LEVEL_ZERO=ON \
    -DOpenCL_INCLUDE_DIR="/opt/intel/oneapi/compiler/2025.0/include/sycl/CL" \
    -DDNNL_DIR="/opt/intel/oneapi/dnnl/latest" \
    -DOpenCL_LIBRARY="/opt/intel/oneapi/compiler/2025.0/lib/libOpenCL.so.1" \
    -DTBB_ROOT="/opt/intel/oneapi/tbb" \
    -DCMAKE_EXE_LINKER_FLAGS="-ltbb"
```

### Build the Project
```bash
cmake --build . --config Release
# Alternatively, use:
make -j$(nproc)
```

---

## Sample Inference Commands with 3 types of GPU based backends

### Fastest: Vulkan
```bash
~/llama.cpp/build/bin/llama-server \
    -m ~/.lmstudio/models/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf \
    --device Vulkan0 -n 128 -c 2048 -t 3 -e
```
> **Note:** Do not use `-ngl` for Vulkan.

---

### Medium Speed: SYCL0
```bash
~/llama.cpp/build/bin/llama-server \
    -m ~/.lmstudio/models/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf \
    --device SYCL0 -n 128 -c 2048 -t 3 -e -ngl 30
```

---

### CPU Main: GPUOpenCL
```bash
~/llama.cpp/build/bin/llama-server \
    -m ~/.lmstudio/models/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf \
    --device GPUOpenCL -n 128 -c 2048 -t 3 -e -ngl 30
```

    