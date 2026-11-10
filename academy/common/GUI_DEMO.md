# Real GUI demos in the sandbox (no hardware virtualization, no GPU needed)

Run any Linux GUI app on a virtual screen, drive it with xdotool, screenshot with ImageMagick `import`.

    apt-get install -y --no-install-recommends virtualbox-qt xdotool openbox   # example app
    export DISPLAY=:99 HOME=/tmp/guihome; mkdir -p $HOME
    Xvfb :99 -screen 0 1920x1080x24 &  openbox &  VirtualBox &
    W=$(xdotool search --name "VirtualBox Manager" | head -1); xdotool windowmove $W 0 0 windowsize $W 1920 1080
    xdotool mousemove X Y click 1;  xdotool type --delay 80 "text";  xdotool key Tab
    import -window root shot.png; convert shot.png -crop WxH+X+Y crop.png

Limits (state them in the video): VMs cannot boot (no /dev/kvm), downloads from vendor sites are blocked by the
network allowlist (apt works), and these are Linux builds of the app. Label as "REAL SCREENSHOT" and say which build.
Also usable with ffmpeg -f x11grab for screen recordings. Never claim a Windows/macOS capture from this.
