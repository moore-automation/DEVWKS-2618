# Getting Started - Connectivity & Access

This workshop is going to be focused on the [NSO Reservable Sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/nso-sandbox_nso){:target="_blank"} .

Connectivity to the lab will be via Cisco Secure Client to an instance specific to your seat number.

## VPN Connectivity

You can find the connection details to connect to the VPN for your seat below. You will need to use the Cisco Secure Client to connect to the VPN.

The VPN Username is provided in the presentation.

## VPN Credentials

<table>
  <thead>
    <tr>
      <th>Pod Name</th>
      <th>VPN Address</th>
      <th>VPN Password</th>
    </tr>
  </thead>
  <tbody>
{% for seat in seats %}
    <tr>
      <td>seat-{{ seat.num }}</td>
      <td><button class="copy-btn" onclick="copyToClipboard(this)">{{ seat.vpn_address }}</button></td>
      <td><button class="copy-btn" onclick="copyToClipboard(this)">{{ seat.vpn_password }}</button></td>
    </tr>
{% endfor %}
  </tbody>
</table>

<script>
function copyToClipboard(btn) {
  const text = btn.textContent;
  navigator.clipboard.writeText(text);
  btn.textContent = "Copied!";
  setTimeout(() => btn.textContent = btn.getAttribute('data-original'), 1000);
}
// Store original text for each button
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
