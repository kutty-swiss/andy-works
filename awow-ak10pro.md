# **Devices**  

## **AWOW AK10 Pro**  

### **Case View**  
<img src="https://m.media-amazon.com/images/I/61jd7fMGXHL._AC_SX679_.jpg" alt="AWOW AK10 Pro" width="700">  

🔗 [**More details here**](https://www.amazon.de/AWOW-AK10-Desktop-Computer-Ethernet/dp/B0D7L6V82N?th=1)  


# AWOW AK10 Pro Specifications

## **Processor**
- **CPU**: Intel Processor N100 (Quad-core, 64-bit)
  - 4x Gracemont Efficient Cores (up to 3.4GHz)

## **Memory**
- **RAM**: 16 GB DDR4 (Upgradable)

## **Graphics**
- **GPU**: Intel UHD Graphics
  - Supports 4K@60Hz Dual Screen Display

## **Storage Options**
- **M.2 SSD**: I upgraded it to 1 TB

## **Display Interfaces**
- **HDMI Output**: 1x Full-Sized HDMI Port
- **DisplayPort**: 1x DisplayPort

## **Networking**
- **Ethernet**: Dual Gigabit Ethernet Ports (1 Gbps each)
- **Wi-Fi**: Wi-Fi 5
- **Bluetooth**: Bluetooth 5.0

## **USB Ports**
- **USB 3.0**: 2x Type-A
- **USB 2.0**: 2x Type-A

## **Operating System Support**
- **Compatible OS**:
  - Windows 11 Pro
  - Linux distributions (community-supported)
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

### **1️⃣ AI Software & Compilation Experience**  
AI inference can be executed using **C++** or **Python** implementations. After testing various setups, I custom-compiled **Llama.cpp** with extensive optimization flags for enhanced performance.  

The following **CMake command** requires pre-installed dependencies, including:  
✅ C++ Compiler (e.g., `icx`, `icpx`)  
✅ Intel OneAPI  
✅ Vulkan SDK  
✅ Diagnostic tools (`vainfo`, `sycl-ls`, etc.)  

### **2️⃣ Custom Compilation Command (Llama.cpp)**
```sh
# Run CMake with optimized MKL integration  
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
```
   

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

### Very important Tweak
Like in Windows task manager, linux does not have a proper GPU monitor for non-nvidia cards. After a lot of struggle i managed to get a working version of a tool "Mission Center"
![image](https://github.com/user-attachments/assets/7abf95fa-7972-4627-b60b-4e414c8ca415)

In addition i used Gnome shell monitoring extensions to have an eye on CPU load & memory usage ( GPU not yet supported)
![image](https://github.com/user-attachments/assets/ec8ed3cb-b752-4ce9-900b-d5df5fe0f207)

