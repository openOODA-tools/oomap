Name:           oomap
Version:        0.1.0
Release:        1%{?dist}
Summary:        Applies transformation expressions to each object in a pipeline stream.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomap
Source0:        oomap-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomap is a sovereign, capability-bounded STREAM MAPPER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomap
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomap-uninstall

%files
/usr/bin/oomap
/usr/bin/oomap-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
