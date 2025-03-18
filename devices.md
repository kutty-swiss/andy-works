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
   
 ![code-tab](/images/Casaos-Rpi4.png)
 
2) Orange Pi 5 Plus with 16 GB RAM, 6 TOPS NPU Processor with really good hardware specs<Br>
4) AWOW AK-10 Pro<Br>
5) Intel Nuc 12 i5 with 32 GB RAM ( Self configured to complete PC from barebone)<Br>

   Each of the above devices have their own advantages.<Br>
