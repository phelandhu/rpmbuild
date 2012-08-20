Name:		R66T-Node.js
Version:	1
Release:	1
Summary:	The Root66 Node.js installation

Group:		R66T
License:	GPL
URL:		repo.r66t.com
Source0:	r66t-node.js-1.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#ExclusiveArch:	x86_64

%description
The Root66 Node.js installation.
Necessary for some hipster thing Jer is doing

%prep
%setup -q


%build

%install
ln -sf usr/local/lib/node_modules/npm/bin/npm-cli.js usr/local/bin/npm
#bash "/usr/local/lib/node_modules/npm/scripts/relocate.sh" /usr/local/bin/node

%clean
#rm -rf %{buildroot}


%files -f fileList.txt
%defattr(-,root,root,-)
%doc



%changelog

