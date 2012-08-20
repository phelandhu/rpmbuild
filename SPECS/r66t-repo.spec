Summary: The Root66 repo RPM
Name: R66T-Repo
Version: 1
Release: 1
Source0: r66t-repo-1.tar.gz
License: GPL
Group: R66T
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
%description
The R66T repository RPM. 
This will enable the repo to be installed on a machine simply by donwloading this RPM and then installing it.
%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 0644 R66T.repo $RPM_BUILD_ROOT/etc/yum.repos.d/R66T.repo
%clean
rm -rf $RPM_BUILD_ROOT
%post
echo " "
echo "This will display after rpm installs the package!"
%files
%dir /etc/yum.repos.d
/etc/yum.repos.d/R66T.repo
