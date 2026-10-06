#!/usr/bin/env python3
import os
import shutil
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
SOURCE_DIR = os.path.join(BASE_DIR, "base-mint-y-aqua")
DEST_SYSTEM = os.path.join(ROOT_DIR, "usr", "share", "themes", "Oxygen-Mint")
DEST_USER = os.path.expanduser("~/.themes/Oxygen-Mint")

def build_theme():
    print("==================================================")
    print("Building Oxygen-Mint Theme (Mint-Y-Aqua Backbone)")
    print("==================================================")

    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Source directory {SOURCE_DIR} does not exist!")
        sys.exit(1)

    # Clean and recreate build directory
    if os.path.exists(DEST_SYSTEM):
        shutil.rmtree(DEST_SYSTEM)
    os.makedirs(DEST_SYSTEM, exist_ok=True)

    # 1. Copy all components from base-mint-y-aqua
    print("1. Assembling theme modules from Mint-Y-Aqua backbone...")
    for item in os.listdir(SOURCE_DIR):
        src_path = os.path.join(SOURCE_DIR, item)
        dest_path = os.path.join(DEST_SYSTEM, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
            print(f"   + Copied directory: {item}")
        else:
            shutil.copy2(src_path, dest_path)
            print(f"   + Copied file: {item}")

    print(f"\n[OK] Theme package successfully generated at:\n     {DEST_SYSTEM}")

    # 2. Deploy to user themes directory for immediate usage
    print(f"\n2. Deploying to user themes directory:\n     {DEST_USER} ...")
    if os.path.exists(DEST_USER):
        shutil.rmtree(DEST_USER)
    os.makedirs(os.path.dirname(DEST_USER), exist_ok=True)
    shutil.copytree(DEST_SYSTEM, DEST_USER)

    # 3. Ensure permissions are readable
    os.system(f"chmod -R a+rX {DEST_USER}")
    os.system(f"chmod -R a+rX {DEST_SYSTEM}")

    print(f"[OK] Successfully installed to: {DEST_USER}")
    print("==================================================")
    print("Oxygen-Mint (Mint-Y-Aqua Backbone) is ready!")
    print("Supports: GTK 3, GTK 4, Libadwaita, MATE (Marco), Cinnamon, GTK 2")
    print("==================================================")

if __name__ == "__main__":
    build_theme()
