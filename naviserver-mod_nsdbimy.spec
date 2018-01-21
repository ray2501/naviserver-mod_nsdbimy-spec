#
# spec file for package naviserver nsdbimy module
#

Summary:        NaviServer nsdbimy module
Name:           naviserver-mod_nsdbimy
Version:        0.2
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsdbimy
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
BuildRequires:  naviserver-mod_nsdbi
BuildRequires:  naviserver-mod_nsdbi-devel
BuildRequires:  libmysqlclient-devel
Requires:       naviserver-mod_nsdbi
Requires:       naviserver
Source0:        %{name}-%{version}.tar.gz
Patch0:         nsdbimy.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the nsdbimy database driver. It connects a MySQL database
to a NaviServer web server using the nsdbi interface.

%prep
%setup -q %{name}-%{version}
%patch0

%build
make NAVISERVER=/var/lib/naviserver

%install
mkdir -p %buildroot/var/lib/naviserver/bin
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%post -n naviserver-mod_nsdbimy
/sbin/ldconfig

%postun -n naviserver-mod_nsdbimy
/sbin/ldconfig

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/bin/nsdbimy.so

%changelog

