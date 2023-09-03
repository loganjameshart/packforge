# Packforge

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

![Packforge logo](https://raw.githubusercontent.com/loganjameshart/packforge/main/packforge%20(250%20%C3%97%20250%20px).svg)

A Python interface for Linux package management.

## Supported Distros / Package Managers

- Debian and Debian-based (apt)
- Fedora (dnf)
- CentOS (yum)
- Arch (pacman)

## Configuration

Configuration is within the ```config.ini``` file in the working directory. If one is not found, default settings will be used.

## Current configuration settings

- noconfirm
	- whether or not you are asked Yes/No before changes are made
- printing
	- whether or not package manager messages are printed to stdout

## Usage

The API is centered around the ```Forge```
class:

```python
from packforge import Forge

# initialize the Forge object
forge = Forge()

# list of all packages that were installed upon initialization
forge.installed_packages

# add packages(s) (also updates the forge.installed_packages attribute)
forge.install_package('geany', 'ufw', 'python3-tk')
```

## Contributing
Pull requests are more than welcome, especially from folks interested in expanding this to more distros. Please open an issue to discuss larger changes.

# Roadmap

## Import Future Additions
- Unit tests with ```pytest```
- Proper Python package management with ```poetry```

## Future Support

- Support for more Linux distributions
- Support for pinning package releases
- More robust interactions with package managers:
	- Adding and updating package sources
	- Provide search interface to repositiories

### Timeline

- September 2, 2023: ***RELEASE***
