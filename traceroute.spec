Name:               traceroute
Epoch:              3
Version:            2.1.1
Release:            1
Summary:            A new modern implementation of traceroute(8) utility for Linux systems
License:            GPLv2+
URL:                http://traceroute.sourceforge.net/
Source0:            https://udomain.dl.sourceforge.net/project/traceroute/traceroute/traceroute-2.1.1/traceroute-2.1.1.tar.gz

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
%license COPYING
/bin/*
%{_bindir}/*

%files help
%defattr(-,root,root)
%doc README TODO CREDITS
%{_mandir}/*/*

%changelog
* Thu Feb 2 2023 Cao Jingbo <caojb@chinatelecom.cn> - 3:2.1.1-1
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:Update to version 2.1.1

* Tue Sep 8 2020 lunankun <lunankun@huawei.com> - 2.1.0-11
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:change source0 url

* Sat Oct 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.1.0-10
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:change the directory of the license file

* Fri Sep 06 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.1.0-9
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: rebuilt spec, add help package.

* Tue Aug 13 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.1.0-8
- Package init

