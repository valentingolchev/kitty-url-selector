#!/usr/bin/env python3

from typing import List, Optional

import json
import re
import subprocess
import sys
import os
from datetime import datetime


def log_message(message, log_filename="my_log.txt"):
    home_dir = os.path.expanduser("~")
    log_path = os.path.join(home_dir, log_filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}\n\n"

    with open(log_path, "a") as log_file:
        log_file.write(full_message)


def get_visible_kitty_text(window_id):
    try:
        proc = subprocess.Popen(
            ["kitty", "@", "get-text", "--match", f"id:{window_id}"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=None,  # Let stderr go to terminal
            text=True
        )
        stdout, _ = proc.communicate()
        return stdout
    except subprocess.CalledProcessError:
        return None


def extract_urls(text: str) -> List[str]:
    # Basic URL-matching regex
    url_pattern = re.compile(r'''(
        (?:
            https?:// |
            ftp:// |
            news:// |
            git:// |
            mailto: |
            file:// |
            www\.
        )
        [\w\-@;/?:&=%\$_.+!*\x27(),~#\x1b\[\]]+
        [\w\-@;/?&=%\$_+!*\x27(~]
    )''', re.VERBOSE)
    urls = url_pattern.findall(text)
    return set([url.rstrip('\'"') for url in urls])


def fzf_select(prompt: str, choices: List[str]) -> str:
    if not choices:
        return None

    fzf = subprocess.Popen(
        ["fzf", f"--prompt={prompt}"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=None,  # Let stderr go to terminal
        text=True
    )
    stdout, _ = fzf.communicate("\n".join(choices))
    if fzf.returncode == 0 and stdout.strip():
        selected_line = stdout.strip()
        return selected_line

    return None


def get_all_windows():
    result = subprocess.run(
        ["kitty", "@", "ls"],
        stdout=subprocess.PIPE,
        text=True
    )
    return json.loads(result.stdout)


def get_active_window():
    windows = get_all_windows()
    for os_window in windows:
        for tab in os_window["tabs"]:
            if tab["is_active"] and tab["is_focused"]:
                for w in tab["windows"]:
                    if w["is_self"] or w["at_prompt"] or w["in_alternate_screen"]:
                        return w["id"]
    return None


def open_url(url):
    if sys.platform.startswith('darwin'):
        subprocess.run(
            ["open", url],
            stdout=subprocess.DEVNULL,
        )
    elif sys.platform.startswith('win'):
        os.startfile(url)
    else:
        subprocess.run(
            ["xdg-open", url],
            stdout=subprocess.DEVNULL,
        )


def main(args: List[str]) -> str:
    window_id = get_active_window()
    text = get_visible_kitty_text(window_id)
    urls = extract_urls(text)
    if not urls:
        return None

    selected_url = fzf_select("Select URL: ", urls)
    if not selected_url:
        return None

    open_url(selected_url)


def handle_result(args: List[str],
                  url: Optional[str],
                  target_window_id: int,
                  boss) -> None:
    pass


if __name__ == "__main__":
    main([])
