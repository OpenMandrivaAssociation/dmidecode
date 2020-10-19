Summary:	Tool for dumping a computer's DMI table contents
Name:		dmidecode
Version:	3.3
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.nongnu.org/dmidecode/
Source0:	http://download.savannah.gnu.org/releases/dmidecode/%{name}-%{version}.tar.xz

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
%autosetup -p1

%build
%set_build_flags
%make_build CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}" CC=%{__cc}

%install
%make_install prefix=%{_prefix} mandir=%{_mandir} CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}" CC=%{__cc}

%files
%doc %{_docdir}/%{name}
%{_sbindir}/dmidecode
%ifnarch ia64 %armx %{riscv}
%{_sbindir}/vpddecode
%{_sbindir}/ownership
%{_sbindir}/biosdecode
%endif
%{_mandir}/man8/*
