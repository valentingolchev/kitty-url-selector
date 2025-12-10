# Kitty URL Selector

A Kitty kitten that extracts URLs from the visible text in the current terminal window, presents them for selection using [fzf](https://github.com/junegunn/fzf), and opens the selected URL in the default browser.

## Features

- 🔍 Extracts URLs from terminal output
- 🎯 Fuzzy search and selection with fzf
- 🌐 Cross-platform URL opening

## Requirements

- [Kitty](https://sw.kovidgoyal.net/kitty/) terminal emulator
- [fzf](https://github.com/junegunn/fzf) fuzzy finder

## Usage

Use the keybinding (default: `kitty_mod+/`) to select and open URLs from the current terminal output. The kitten will extract URLs, present them in fzf for selection, and open the chosen URL.

## Installation

### Automatic Installation

Run the installation script:

```bash
./install.sh
```

Optionally, specify a subfolder within `~/.config/kitty/`:

```bash
./install.sh kittens
```

This places the kitten in the specified subfolder and updates the configuration.

### Manual Installation

1. Copy `url_select.py` to `~/.config/kitty/` (or a subfolder).

2. Add the keybinding to `~/.config/kitty/kitty.conf`:

   ```conf
   map kitty_mod+/ kitten url_select.py
   ```

   Adjust the path if using a subfolder.

## Configuration

To change the keybinding, edit `~/.config/kitty/kitty.conf`. For example:

```conf
map ctrl+shift+u kitten url_select.py
```

## Troubleshooting

- Ensure fzf is installed
- Check that terminal output contains URLs
- Verify default browser settings

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

