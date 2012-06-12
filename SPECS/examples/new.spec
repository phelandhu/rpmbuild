Name:           r66t
Version:        0.1.0
Release:        1%{?dist}
Summary:        The Node software for R66T and how we will serve the world, like man

Group:          Applications/Internet 
License:        We're not sharing
URL:            r66t.int/
Source0:        r66t.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:      PyXML >= 0.8.3
Requires:      make > 1.3.5
Requires:      gcc > 4.3.1 

%description
The base level installation package to get one of our nodes up and running

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
