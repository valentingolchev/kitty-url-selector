#!/bin/sh

# Check if fzf is installed
echo "🔍 Checking for fzf dependency..."
if ! command -v fzf >/dev/null 2>&1; then
    echo "⚠️ fzf is required but not installed. Please install fzf first."
    exit 1
fi

# Determine the kitten directory
KITTY_CONFIG_DIR="$HOME/.config/kitty"
if [ $# -gt 0 ]; then
    KITTEN_DIR="$KITTY_CONFIG_DIR/$1"
    KITTEN_PATH="$1/url_select.py"
else
    KITTEN_DIR="$KITTY_CONFIG_DIR"
    KITTEN_PATH="url_select.py"
fi

# Create directory if it doesn't exist
echo "📁 Creating kitten directory at $KITTEN_DIR..."
mkdir -p "$KITTEN_DIR"

# Copy the kitten
echo "📋 Copying url_select.py to $KITTEN_DIR..."
cp url_select.py "$KITTEN_DIR/"

# Add to kitty.conf
KITTY_CONF="$KITTY_CONFIG_DIR/kitty.conf"
echo "⚙️ Updating kitty.conf with keybinding..."
if [ ! -f "$KITTY_CONF" ]; then
    touch "$KITTY_CONF"
fi

# Check if the line already exists
if ! grep -q "map kitty_mod+/ kitten $KITTEN_PATH" "$KITTY_CONF"; then
    echo "map kitty_mod+/ kitten $KITTEN_PATH" >>"$KITTY_CONF"
else
    echo "ℹ️ Keybinding already exists in kitty.conf."
fi

echo "✅ Installation complete."
