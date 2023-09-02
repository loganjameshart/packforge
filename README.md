# Packforge

A Python interface for Linux package management.

## Supported Distros / Package Managers

- Debian and Debian-based (apt)
- Fedora (dnf)
- CentOS (yum)
- Arch (pacman)

## Installation

```bash
pip install packforge
```

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
