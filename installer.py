import os
import subprocess
import sys

print("This script will install package below\n -curl\n -podman\n -nix")

while True:
    choice = input("This script will use sudo access, do you wanto to give access?").strip().lower()

    if choice in ["y", "yes"]:
        print("Let's do this!")
        break
    elif choice in ["n", "no"]:
        print("I'm out")
        break
    else:
        print("Nothing")

if os.getuid() !=0:
    print("Get ready!")
    os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
    sys.exit(1)

ITEMS= ["curl", "podman"]

subprocess.run(["apt", "install", *ITEMS])

print("Will curling nix from source")

subprocess.run(["bash -c\ "sh <(curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install) --daemon""])
shell = True

print("It's done, soldier!")