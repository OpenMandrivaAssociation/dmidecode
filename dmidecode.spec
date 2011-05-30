Summary:	Tool for dumping a computer's DMI table contents
Name:		dmidecode
Version:	2.11
Release:	%mkrel 1
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
