Name:		privoxy-r66t
Version:	1
Release:	1%{?dist}
Summary:	The privoxy install customized for R66T

Group:		
License:	
URL:		
Source0:	privoxy-r66t-1.0.0.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	
Requires:	

%description
This is the R66T version of a privoxy installation.

At this point it is in test mode awaiting the test of validation process

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc



%changelog

