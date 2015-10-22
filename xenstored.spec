Summary:	xenstored daemon
Name:		xenstored
Version:	1.9.9
Release:	21%{?dist}
License:	GPLv2+
Group:		System/Hypervisor
Source:		%{name}-%{version}.tar.gz
URL:		https://github.com/jjd27/ocaml-xenstore-server
BuildRequires:	systemd-units

%description
xenstore daemon

%prep
%autosetup -n ocaml-xenstore-server

%build
make %{?_smp_mflags}

%install
install -m 755 -d %{buildroot}/%{_sbindir}
install -m 755 _build/userspace/main.native %{buildroot}/%{_sbindir}/xenstored-v3
install -m 755 -d %{buildroot}/%{_unitdir}
install -m 644 xenstored.service %{buildroot}/%{_unitdir}

%files
%{_sbindir}/xenstored-v3
%{_unitdir}/xenstored.service

%changelog
* Thu Oct 22 2015 Jonathan Davies <jonathan.davies@citrix.com> - 1.9.9
- Rebuilt
