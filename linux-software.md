### Debian Packages

| Command/Utility       | Description                                              |
|------------------------|----------------------------------------------------------|
| `tree`                | Displays directories as trees.                           |
| `locate`              | Quickly finds files by name.                             |
| `btop`                | Resource monitor with a modern interface.                |
| `iotop-c`             | Displays real-time disk I/O usage by processes.          |
| `jq`                  | Command-line JSON processor.                             |
| `mpv`                 | Lightweight media player.                                |
| `tasksel`             | Task-based package installer.                            |
| `cockpit`             | Web-based system management tool.                        |
| `gnome-tweaks`        | Customizes GNOME desktop settings.                       |
| `gnome-shell-extensions` | Adds extra functionality to GNOME Shell.              |
| `gnome-software`      | GNOME's graphical software manager.                      |
| `stacer`              | System optimizer and monitoring tool.                    |
| `neofetch`            | Displays system information in the terminal.             |
| `chromium-browser`    | Open-source web browser.                                 |
| `notepadqq`           | Notepad++ alternative for Linux.                         |
| `rpi-imager`          | Raspberry Pi imaging utility.                            |
| `filezilla`           | FTP client for file transfers.                           |
| `geany`               | Lightweight text editor and IDE.                         |
| `yt-dlp`              | Downloads videos from YouTube and other platforms.       |
| `streamlink`          | Streams videos from various services in a media player.  |
| `vlc`                 | Versatile media player.                                  |
| `vainfo`              | Displays VA-API (hardware acceleration) information.     |
| `kodi`                | Open-source home theater software.                       |

---

### Snap Packages (Ubuntu Specific)

| Command/Utility       | Description                                              |
|------------------------|----------------------------------------------------------|
| `snap`               | Package manager for Snap applications.                   |
| `snap-store`         | Graphical interface for managing Snap packages.          |
| `vivaldi`            | Privacy-focused web browser.                             |
| `notepadnext`        | Advanced text editor (Notepad++ alternative).            |
| `freetube`           | Privacy-focused YouTube client.                          |
| `webmin`             | Web-based system administration tool.                    |

---

### Flatpak Applications

| Command/Utility         | Description                                              |
|--------------------------|----------------------------------------------------------|
| `org.freedesktop.Platform` | Base runtime for Flatpak applications.                 |
| `io.github.subhra74.Muon`  | Modern file manager for Linux.                         |
| `com.vivaldi.Vivaldi`      | Privacy-focused web browser.                           |
| `com.github.dail8859.NotepadNext` | Advanced text editor (Notepad++ alternative).  |
| `net.newpipe.NewPipe`       | Lightweight YouTube client.                           |
| `io.freetubeapp.FreeTube`   | Privacy-focused YouTube client.                       |
| `io.github.prateekmedia.pstube` | YouTube downloader and player.                   |
| `dev.fredol.open-tv`        | Open-source IPTV player.                              |


## Special Linux Commands used for GPU / LLM inferencing

| **Command**                                      | **Description**                                                 | **Group**        | **ID**   |
|--------------------------------------------------|---------------------------------------------------------------|------------------|----------|
| `clinfo`                                         | Displays information about OpenCL platforms and devices.       | System Info      | `cmd034` |
| `sy-ls`                                          | Lists available SYCL platforms and devices.                    | System Info      | `cmd035` |
| `lspci \| grep -i 'vga'`                           | Lists all PCI devices and filters for VGA (graphics) devices.  | Hardware Info    | `cmd036` |
| `vulkaninfo \| grep "deviceName"`                  | Shows Vulkan device information and filters for device name.   | Graphics Info    | `cmd037` |
| `clinfo \| grep "OpenCL"`                          | Filters OpenCL information from the `clinfo` output.           | System Info      | `cmd040` |
| `zocl-ls`                                        | Lists available devices for the Zynq OpenCL runtime.           | System Info      | `cmd043` |
| `vainfo`                                         | Displays information about VA-API (Video Acceleration API).    | Video Info       | `cmd044` |
| `intel-opencl --check`                           | Checks the OpenCL runtime installation on Intel platforms.     | System Info      | `cmd045` |
| `dmesg \| grep i915`                              | Filters `dmesg` log output for Intel GPU (i915) information.   | System Info      | `cmd046` |



### Most used commands
Note : I have removed basic commands from the list.


| **Command**    | **Description**                                      | **Group**       | **ID**  |
|----------------|------------------------------------------------------|-----------------|---------|
| `echo`         | Prints text to the terminal or a file.               | Basic Commands  | `cmd001`|
| `htop`         | Interactive process viewer (alternative to top).    | System Monitoring| `cmd002`|
| `df`           | Shows disk space usage.                              | Disk Management | `cmd003`|
| `du`           | Displays disk usage of files and directories.        | Disk Management | `cmd004`|
| `free`         | Displays memory usage.                               | System Monitoring| `cmd005`|
| `ps`           | Lists running processes.                             | System Monitoring| `cmd006`|
| `grep`         | Searches for patterns in files.                      | Text Processing | `cmd007`|
| `find`         | Searches for files and directories.                  | File Search     | `cmd008`|
| `ping`         | Tests network connectivity to a host.                | Networking      | `cmd009`|
| `traceroute`   | Traces the route packets take to a host.             | Networking      | `cmd010`|
| `ifconfig`     | Displays or configures network interfaces.           | Networking      | `cmd011`|
| `netstat`      | Displays network connections and statistics.         | Networking      | `cmd012`|
| `curl`         | Transfers data from or to a server.                  | Networking      | `cmd013`|
| `wget`         | Downloads files from the web.                        | Networking      | `cmd014`|
| `tar`          | Archives files into a tarball.                       | File Management | `cmd015`|
| `zip`/`unzip`  | Compresses or extracts zip files.                    | File Management | `cmd016`|
| `chmod`        | Changes file permissions.                            | File Management | `cmd017`|
| `chown`        | Changes file ownership.                              | File Management | `cmd018`|
| `systemctl`    | Manages system services.                             | System Management| `cmd019`|
| `journalctl`   | Views system logs.                                   | System Monitoring| `cmd020`|
| `uptime`       | Displays system uptime.                              | System Monitoring| `cmd021`|
| `whoami`       | Prints the current user.                             | Basic Commands  | `cmd022`|
| `uname`        | Displays system information.                         | System Info     | `cmd023`|
| `dmesg`        | Prints kernel ring buffer messages.                  | System Monitoring| `cmd024`|
| `ssh`          | Connects to a remote machine via SSH.                | Networking      | `cmd025`|
| `scp`          | Copies files between hosts over SSH.                 | Networking      | `cmd026`|
| `rsync`        | Synchronizes files and directories.                  | File Management | `cmd027`|
| `alias`        | Creates shortcuts for commands.                      | Basic Commands  | `cmd028`|
| `history`      | Shows the command history.                           | Basic Commands  | `cmd029`|
| `id`           | Prints user and group information.                   | User Info       | `cmd030`|
| `groups`       | Displays the groups a user is a member of.           | User Info       | `cmd031`|
| `sudo -i`     | Switches to root mode (interactive shell).          | System Management | `cmd032`|
| `export`      | Sets environment variables in the current session.  | Environment Setup | `cmd033`|














