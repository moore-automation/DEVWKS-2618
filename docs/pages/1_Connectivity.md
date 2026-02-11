# Getting Started - Connectivity & Access

This workshop is going to be focused on the [NSO Reservable Sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/nso-sandbox_nso){:target="_blank"} .

Connectivity to the lab will be via Cisco Secure Client (or OpenConnect on Linux) to an instance specific to your seat number.

## VPN Connectivity

You can find the connection details to connect to the VPN for your seat below. Use the **Cisco Secure Client** to connect on Windows/macOS. On **Linux**, if Secure Client causes issues (for example with resolv.conf), use **OpenConnect** instead: click **Copy OpenConnect script**, paste into a new file (e.g. `vpn.sh`), then run `bash vpn.sh`. (Pasting the command directly into the terminal can break on some setups because of bracketed paste; pasting into a file and running it avoids that.)

The VPN Username is provided in the presentation.

## VPN Credentials

<table>
  <thead>
    <tr>
      <th>Pod Name</th>
      <th>VPN Address</th>
      <th>VPN Password</th>
      <th>OpenConnect (Linux)</th>
    </tr>
  </thead>
  <tbody>
{% for seat in seats %}
    <tr>
      <td>seat-{{ seat.num }}</td>
      <td><button class="copy-btn" onclick="copyToClipboard(this)">{{ seat.vpn_address }}</button></td>
      <td><button class="copy-btn" onclick="copyToClipboard(this)">{{ seat.vpn_password }}</button></td>
      <td><button class="copy-btn copy-cmd-btn" onclick="copyToClipboard(this)" data-copy="{{ seat.openconnect_script }}">Copy OpenConnect script</button></td>
    </tr>
{% endfor %}
  </tbody>
</table>

### Linux: DNS / resolv.conf after VPN is up

If DNS resolution fails once the VPN is connected (e.g. `resolv.conf` was reset), run the following in your terminal. Copy the command, then press **e** and **Tab** to autocomplete the ethernet interface name, followed by `~`.

<button class="copy-btn" onclick="copyToClipboard(this)" data-copy="sudo resolvectl domain ">Copy command</button>

<script>
function copyToClipboard(btn) {
  const text = btn.getAttribute('data-copy') || btn.textContent;
  navigator.clipboard.writeText(text);
  const orig = btn.getAttribute('data-original');
  btn.textContent = "Copied!";
  setTimeout(() => { btn.textContent = orig; }, 1000);
}
// Store original label for each button (so "Copied!" can be restored)
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.setAttribute('data-original', btn.textContent);
  });
});
</script>

<style>
.copy-btn {
  font-size: 0.95em;
  margin-left: 0;
  cursor: pointer;
  background: none;
  border: none;
  color: #0078d4;
  text-decoration: underline;
  padding: 0;
}
td {
  position: relative;
}
</style>

---
