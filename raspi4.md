## Devices

### 1️⃣ Raspberry Pi 4
- **Model**: Pi 4 | 4 GB RAM  
- **GPU**: Very Low Powered  
- **Usage Mode**: Headless  
- **Power Consumption**: Very low (~4 watts)  

![Raspberry Pi 4](https://assets.raspberrypi.com/static/raspberry-pi-4-labelled-f5e5dcdf6a34223235f83261fa42d1e8.png)

---

### 🔹 Typical Use Cases
- 🗂 **File Sharing** via Samba Share
- 🗂 **File Sharing** via nginx through browser 
- 🔄 **FTP Server** (Non-secure, intranet only, better performance)  
- 🐳 **CasaOS** for Docker Management  
- 📊 **Dashboards**: Dashy, Heimdall  
- 📚 **Bookmark Manager**: Wallabag  

---

### ⚠️ Limitations
1. 🖥 **Low-powered GPU**: Not suitable for smooth video playback despite dual 4K output  
2. 🌐 **Network Bandwidth**: Somewhat limited  
3. 🎥 **No Video Encoding/Decoding for Live Streams** (ffmpeg support, but limited hardware acceleration)  
4. 🔄 **Hardware Acceleration**:  
   - Works best for **H.264 (1080p60)**  
   - Other formats rely on **software decoding**, causing performance issues  
   - **ffmpeg & gstreamer** struggle with non-H.264 formats  
5. 🖥 **Software Availability**: Many Linux applications lack ARM architecture support  

---

## 📌 CasaOS on Raspberry Pi 4  
![CasaOS](/images/Casaos-Rpi4.png)

## 📌 Wallabag Bookmark on Raspberry Pi 4  
![Wallabag](/images/Wallabag-rpi4.png)

## 📌 Dashy Dashboard on Raspberry Pi 4  
![Dashy](/images/Dashy-Rpi4.png)
