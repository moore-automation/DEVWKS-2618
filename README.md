# DEVWKS-2618: Keeping Compliant with Open-Source Automation and NSO

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Workshop Overview

This hands-on workshop explores how to integrate Cisco Network Services Orchestrator (NSO) into a CI/CD pipeline to manage network services efficiently. Learn how to leverage open-source testing and automation tools to improve the quality and reliability of network deployments through thorough testing and version control.

**Duration:** ~45 minutes

## What You'll Learn

* **CI/CD Fundamentals** - Understand Continuous Integration and Continuous Deployment concepts
* **NSO Integration** - Integrate NSO with GitLab CI/CD pipelines  
* **Automated Testing** - Implement automated tests using Robot Framework and pyATS
* **Compliance Reporting** - Leverage NSO compliance reporting for configuration validation
* **DevOps Best Practices** - Apply modern DevOps practices to network automation

## Prerequisites

- Basic understanding of network configuration (Cisco IOS/IOS-XE)
- Familiarity with CLI operations
- Access to DevNet Sandbox or NSO instance
- VPN client (Cisco Secure Client)

## Lab Topology

The workshop uses a dCloud environment with:

- **Development NSO** (`10.10.20.47`) - Testing environment for validation
- **Production NSO** (`10.10.20.48`) - Production deployment target
- **DevBox** - Linux VM for service development and testing
- **DevTools** - Linux VM with GitLab and automation tools
- **CML Environments** - Two Cisco Modeling Labs instances (test and production)

## Getting Started

### Option 1: Using Make (Recommended)

```bash
# Clone the repository
git clone https://github.com/moore-automation/DEVWKS-2618.git
cd DEVWKS-2618

# Install dependencies
make install

# Start the development server
make serve

# Open your browser to http://localhost:8000
```

### Option 2: Manual Setup

```bash
# Clone the repository
git clone https://github.com/moore-automation/DEVWKS-2618.git
cd DEVWKS-2618

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start MkDocs server
mkdocs serve
```

## Makefile Commands

| Command | Description |
|---------|-------------|
| `make help` | Display available commands |
| `make install` | Set up Python virtual environment and install dependencies |
| `make serve` | Start local development server at http://localhost:8000 |
| `make build` | Build static site to `site/` directory |
| `make clean` | Remove built files and Python cache |
| `make clean-all` | Remove everything including virtual environment |

## Workshop Structure

1. **Get Connected** - Access the sandbox environment
2. **Create CI/CD Pipeline** - Define GitLab pipeline stages and jobs
3. **Pipeline-Driven NSO Development** - Develop and test NSO services
4. **Pre-Checks** - Add automated validation and testing
5. **Service Deployment** - Apply services to network devices
6. **Compliance Reporting** - Validate configurations against policies

## Resources

The `resources/` folder contains:

- **Python scripts** - Automation scripts for NSO interactions
- **XML templates** - NSO service and device templates
- **Test files** - pyATS and validation scripts
- **Configuration files** - Lab environment configurations

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## Community

- [Code of Conduct](docs/CODE_OF_CONDUCT.md)
- [Security Policy](docs/SECURITY.md)

## Authors

- **Ed Moore** - [@moore-automation](https://github.com/moore-automation)
- **David Quezada**
- **Jorge Mira**

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Cisco DevNet for sandbox infrastructure
- NSO development community
- Cisco Live 2026 attendees

---

**Questions or Issues?**

- Open an [issue](https://github.com/moore-automation/DEVWKS-2618/issues)
- Visit [Cisco DevNet](https://developer.cisco.com)
- Join the NSO community discussions
