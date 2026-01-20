# NSO Automation Scripts

Workshop resources for **DEVWKS-2618: NSO CI/CD Pipeline Automation**

## 📁 Contents

### Python Scripts

- **`apply.py`** - Apply loopback service configuration to NSO devices
- **`compliance.py`** - Generate and run compliance reports
- **`loopback-test.py`** - Automated testing using pyATS/AETest framework

### Configuration Files

- **`environments.yml`** - GitLab CI/CD environment variables
- **`loopback-template.xml`** - NSO service template (IOS/IOS-XR)
- **`requirements.txt`** - Python dependencies

---

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export NSO_DEV_IP=10.10.20.47
export NSO_DEV_USER=developer
export NSO_DEV_PWD=C1sco12345
```

---

## 📖 Usage

### Apply Service

Apply a loopback interface configuration to a device:

```bash
python apply.py \
  --nso_url http://10.10.20.47:8080 \
  --device dev-dist-rtr01 \
  --username developer \
  --password C1sco12345 \
  --loopback_intf 1166 \
  --ip_address 10.100.66.1
```

**Options:**
- `--nso_url`: NSO server URL (default: http://localhost:8080)
- `--device`: Target device name
- `--username`: NSO username
- `--password`: NSO password
- `--loopback_intf`: Loopback interface number (default: 1166)
- `--ip_address`: IP address for loopback (default: 10.100.66.1)

---

### Compliance Reports

Generate and run compliance reports:

```bash
python compliance.py \
  --nso_url http://10.10.20.47:8080 \
  --username developer \
  --password C1sco12345 \
  --device dev-dist-rtr01 \
  --report_name Loopback_report \
  --outformat html
```

**Options:**
- `--nso_url`: NSO server URL
- `--username`: NSO username
- `--password`: NSO password
- `--device`: Device to check (default: dev-dist-rtr01)
- `--report_name`: Compliance report name (default: Loopback_report)
- `--outformat`: Output format - html, text, or xml (default: html)

---

### Automated Testing

Run integration tests using pyATS framework:

```bash
# Test IOS-XR device
python loopback-test.py \
  --nso_url http://10.10.20.47:8080 \
  --device dev-core-rtr01 \
  --username developer \
  --password C1sco12345

# Test IOS device
python loopback-test.py \
  --nso_url http://10.10.20.47:8080 \
  --device dev-dist-rtr01 \
  --username developer \
  --password C1sco12345
```

**Test Flow:**
1. Sync configuration from device to NSO
2. Apply loopback service
3. Delete loopback service
4. Exit with code 0 (success) or 1 (failure)

**Exit Codes:**
- `0` - All tests passed ✅
- `1` - One or more tests failed ❌

---

## 🔧 Features

### Reliability
- **Automatic retry logic** in apply.py (3 retries with exponential backoff)
- **Robust error handling** with clear error messages
- **Timeout protection** (10-15 second timeouts)

### Testing
- **pyATS integration** for structured test reporting
- **Step-by-step validation** with detailed logs
- **Proper exit codes** for CI/CD integration

### Security
- **SSL verification disabled** for demo environments
- **Environment variable support** for credentials
- **Demo-friendly defaults** for workshop use

---

## 🏗️ CI/CD Integration

These scripts are designed to work with GitLab CI/CD pipelines:

### GitLab Pipeline Usage

```yaml
test-loopback-service:
  stage: test
  script:
    - cd nso_cicd/tests/loopback-test
    - python loopback-test.py --nso_url "http://$NSO_DEV_IP:8080" --device "dev-core-rtr01" --username "$NSO_DEV_USER" --password "$NSO_DEV_PWD"
```

### Environment Variables

Set these in GitLab CI/CD → Settings → Variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `NSO_DEV_IP` | Dev NSO server IP | 10.10.20.47 |
| `NSO_PROD_IP` | Prod NSO server IP | 10.10.20.48 |
| `NSO_DEV_USER` | NSO username | developer |
| `NSO_DEV_PWD` | NSO password | (masked) |
| `NSO_PROD_PWD` | Prod NSO password | (masked) |

---

## 📝 Notes

- Scripts use HTTP (not HTTPS) for demo simplicity
- SSL warnings are suppressed for self-signed certificates
- Default passwords are included for workshop convenience
- Designed for Cisco DevNet Sandbox environments

---

## 🐛 Troubleshooting

### Connection Refused
```
Error connecting to NSO: HTTPConnectionPool
```
**Solution:** Verify NSO server is running and IP address is correct

### Authentication Failed
```
Failed to apply service: 401
```
**Solution:** Check username and password

### Service Already Exists
```
Failed to apply service: 409
```
**Solution:** Delete existing service first or use a different service name

---

## 📚 Additional Resources

- [NSO Documentation](https://developer.cisco.com/docs/nso/)
- [pyATS Documentation](https://developer.cisco.com/docs/pyats/)
- [Workshop Lab Guide](../docs/)

---

## 👥 Support

For workshop support, contact your instructor or visit the DevNet Community.
