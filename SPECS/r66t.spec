Summary: My first rpm script package
Name: r66t
Version: 1
Release: 1
Source0: r66t-1.tar.gz
License: GPL
Group: MyJunk
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
%description
Make some relevant package description here
%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/r66t
install -m 0755 myscript.sh $RPM_BUILD_ROOT/usr/r66t/myscript.sh
%clean
rm -rf $RPM_BUILD_ROOT
%post
echo " "
echo "This will display after rpm installs the package!"
%files
%dir /usr/r66t
/usr/r66t/myscript.sh
