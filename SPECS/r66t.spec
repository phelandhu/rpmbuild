Summary: R66T demo Traffic light package
Name: r66t_demo
Version: 1
Release: 1
Source0: r66t-1.tar.gz
License: GPL
Group: MyJunk
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires:      PyXML >= 0.8.3
Requires:      make > 1.3.5
Requires:      gcc > 4.3.1

%description
Make some relevant package description here

%prep
%setup -q

%build

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -m 0755 -d $RPM_BUILD_ROOT/opt/r66t
install -m 0755 myscript.sh $RPM_BUILD_ROOT/opt/r66t/myscript.sh
install -m 0755 -d $RPM_BUILD_ROOT/opt/r66t/src
install -m 0755 -d $RPM_BUILD_ROOT/opt/r66t/bin

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "This will display after rpm installs the package!"

%files
%dir /opt/r66t/
%dir /opt/r66t/bin/
%dir /opt/r66t/src/
/opt/r66t/myscript.sh
/opt/r66t/bin/hello
/opt/r66t/bin/README
/opt/r66t/bin/bytesize
/opt/r66t/src/weight.c
/opt/r66t/src/sort.c
/opt/r66t/src/hello.c
/opt/r66t/src/bytesixe.c
/opt/r66t/src/README
/opt/r66t/README
