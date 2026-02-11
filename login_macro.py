"""
MkDocs Macros hook – reads resources/login.yaml at build time
and exposes VPN seat data to Jinja2 templates.

Credentials live in login.yaml (gitignored) and are injected
into the rendered site only; they never appear in the markdown source.
"""

import base64
import os
import re
import yaml


def define_env(env):
    """Load seat data from resources/login.yaml and register as a template variable."""

    login_file = os.path.join(os.path.dirname(__file__), "resources", "login.yaml")

    seats = []
    speakers = []

    if not os.path.exists(login_file):
        env.variables["seats"] = seats
        env.variables["speakers"] = speakers
        return

    with open(login_file, "r") as f:
        data = yaml.safe_load(f)

    if not data:
        env.variables["seats"] = seats
        env.variables["speakers"] = speakers
        return

    def _openconnect_cmd(username, password, address):
        """Build openconnect one-liner (base64 password)."""
        b64 = base64.b64encode((password or "").encode()).decode()
        return f"echo {b64} | base64 -d | sudo openconnect --user {username} --passwd-on-stdin {address}"

    def _openconnect_script(username, password, address):
        """Build a short script so users paste into a file and run with bash (avoids bracketed-paste in shell)."""
        one_liner = _openconnect_cmd(username, password, address)
        return f"#!/bin/bash\n{one_liner}\n"

    for entry in data:
        for name, info in entry.items():
            if "-seat" in name:
                # Extract seat number from e.g. "devwks-2618-ws1-seat12"
                match = re.search(r"seat(\d+)$", name)
                seat_num = int(match.group(1)) if match else 0
                addr = info.get("vpn_address", "")
                user = info.get("vpn_username", "")
                pwd = info.get("vpn_password", "")
                seats.append(
                    {
                        "num": seat_num,
                        "name": name,
                        "vpn_address": addr,
                        "vpn_password": pwd,
                        "vpn_username": user,
                        "openconnect_cmd": _openconnect_cmd(user, pwd, addr),
                        "openconnect_script": _openconnect_script(user, pwd, addr),
                    }
                )
            elif "-speaker" in name:
                match = re.search(r"speaker(\d+)$", name)
                spk_num = int(match.group(1)) if match else 0
                addr = info.get("vpn_address", "")
                user = info.get("vpn_username", "")
                pwd = info.get("vpn_password", "")
                speakers.append(
                    {
                        "num": spk_num,
                        "name": name,
                        "vpn_address": addr,
                        "vpn_password": pwd,
                        "vpn_username": user,
                        "openconnect_cmd": _openconnect_cmd(user, pwd, addr),
                        "openconnect_script": _openconnect_script(user, pwd, addr),
                    }
                )

    seats.sort(key=lambda s: s["num"])
    speakers.sort(key=lambda s: s["num"])

    env.variables["seats"] = seats
    env.variables["speakers"] = speakers
