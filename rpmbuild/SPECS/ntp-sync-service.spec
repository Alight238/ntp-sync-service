Name:           ntp-sync-service
Version:        1.0
Release:        1
Summary:        NTP Time Synchronization Service

License:        GPLv3+
URL:            https://github.com/Alight238/ntp-sync-service
Source0:        %{name}-%{version}.tar.gz

Requires:       chrony
Requires:       sudo

BuildArch:      noarch

%description
NTP time synchronization service with logging.
Course project for OS Security.

%prep
%setup -q

%build
# Nothing to build

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/systemd/system
mkdir -p %{buildroot}/etc/sudoers.d

install -m 755 ntp-sync-service-1.0/ntp-sync-service.sh %{buildroot}/usr/local/bin/
install -m 644 ntp-sync-service-1.0/ntp-sync-service.service %{buildroot}/etc/systemd/system/
install -m 440 ntp-sync-service-1.0/ntp-sync-sudoers %{buildroot}/etc/sudoers.d/ntp-sync-service

%files
/usr/local/bin/ntp-sync-service.sh
/etc/systemd/system/ntp-sync-service.service
/etc/sudoers.d/ntp-sync-service

%post
systemctl daemon-reload

%preun
if [ $1 -eq 0 ]; then
    systemctl stop ntp-sync-service.service 2>/dev/null || :
    systemctl disable ntp-sync-service.service 2>/dev/null || :
fi

%changelog
* Tue Dec 23 2025 user-13-63 <user-13-63@localhost> - 1.0-1
- Initial package for course project
