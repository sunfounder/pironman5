if [ ! -e /dev/gpiochip0 ]; then
    echo "Softlink gpiochip4 failed: gpiochip0 not found"
    exit 0
fi
if [ ! -e /dev/gpiochip4 ]; then
    echo "Softlink gpiochip4 to gpiochip0"
    sudo ln -s /dev/gpiochip0 /dev/gpiochip4
fi
