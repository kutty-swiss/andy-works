## Devices
1) Raspberry Pi
   Model : Pi 4 | 4 GB RAM | Very Low Powered GPU | Headless | Very low power consumption | 
   
   Typical Usecases for me :
   a) Running File Sharing via Samba Share,
   b) Running FTP (Non-Secure version due to only intranet usage, Perfromance benefits due to lack of need for authentication)
   c) Casa-OS Docker Managmement
   d) Dashboards : Dashy, Heimdall
   e) Wallabag
   
   Limitations :
   a) Low powered GPU, not suitable for smooth video playback, though Raspi has dual 4k
   b) Network bandwidth is somehow limited
   c) Cannot be used for Video Encoding and Decoding for live Streams, though it supports ffmpeg
   d) Hardware acceleration works best for H.264 (1080p60), but other formats rely on software decoding.
      ffmpeg & gstreamer struggle a lot.
   e) Lots of available linux software are not available for arm architecture.
   

2) Orange Pi 5 Plus with 16 GB RAM, 6 TOPS NPU Processor with really good hardware specs
4) AWOW AK-10 Pro
5) Intel Nuc 12 i5 with 32 GB RAM ( Self configured to complete PC from barebone)

   Each of the above devices have their own advantages.
