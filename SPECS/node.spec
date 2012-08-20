Summary: My second rpm script package
Name: node
Version: 1
Release: 1
Source0: node-1.tar.gz
License: GPL
Group: MyJunk
BuildRoot: %{_tmppath}/%{name}-buildroot
%description
Make some relevant package description here
%prep
%setup -q
%pre
if [ `grep -c ^privoxy /etc/passwd` = "0" ]; then
useradd --system --uid 73 --shell /sbin/nologin --user-group --home-dir /usr/local/etc/privoxy privoxy
fi
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/r66t/bin
install -m 0755 -d $RPM_BUILD_ROOT/usr/mongoDB
install -m 0755 myscript.sh $RPM_BUILD_ROOT/usr/r66t/myscript.sh
install -m 0755 r66t/bin/bytesize $RPM_BUILD_ROOT/usr/r66t/bin/bytesize
install -m 0755 r66t/bin/hello $RPM_BUILD_ROOT/usr/r66t/bin/hello


%clean
rm -rf $RPM_BUILD_ROOT
%post
echo " "
echo "This will display after rpm installs the package!"
%files
%dir /usr/r66t/bin
%dir /usr/mongoDB
/usr/r66t/myscript.sh
/usr/r66t/bin/bytesize
/usr/r66t/bin/hello
