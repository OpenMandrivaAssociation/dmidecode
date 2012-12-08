Summary:	Tool for dumping a computer's DMI table contents
Name:		dmidecode
Version:	2.11
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.nongnu.org/dmidecode/
Source0:	http://download.savannah.gnu.org/releases/dmidecode/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	drakxtools-backend <= 10.3-0.64mdk

%description
Dmidecode is a tool for dumping a computer's DMI (some say SMBIOS) table
contents in a human-readable format. This table contains a description of the
system's hardware components, as well as other useful pieces of information
such as serial numbers and BIOS revision. Part of its code can be found in
the Linux kernel, because DMI data may be used to enable or disable specific
portions of code depending on the hardware vendor. Thus, dmidecode is mainly
used to detect system "signatures" and add them to the kernel source code
when needed.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}"

%install
rm -rf %{buildroot}
%{makeinstall_std} prefix=%{_prefix} mandir=%{_mandir}
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE AUTHORS CHANGELOG
%{_sbindir}/*
%{_mandir}/man8/*


%changelog
* Mon May 30 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.11-1mdv2011.0
+ Revision: 681984
- spec file clean
- drop patch 0
- update to new version 2.11
- update url for Source0

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.10-5
+ Revision: 663785
- mass rebuild

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 2.10-4mdv2011.0
+ Revision: 623261
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.10-3mdv2010.1
+ Revision: 522482
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.10-2mdv2010.0
+ Revision: 413361
- rebuild

* Mon Nov 24 2008 Funda Wang <fwang@mandriva.org> 2.10-1mdv2009.1
+ Revision: 306340
- new version 2.10
- use compile flags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2.9-4mdv2009.0
+ Revision: 220667
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 2.9-3mdv2008.1
+ Revision: 149185
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 2.9-2mdv2008.0
+ Revision: 69362
- kill unused prereq


* Wed Mar 07 2007 Erwan Velu <erwan@mandriva.org> 2.9-1mdv2007.0
+ Revision: 134384
- 2.9

* Mon Jan 15 2007 Erwan Velu <erwan@mandriva.org> 2.8-1mdv2007.1
+ Revision: 109252
- Import dmidecode

* Mon Feb 27 2006 Erwan Velu <velu@seanodes.com> 2.8-1mdk 
- 2.8

* Fri Jan 20 2006 Pixel <pixel@mandriva.com> 2.7-2mdk
- output format has changed in 2.7, so conflict with MDV2006 drakxtools which doesn't parse it correctly

* Fri Oct 21 2005 Erwan Velu <velu@seanodes.com> 2.7-1mdk 
- 2.7

* Mon Mar 14 2005 Erwan Velu <velu@seanodes.com> 2.6-1mdk 
- 2.6

* Thu Dec 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.5-1mdk
- 2.5
- drop P0, override parameter in stead
- no bz2 ending in %%files for man pages

* Sat May 08 2004 Erwan Velu <erwan@mandrakesoft.com> 2.4-1mdk 
- new release 2.4
- moving man pages in /usr/share/man

* Sat May 08 2004 Michael Scherer <misc@mandrake.org> 2.3-3mdk 
- use macro
- do not own /usr/sbin/

