Name:               traceroute
Epoch:              3
Version:            2.1.0
Release:            9
Summary:            A new modern implementation of traceroute(8) utility for Linux systems
License:            GPLv2+
URL:                http://traceroute.sourceforge.net/
Source0:            https://sourceforge.net/projects/traceroute/files/traceroute/%{name}-%{version}/%{name}-%{version}.tar.gz

Provides:           tcptraceroute = 1.5-1
Obsoletes:          tcptraceroute < 1.5-1

BuildRequires:      gcc

%description
Traceroute tracks the route packets taken from an IP network on their way
to a given host. It utilizes the IP protocol's time to live (TTL) field
and attempts to elicit an ICMP TIME_EXCEEDED response from each gateway
along the path to the host.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
make  CFLAGS="$RPM_OPT_FLAGS"  LDFLAGS="$RPM_LD_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT/bin
install -m755 traceroute/traceroute $RPM_BUILD_ROOT/bin

pushd $RPM_BUILD_ROOT/bin
ln -s traceroute traceroute6
popd

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m755 wrappers/tcptraceroute $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m644 traceroute/traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8

pushd $RPM_BUILD_ROOT%{_mandir}/man8
ln -s traceroute.8 traceroute6.8
ln -s traceroute.8 tcptraceroute.8
popd

%files
%defattr(-,root,root)
%doc COPYING
/bin/*
%{_bindir}/*

%files help
%defattr(-,root,root)
%doc README TODO CREDITS
%{_mandir}/*/*

%changelog
* Fri Sep 06 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.1.0-9
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: rebuilt spec, add help package.

* Tue Aug 13 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.1.0-8
- Package init

