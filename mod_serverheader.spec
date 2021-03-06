Summary:	   Provides Apache HTTPD directive allowing you to override Apache HTTPD's "Server" response header.
Name:        mod_serverheader
Version:     1.0.5
Release:     3
License:     ASL 2.0
Url:         https://github.com/bostrt/mod_serverheader

Source0:   https://github.com/bostrt/mod_serverheader/archive/%{version}.tar.gz
Source1:   mod_serverheader.conf
Source2:   00-serverheader.conf

BuildRequires: httpd-devel
BuildRequires: gcc

Requires: httpd

%description
This directive allows you to override Apache HTTPD's Server response header. In
addition to configuring this directive, you may also need to modify your 
ServerTokens directive to allow for a longer value to be used.

%prep
%setup -q -n %{name}-%{version}

%build
apxs -c mod_serverheader.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/httpd/modules
cp .libs/mod_serverheader.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_serverheader.so
install -Dp -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/mod_serverheader.conf
install -Dp -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.modules.d/00-serverheader.conf

%files
%defattr(-,root,root)
%{_libdir}/httpd/modules/mod_serverheader.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_serverheader.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.modules.d/00-serverheader.conf
%doc README.md

%changelog
* Fri Jul 31 2020 Robert Bost 1.0.5-3
- Reordering changelog to appease copr
- error: %changelog not in descending chronological order
* Thu Jul 30 2020 Robert Bost 1.0.5-1
- Fix RPM versioning
* Mon Mar 27 2017 Robert Bost 1.0-2
- Initial addition of changelog (bostrt@gmail.com)
