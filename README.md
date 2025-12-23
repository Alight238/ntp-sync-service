# NTP Sync Service
**Course project for OS Security - user-13-63**

## Description
Systemd service for automatic NTP time synchronization with logging.

## Requirements
- Fedora/RHEL/Rocky Linux
- chrony
- sudo

## Installation
```bash
# Build RPM package
rpmbuild -ba rpmbuild/SPECS/ntp-sync-service.spec --define "_topdir $(pwd)/rpmbuild"

# Create local repository
sudo mkdir -p /var/local/repo
sudo cp rpmbuild/RPMS/noarch/*.rpm /var/local/repo/
sudo createrepo_c /var/local/repo

# Add repository
echo "[myrepo]
name=My Repository
baseurl=file:///var/local/repo
enabled=1
gpgcheck=0" | sudo tee /etc/yum.repos.d/myrepo.repo

# Install package
sudo dnf install -y ntp-sync-service
