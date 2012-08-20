# FILE: ~/rpmbuild/SPECS/dirsplit.spec

Summary:    dirsplit utility
Name:       dirsplit
Version:    1.1.11
Release:    1%{?dist}
SOURCE0:    dirsplit-%{version}.tar.gz
 
Requires:   perl >= 4:5.8.1
License:    GPLv2
Group:      Applications/System
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-buildroot
 
%description -n dirsplit
dirsplit
 
%prep
%setup -q
 
%build
 
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cp -R * $RPM_BUILD_ROOT/.
 
%clean
rm -rf $RPM_BUILD_ROOT
 
%files -n dirsplit
%defattr(-,root,root)
%{_bindir}/dirsplit
%{_mandir}/man1/dirsplit.*
 
%changelog
* Tue Feb 21 2012 Sam Mingolelli <rpms@lamolabs.org> - 1.1.11-1
- Initial creation
 
# vim: ts=2 nolist :
