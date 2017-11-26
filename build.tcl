#!/usr/bin/tclsh

set arch "x86_64"
set base "naviserver-mod_nsdbimy-0.2"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force nsdbimy.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsdbimy.spec]
exec >@stdout 2>@stderr {*}$buildit
