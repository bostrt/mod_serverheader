Summary:	   Provides Apache HTTPD directive allowing you to override Apache HTTPD's "Server" response header.
Name:        mod_serverheader
Version:     1.0
Release:     2
License:     ASL 2.0
Url:         https://github.com/bostrt/mod_serverheader

Source0:   https://github.com/bostrt/mod_serverheader/archive/%{version}.tar.gz
Source1:   mod_serverheader.conf
Source2:   00-serverheader.conf

BuildRequires: httpd-devel

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
* Mon Mar 27 2017 Robert Bost 1.0-2
- Initial addition of changelog (bostrt@gmail.com)
