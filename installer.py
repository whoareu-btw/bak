import os
import subprocess
import sys

print("This script will install package below\n -curl\n -podman\n -nix (multiuser)")

while True:
    choice = input("This script will use sudo access, do you wanto to give access?\n [y/n]").strip().lower()

    if choice in ["y", "yes"]:
        print("Let's do this!")
        break
    else choice in ["n", "no"]:
        print("I'm out")
        break

print("One more time, this script will use sudo access")

if os.getuid() !=0:
    print("Get ready!")
    os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
    sys.exit(1)

ITEMS = ["curl", "podman"]

subprocess.run(["apt", "install", *ITEMS])

print("Will curling nix from source")

COMMAND = "sh <(curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install) --daemon"
subprocess.run(["bash", "-c", COMMAND])

print("It's done, soldier!")