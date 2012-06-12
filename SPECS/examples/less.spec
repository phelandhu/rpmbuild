# Header Stanza begins here
#
# Short description
Summary: A text file browser similar to more, but better.
# the application name
Name: less
# the version of the application
Version: 444
# the packaging revision of this particular version
Release: 1
# this software is licensed under the GPL
License: GPL
# this software is an application used with text files
Group: Applications/Text
# this software source file; not the use of variables
Source: http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
# a shell script needed for use with less
Source1: lesspipe.sh
# script to change the environment when less is used in Bourne-compatible shells
Source2: less.sh
# script to change the environment when less is used in C shells
Source3: less.csh
# this software can be downloaded from the following location
URL: http://www.greenwoodsoftware.com/less/
# temporary dir where the software should be compiled
Buildroot: %{_tmppath}/%{name}-root
# non-obvious software required to build the software
BuildRequires: ncurses-devel
# long description
%description
The less utility is a text file browser that resembles more, but has
more capabilities. Less allows you to move backwards in the file as
well as forwards. Since less doesn't have to read the entire input file
before it starts, less starts up more quickly than text editors (for
example, vi).
You should install less because it is a basic utility for viewing text
files, and you'll use it frequently.
# Prep Stanza begins here
#
%prep
# unpack the source and cd into the source directory
%setup -q
# perform other needed setup
chmod -R a+w *
# Build Stanza begins here
#
%build
# less uses autoconf, so ./configure it w/ appropriate options
%configure
# compile the software
make CC="gcc $RPM_OPT_FLAGS -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOU
RCE -D_FILE_OFFSET_BITS=64" datadir=%{_docdir}
# Install Stanza begins here
#
%install
# as sanity protection, make sure the Buildroot is empty
rm -rf $RPM_BUILD_ROOT
# install software into the Buildroot
%makeinstall
strip -R .comment $RPM_BUILD_ROOT/usr/bin/less
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
install -c -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/bin/
install -c -m 755 %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
install -c -m 755 %{SOURCE3} $RPM_BUILD_ROOT/etc/profile.d
# define a clean-up script to run after the software in Buildroot is pkg'ed
%clean
# the actual script -- just delete all files within the Buildroot
rm -rf $RPM_BUILD_ROOT
# Files Stanza begins here
#
%files
# set perms and ownerships of packaged files
# the - indicates that the current permissions on the files should be used
%defattr(-,root,root)
# package all files within the $RPM_BUILD_ROOT/etc/profile.d directory
/etc/profile.d/*
# package all files within the $RPM_BUILD_ROOT/usr/bin directory
/usr/bin/*
# package all files within the $RPM_BUILD_ROOT/usr/share/man/man1 directory
%{_mandir}/man1/*
# Scripts Stanza begin here
#
# No Scripts in this RPM
# Changelog begins here
#
%changelog




