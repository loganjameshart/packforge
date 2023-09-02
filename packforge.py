"""
A Python interface for package management in Linux distributions.
"""

import subprocess
from configparser import ConfigParser


class Forge:
    def __init__(self):
        """Initialize the Forge instance, detecting both package manager and installed packages."""

        self.package_manager = self._detect_package_manager()
        self.settings = self._forge_configuration()
        self.installed_packages = self.list_installed_packages()

    def _forge_configuration(self) -> dict:
        """Load configuration settings from the 'config.ini' file and return them as a dictionary."""

        settings = {}
        parser = ConfigParser()
        try:
            parser.read("config.ini")
            noconfirm_bool = parser.getboolean("Settings", "noconfirm")
            print_bool = parser.getboolean("Settings", "printing")
            settings["noconfirm"] = noconfirm_bool
            settings["printing"] = print_bool
        except Exception as e:
            print(
                f"An error occurred: {e}\n Please provide config.ini file. Using default settings."
            )
            settings["noconfirm"] = False
            settings["printing"] = True
        return settings

    def _detect_package_manager(self) -> str:
        try:
            with open("/etc/os-release") as os_info_file:
                os_info = os_info_file.read().lower()

            if "ubuntu" in os_info:
                return "apt"
            elif "debian" in os_info:
                return "apt"
            elif "fedora" in os_info:
                return "dnf"
            elif "centos" in os_info:
                return "yum"
            elif "arch" in os_info:
                return "pacman"

        except FileNotFoundError:
            print(FileNotFoundError)

    def _run_subprocess(self, command, print_output=True):
        """Helper function to run the subprocess and optionally print to stdout."""

        if self.settings["printing"]:
            print_output = True
        else:
            print_output = False

        try:
            process = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if print_output:
                print(process.stdout)
            return process
        except Exception as e:
            print(f"An error occurred: {e}")

    def list_installed_packages(self) -> list:
        """Returns a list of installed packages."""

        process = subprocess.run(
            [self.package_manager, "list", "--installed"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        package_list = process.stdout.split("\n")
        return package_list

    def update_packages(self) -> None:
        """Checks for updates for installed packages."""

        try:
            if self.package_manager == "apt" or "yum":
                self._run_subprocess([self.package_manager, "update"])
                self.installed_packages = self.list_installed_packages()
            elif self.package_manager == "dnf":
                self._run_subprocess([self.package_manager, "check-update"])
                self.installed_packages = self.list_installed_packages()
            elif self.package_manager == "pacman":
                self._run_subprocess([self.package_manger, "-Syu"])
                self.installed_packages = self.list_installed_packages()
        except Exception as e:
            print(f"An error occurred: {e}")

    def upgrade_packages(self) -> None:
        """Upgrades installed packages."""

        try:
            if self.package_manager == "apt" or "yum" or "dnf":
                self._run_subprocess([self.package_manger, "upgrade", "-y"])
                self.installed_packages = self.list_installed_packages()
            elif self.package_manger == "pacman":
                self._run_subprocess([self.package_manager, "--upgrade"])
                self.installed_packages = self.list_installed_packages()
        except Exception as e:
            print(f"An error occurred: {e}")

    def install_package(self, *desired_packages: str) -> None:
        """Installs one or multiple packages."""

        try:
            if self.package_manager == "apt" or "yum" or "dnf":
                for package in desired_packages:
                    if self.settings["noconfirm"]:
                        self._run_subprocess(
                            [self.package_manager, "install", "-y", package]
                        )
                    else:
                        self._run_subprocess([self.package_manager, "install", package])
                self.installed_packages = self.list_installed_packages()
            elif self.package_manager == "pacman":
                for package in desired_packages:
                    if self.settings["noconfirm"]:
                        self._run_subprocess(
                            [self.package_manager, "-S", "--noconfirm", package]
                        )
                    else:
                        self._run_subprocess([self.package_manager, "-S", package])
                self.installed_packages = self.list_installed_packages()
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_package(self, *unwanted_packages: str) -> None:
        try:
            if self.package_manger == "apt" or "yum" or "dnf":
                for package in unwanted_packages:
                    if self.settings["noconfirm"]:
                        self._run_subprocess(
                            [self.package_manager, "remove", "-y", package]
                        )
                    else:
                        self._run_subprocess([self.package_manager, "remove", package])
                self.installed_packages = self.list_installed_packages()
            elif self.package_manager == "pacman":
                for package in unwanted_packages:
                    if self.settings["noconfirm"]:
                        self._run_subprocess(
                            [self.package_manager, "-R", "--noconfirm", package]
                        )
                    else:
                        self._run_subprocess([self.package_manager, "-R", package])
                self.installed_packages = self.list_installed_packages()
        except Exception as e:
            print(f"An error occurred: {e}")

    def check_package(self, package):
        """Detects if a package is within the installed packages list attribute."""

        try:
            if package in self.installed_packages:
                return True
            else:
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
