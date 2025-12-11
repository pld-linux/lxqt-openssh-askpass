#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Askpass openssh transition dialog for LXQt desktop suite
Summary(pl.UTF-8):	Okno dialogowe pytania o hasło OpenSSH dla środowiska graficznego LXQt
Name:		lxqt-openssh-askpass
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-openssh-askpass/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	e337d2687c9f1cb77c617914f0ed6d09
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Askpass openssh transition dialog for LXQt desktop suite.

%description -l pl.UTF-8
Okno dialogowe pytania o hasło OpenSSH dla środowiska graficznego
LXQt.

%prep
%setup -q

%build
%cmake  -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-openssh-askpass
%{_mandir}/man1/lxqt-openssh-askpass.1*
%dir %{_datadir}/lxqt/translations/%{name}
