%define version 1.6.2.16
%define fversion 1.6.2
%define release %mkrel 4


Summary:   Installations tracker
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




%changelog
* Tue Dec 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.2.16-4mdv2012.0
+ Revision: 738144
- rebuild
- update patch 3
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.2.16-2mdv2011.0
+ Revision: 610134
- rebuild

* Fri Jan 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.2.16-1mdv2010.1
+ Revision: 498052
- new version 1.6.2
- update patch 3 for the new glibc
- add Debian patch to make installwatch build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jan 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.2.16-0.3mdv2009.1
+ Revision: 334790
- patch for rpm's new way to set the build root
- update paths, arch and man page compression in patch 0

* Mon Jan 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.2.16-0.2mdv2009.1
+ Revision: 333703
- fix glibc detection
- new git snapshot
- update patch 0
- drop patch 1

* Mon Jan 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.1-7mdv2009.1
+ Revision: 333662
- remove some broken rpm version tests
- update license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.6.1-6mdv2009.0
+ Revision: 243862
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.1-4mdv2008.1
+ Revision: 99075
- fix path to installwatch.so

* Mon Oct 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.1-3mdv2008.1
+ Revision: 98371
- replace remaining /usr/lib on 64 bit, fixing bug #34775

* Wed Apr 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.1-3mdv2008.0
+ Revision: 14740
- fix for x86_64


* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.1-2mdv2007.0
+ Revision: 87354
- fix build on 64 bit
- Import checkinstall

* Fri Nov 24 2006 Götz Waschk <waschk@mandriva.org> 1.6.1-1mdv2007.1
- drop patch 1
- New version 1.6.1

* Fri Jul 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.6.0-1mdv2007.0
- Rebuild

* Mon Feb 13 2006 Götz Waschk <waschk@mandriva.org> 1.6.0-2mdk
- fix bug #21100 (switched options), thanks to danxuliu)

* Fri Aug 12 2005 Götz Waschk <waschk@mandriva.org> 1.6.0-1mdk
- rediff patch, it was partitially merged
- new version

* Tue Aug 09 2005 Götz Waschk <waschk@mandriva.org> 1.6.0-0.beta4.3mdk
- update patch to fix bug 16848 (thanks to sieczka)

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 1.6.0-0.beta4.2mdk
- update patch 0 to fix bug 16110 (thanks to Jan Ciger)

* Thu Dec 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.6.0-0.beta4.1mdk
- update patch 0
- new version

* Mon Jun 21 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.6.0-0.beta3.2mdk
- require rpm-build

* Tue May 04 2004 Götz Waschk <waschk@linux-mandrake.com> 1.6.0-0.beta3.1mdk
- rediff patch
- new version

