%define version 1.6.1
%define fversion %version
%define release %mkrel 2
%define iwver 0.7.0beta5

Summary:   CheckInstall installations tracker
Name:      checkinstall
Version:   %version
Release:   %release
License:   GPL
Group:     System/Configuration/Packaging
Source:    http://checkinstall.izto.org/files/source/%{name}-%{fversion}.tar.bz2
Patch0:	   checkinstall-1.6.0-mdk.patch
Patch1:    checkinstall-1.6.1-64bit.patch
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
ln -s installwatch-%iwver installwatch-0.7.0beta4
%patch0 -p1 -b .mdv
%patch1 -p1 -b .64bit

%build
make

%install
rm -rf %buildroot
install -D -m 755 checkinstall %buildroot/%{_bindir}/checkinstall
install -D -m 755 makepak %buildroot/%{_sbindir}/makepak
install -m 755 installwatch-%iwver/installwatch %buildroot/%{_bindir}
install -D -m 755 installwatch-%iwver/installwatch.so %buildroot/%{_libdir}/checkinstall/installwatch.so
install -m 755 checkinstallrc-dist %buildroot/%{_libdir}/checkinstall/checkinstallrc
install -D -m 644 locale/checkinstall-es.mo %buildroot%_libdir/checkinstall/locale/es/LC_MESSAGES/checkinstall.mo
perl -pi -e "s!#PREFIX#!%_prefix!" %buildroot%_bindir/installwatch

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


