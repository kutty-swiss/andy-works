
## Devices
4) Intel Nuc12i5 <Br>

This is far superior compared to Ak10 n100 PC. Also has 64GB RAM and a strong processor (better CPU & GPU Specs). Most of the mid sized Large Language models are easily supported by it.

<img src="https://m.media-amazon.com/images/I/71NQkh6a2tL._AC_SL1500_.jpg" alt="Logo" width="700"> <Br>

[More details here](https://www.amazon.com/NUC12WSKi5-Computer-i5-1240P-Processor-Graphics/dp/B0BPCJ59BH?th=1)


## **Processor**
- **CPU**: Intel Core i5-1240P (12 cores, 16 threads)
  - Performance Cores: 4 (up to 4.4GHz)
  - Efficient Cores: 8 (up to 3.3GHz)

## **Memory**
- **RAM**: 32 GB DDR4-3200MHz

## **Graphics**
- **GPU**: Intel Iris Xe Graphics
  - Supports up to four 4K displays simultaneously

## **Storage Options**
- **M.2 SSD**: 1 TB NVMe SSD (PCIe Gen4x4)
  - *Supports expansion up to 8 TB*
- **SATA**: 2.5" SATA 6Gb/s bay
  - *Supports additional SSD/HDD up to 4 TB*

## **Display Interfaces**
- **HDMI Outputs**: 2x HDMI 2.0b ports
- **Thunderbolt 4**: 2x ports supporting DisplayPort 1.4a

## **Networking**
- **Ethernet**: 1x 2.5 Gbps Intel i225-LM port
- **Wi-Fi**: Intel Wi-Fi 6E AX211
- **Bluetooth**: Bluetooth 5.2

## **USB Ports**
- **USB 3.2**: 3x Type-A ports
- **Thunderbolt 4**: 2x Type-C ports
- **Audio Jack**: 1x 3.5mm headphone/microphone combo jack

## **Operating System Support**
- **Compatible OS**:
  - Windows 11 Pro
  - Ubuntu 24.04 LTS
  - In my case i have dual boot with Ubuntu 24.04 (Primary OS) & Windows 11.
      
 ## **Typical Usecases for me**
   a) Very good software support with almost all possible .deb packages installable due to X64 architecture<Br>
   b) Very capable and power efficient due to n100, slightly consumnes more than orange pi, but fan cooled<Br>
   c) Jellyfin/ FFMpeg / GStreamer Transcoding<Br>
   d) One of the daily driver / always running<Br>
   e) Running FTP (Non-Secure version due to only intranet usage, Perfromance benefits due to lack of need for authentication)<Br>
   f) Casa-OS Docker Managmement<Br>
   g) Dashboards : Dashy, Heimdall, Next Cloud, Obsidian Notes <Br>
   h) Intel OneAPI, Intel OpenVino, Level Zero, SYCL, OpenCL, Vulkan <Br>
   g) Versatile Software support including LLM inference Software<Br>
   h) SSD Support, Higher RAM ( useful for ai llm loading, but single channel), Highspeed network<Br>
   i) Samba File Sharing to all devices like Win / Lin PCs, Android Set-top-box, Mobile devices<Br>
   j) Faster GPU experience compared to Orange Pi 5 Plus 
   
  ## **Limitations**
   a) Single Channel RAM, may limit the bandwidth of loading and execution of large language models<Br>
   b) Better software support than orang pi, but not on par support & software comared to expensive nvidia GPUs<Br>
   c) Integrated GPUs consume less power, but also performance is slower compared to eGPU<Br>

  ## **AI Inference**
   a) AI programs currently use either C++ OR Python version.
   I tried all the combinations. After a lot of hassles, I custom compiled Lllama.cpp using a vast amount of flags for compilation.
   The following command assumes a number of supporting software installed for example C++ compiler, intel One API, Vulkan SDK, diagnositic sofware like vainfo, sycl-ls etc.

   # Run CMake with your configuration (Focus on proper MKL integration)
   cmake .. \
    -DCMAKE_C_COMPILER=$(which icx) \
    -DCMAKE_CXX_COMPILER=$(which icpx) \
    -DGGML_NATIVE=ON \
    -DGGML_AVX2=ON \
    -DGGML_AVX512=ON \
    -DGGML_OPENBLAS=ON \
    -DGGML_MKL=ON \
    -DGGML_SYCL=ON \
    -DGGML_SYCL_DEVICE=SYCL0 \
    -DGGML_SYCL_DEVICE_ARCH=GEN12LP \
    -DGGML_SYCL_TARGET=INTEL \
    -DGGML_OPENVINO=ON \
    -DGGML_OPENVINO_BNNS=ON \
    -DGGML_OPENVINO_VPU=ON \
    -DGGML_OPENCL=ON \
    -DGGML_OPENCL_TARGET=intel_gpu \
    -DGGML_OPENCL_USE_ADRENO_KERNELS=OFF \
    -DGGML_VULKAN=ON \
    -DGGML_FP16=ON \
    -DGGML_INT8=ON \
    -DGGML_OPENVINO_USE_INT8=ON \
    -DGGML_LEVEL_ZERO=ON \
    -DGGML_SYCL_LEVEL_ZERO=ON \
    -DGGML_MEMORY_OPTIMIZE=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_PREFIX_PATH="/opt/intel/oneapi" \
    -DOpenCL_INCLUDE_DIR="/opt/intel/oneapi/compiler/2025.0/include/sycl/CL" \
    -DDNNL_DIR="/opt/intel/oneapi/dnnl/latest" \
    -DOpenCL_LIBRARY="/opt/intel/oneapi/compiler/2025.0/lib/libOpenCL.so.1" \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DGGML_USE_MKL=ON
   b) Better software support than orang pi, but not on par support & software comared to expensive nvidia GPUs<Br>
   c) Integrated GPUs consume less power, but also performance is slower compared to eGPU<Br>
   d) Tried variety of image to text AI software:
   Comfy UI, Invoke AI, Easy Diffusion, Automatic1111, Forge, Reforge
   e) All in one AI: LocalAI
   f) Image Upscaler : Upscayl
   g) Intel AI Playground (Windows only), 
   h) Intel AI Reference Models (https://github.com/intel/ai-reference-models)
   i) AI Optimized intel IPEX LLM ( But not on par with custom compiled Llama.cpp)
   

## **Extras**  

### Software Installed  
- **Remote Administration**:  
  - Webmin  
  - Cockpit (for remote administration like shell executions)
  - Portainer & Casa OS ( For managing docker containers like Grafana, Wallabag, Dashy etc )

- **Browser**:  
  - Opera  
  - Firefox
  - Google Chrome
  - MS Edge
    
- **Editors**:  
  - Geany
  - VS Codium

- **SSH GUI**:  
  - Snowflake (Supports both SSH & FTP in one software)  

- **Utilities**:  
  - Stacer  
  - Btop  
  - Neofetch  
  - locate  
  - tree  
  - ffmpeg  
  - gstreamer  
  - ansible  

  
