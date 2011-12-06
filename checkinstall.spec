%define version 1.6.2.16
%define fversion 1.6.2
%define release %mkrel 4


Summary:   CheckInstall installations tracker
Name:      checkinstall
Version:   %version
Release:   %release
License:   GPLv2+
Group:     System/Configuration/Packaging
#gw git snapshot
Source:    http://checkinstall.izto.org/files/source/%{name}-%{fversion}.tar.gz
Patch0:	   checkinstall-mdv.patch
Patch2:	   checkinstall-1.6.1-rpm-version-check.patch
Patch3:    checkinstall-fix-glibc-detection.patch
Patch4:    checkinstall-rpm-set-buildroot.patch
#gw from Debian, build with new glibc
Patch5:	   21build-glibc-2.10.diff
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://asic-linux.com.mx/~izto/checkinstall/
Provides: libcheckinstall1
Obsoletes: libcheckinstall1
Requires: rpm-build

%description
CheckInstall  keeps  track of all the files created  or
modified  by your installation  script  ("make install"
"make install_modules",  "setup",   etc),   builds    a 
standard   binary   package and  installs  it  in  your 
system giving you the ability to uninstall it with your 
distribution's  standard package management  utilities. 

%prep

%setup -q -n %name-%fversion
%patch0 -p1 -b .mdv
%patch2 -p0
%patch3 -p0 -b .glibc
%patch4 -p1 -b .buildroot
ln -s installwatch installwatch-0.7.0beta5
%patch5 -p1
%build
make

%install
rm -rf %buildroot
install -D -m 755 checkinstall %buildroot/%{_bindir}/checkinstall
install -D -m 755 makepak %buildroot/%{_sbindir}/makepak
install -m 755 installwatch/installwatch %buildroot/%{_bindir}
install -D -m 755 installwatch/installwatch.so %buildroot/%{_libdir}/checkinstall/installwatch.so
install -m 755 checkinstallrc-dist %buildroot/%{_libdir}/checkinstall/checkinstallrc
install -D -m 644 locale/checkinstall-es.mo %buildroot%_libdir/checkinstall/locale/es/LC_MESSAGES/checkinstall.mo
perl -pi -e "s!#PREFIX#!%_prefix!" %buildroot%_bindir/installwatch
perl -pi -e "s!/lib/!/%_lib/!" %buildroot%_bindir/*


%clean
rm -rf %buildroot

%files
%defattr(-,root,root,755)
%doc README INSTALL RELNOTES BUGS TODO CREDITS COPYING
%{_bindir}/installwatch
%{_bindir}/checkinstall
%{_sbindir}/makepak
%dir %{_libdir}/checkinstall/
%{_libdir}/checkinstall/checkinstallrc
%{_libdir}/checkinstall/installwatch.so
%lang(es) %{_libdir}/checkinstall/locale/es
%dir %{_libdir}/checkinstall/locale/


