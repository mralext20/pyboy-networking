# PyBoy Networking

This is a simple flask app depending on [PyBoy](https://github.com/Baekalfen/PyBoy). 


# Usage
place your rom of choice in the same directory as the app, and set the ROM_NAME enviroment Variable to set the name of the rom in the rom folder.

# Docker

images are published to hub.docker.com/mralext20/pyboy-networking.

use these images with somthing like `docker run -it -e ROM_NAME="tetris.gb" -v $(pwd)/rom:/app/rom --net=host mralext20/pyboy-networking`
