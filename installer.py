import os
import subprocess
import sys

print("This script will install package below\n -curl\n -podman\n -nix")

while True:
    choice = input("This script will use sudo access, do you wanto to give access?").strip().lower()

    if choice in ["y", "yes"]:
        print("Let's do this!")
        break
    else choice in ["n", "no"]:
        print("I'm out")
        break

while True:
    choice = input("Are you sure").strip().lower()

    if choice in ["y", "yes"]:
        print("alright soldier!")
        break
    else choice in ["n", "no"]:
        print("It's ok, soldier. Maybe next time")
        break


print("One more time, this script will use sudo access")

if os.getuid() !=0:
    print("Get ready!")
    os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
    sys.exit(1)

ITEMS= ["curl", "podman"]

subprocess.run(["apt", "install", *ITEMS])

print("Will curling nix from source")

subprocess.run(["sh <(curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install) --daemon"])

print("It's done, soldier!")