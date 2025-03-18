## Devices
1) Raspberry Pi <Br>
   Model : Pi 4 | 4 GB RAM | Very Low Powered GPU | Headless | Very low power consumption | <Br>
   
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
 ![code-tab](/images/Casaos-Rpi4.png)

Wallabag Bookmark on my Rpi4 <Br>
 ![code-tab](/images/Wallabag-rpi4.png)
 
Dashy Dashbaord on my Rpi4 <Br>
 ![code-tab](/images/Dashy-Rpi4.png)


