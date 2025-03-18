## Devices
2) Orange Pi <Br>

 [More details here](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-plus.html)

## **Processor**
- **CPU**: Rockchip RK3588 (8-core, 64-bit)  
  - 4x Cortex-A76 (up to 2.4GHz)  
  - 4x Cortex-A55 (up to 1.8GHz)  

## **Memory**
- **RAM**:  16 GB

## **Graphics**
- **GPU**: ARM Mali-G610 MP4  
  - Supports OpenGL ES 1.1/2.0/3.2, OpenCL 2.2, Vulkan 1.2  
- **NPU**:  
  - Up to 6 TOPS (Tera Operations Per Second) for AI and machine learning  

## **Storage Options**
- **eMMC**: Socket available for eMMC modules (supports 32GB, 64GB, and 256GB)  
- **MicroSD**: Card slot for expandable storage  
- **M.2 Slot**: Supports NVMe SSDs (PCIe 3.0 x4)  

## **Display Interfaces**
- **HDMI Outputs**:  
  - Two HDMI 2.1 ports (up to 8Kp60)  
- **HDMI Input**:  
  - One HDMI input (up to 4Kp60)  
- **USB-C (DisplayPort 1.4)**: Supports up to 8Kp30  

## **Networking**
- **Ethernet**:  
  - Dual 2.5 Gbps RJ45 ports (PoE support with an optional hat)  

## **Operating System Support**
- **Compatible OS**:  
  - Orange Pi OS
  - Android 12  
  - Debian 11  
  - Ubuntu 24.04  (My preferred Light weight OS)
      
   Typical Usecases for me : <Br>
   a) Running File Sharing via Samba Share,<Br>
   b) Running FTP (Non-Secure version due to only intranet usage, Perfromance benefits due to lack of need for authentication)<Br>
   c) Casa-OS Docker Managmement<Br>
   d) Dashboards : Dashy, Heimdall<Br>
   e) Wallabag<Br>
   
   Limitations :
   a) Low powered GPU, not suitable for smooth video playback, though Raspi has dual 4k<Br>
   b) Network bandwidth is somehow limited<Br>
   c) Cannot be used for Video Encoding and Decoding for live Streams, though it supports ffmpeg<Br>
   d) Hardware acceleration works best for H.264 (1080p60), but other formats rely on software decoding.<Br>
      ffmpeg & gstreamer struggle a lot.<Br>
   e) Lots of available linux software are not available for arm architecture.<Br>

CasaOS on my Raspberr Pi <Br>
 ![code-tab](/images/Casaos-Rpi4.png) <Br>




