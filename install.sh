#!/usr/bin/env bash
# ==============================================================================
# Oxygen-Mint Theme Installer
# Builds and installs Oxygen-Mint theme to ~/.themes/Oxygen-Mint
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN=""

if command -v python3 &>/dev/null; then
    PYTHON_BIN="python3"
elif command -v python &>/dev/null; then
    PYTHON_BIN="python"
else
    echo "Error: Python 3 is required to build Oxygen-Mint." >&2
    exit 1
fi

echo "=================================================="
echo " Oxygen-Mint Theme Installer"
echo "=================================================="

"${PYTHON_BIN}" "${SCRIPT_DIR}/src/build-themes.py" "$@"

echo ""
echo "[OK] Installation completed successfully!"
echo "You can now select 'Oxygen-Mint' in your Appearance / Themes settings."
echo "=================================================="
