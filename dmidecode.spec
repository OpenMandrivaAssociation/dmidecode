Summary:	Tool for dumping a computer's DMI table contents
Name:		dmidecode
Version:	2.12
Release:	6
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.nongnu.org/dmidecode/
Source0:	http://download.savannah.gnu.org/releases/dmidecode/%{name}-%{version}.tar.bz2
Patch0:		dmidecode-2.12-smbios_fix.patch
ExclusiveArch:	%{ix86} x86_64 ia64

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
%patch0 -p1 -b .smbios_fix~

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}" CC=%{__cc}

%install
%makeinstall_std prefix=%{_prefix} mandir=%{_mandir}
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

%files
%doc README LICENSE AUTHORS CHANGELOG
%{_sbindir}/dmidecode
%ifnarch ia64
%{_sbindir}/vpddecode
%{_sbindir}/ownership
%{_sbindir}/biosdecode
%endif
%{_mandir}/man8/*
