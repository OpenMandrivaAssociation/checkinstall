%define debug_package %{nil}

%define fversion 1.6.2

Summary:   CheckInstall installations tracker
Name:      checkinstall
Version:   1.6.2.16
Release:   11
License:   GPLv2+
Group:     System/Configuration/Packaging
#gw git snapshot
Source:    http://checkinstall.izto.org/files/source/%{name}-%{fversion}.tar.gz
Patch0:    checkinstall-mdv-fix-paths.patch
Patch2:    checkinstall-1.6.1-rpm-version-check.patch
Patch3:    installwatch-glibc_minor.patch
Patch4:    checkinstall-mdv-rpm-set-buildroot.patch
#gw from Debian, build with new glibc
Patch5:    checkinstall-1.6.1-deb-mdv-build-with-new-glibc.patch
Url:       https://asic-linux.com.mx/~izto/checkinstall/
Requires:  rpm-build

%description
CheckInstall keeps track of all the files created or modified by your 
installation script ("make install" "make install_modules", "setup", etc),
builds a standard binary package and installs it in your system giving
you the ability to uninstall it with your distribution's standard 
package management utilities. 


%prep
%setup -q -n %{name}-%{fversion}
%patch0 -p1 -b .mdv
%patch2 -p0
%patch3 -p0 -b .glibc
%patch4 -p1 -b .buildroot
ln -s installwatch installwatch-0.7.0beta5
%patch5 -p1

%build
%make

%install
install -D -m 755 checkinstall %{buildroot}/%{_bindir}/checkinstall
install -D -m 755 makepak %{buildroot}/%{_sbindir}/makepak
install -m 755 installwatch/installwatch %{buildroot}/%{_bindir}
install -D -m 755 installwatch/installwatch.so %{buildroot}/%{_libdir}/checkinstall/installwatch.so
install -m 755 checkinstallrc-dist %{buildroot}/%{_libdir}/checkinstall/checkinstallrc
install -D -m 644 locale/checkinstall-es.mo %{buildroot}%{_libdir}/checkinstall/locale/es/LC_MESSAGES/checkinstall.mo
perl -pi -e "s!#PREFIX#!%{_prefix}!" %{buildroot}%{_bindir}/installwatch
perl -pi -e "s!/lib/!/%{_lib}/!" %{buildroot}%{_bindir}/*

%files
%doc README RELNOTES BUGS TODO CREDITS
%{_bindir}/installwatch
%{_bindir}/checkinstall
%{_sbindir}/makepak
%dir %{_libdir}/checkinstall/
%{_libdir}/checkinstall/checkinstallrc
%{_libdir}/checkinstall/installwatch.so
%lang(es) %{_libdir}/checkinstall/locale/es
%dir %{_libdir}/checkinstall/locale/
