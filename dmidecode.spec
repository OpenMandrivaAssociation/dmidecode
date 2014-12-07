%bcond_without	uclibc

Summary:	Tool for dumping a computer's DMI table contents
Name:		dmidecode
Version:	2.12
Release:	9
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.nongnu.org/dmidecode/
Source0:	http://download.savannah.gnu.org/releases/dmidecode/%{name}-%{version}.tar.bz2
Patch0:		dmidecode-2.12-smbios_fix.patch
# (tpg) does not work with clang
Patch1:		dmidecode-2.12-whole-program.patch
#ExclusiveArch:	%{ix86} x86_64 ia64

%description
Dmidecode is a tool for dumping a computer's DMI (some say SMBIOS) table
contents in a human-readable format. This table contains a description of the
system's hardware components, as well as other useful pieces of information
such as serial numbers and BIOS revision. Part of its code can be found in
the Linux kernel, because DMI data may be used to enable or disable specific
portions of code depending on the hardware vendor. Thus, dmidecode is mainly
used to detect system "signatures" and add them to the kernel source code
when needed.

%package -n	uclibc-%{name}
Summary:	Tool for dumping a computer's DMI table contents (uClibc)
Group:		System/Kernel and hardware

%prep
%setup -q
%patch0 -p1 -b .smbios_fix~

%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
%if %{with uclibc}
pushd .uclibc
%make CFLAGS="%{uclibc_cflags}" LDFLAGS="%{?ldflags}" CC=%{uclibc_cc}
popd
%endif

%make CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}" CC=%{__cc}

%install
%if %{with uclibc}
%makeinstall_std -C .uclibc CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}" CC=%{__cc} prefix=%{uclibc_root}%{_prefix} mandir=%{_mandir}
rm -r %{buildroot}%{uclibc_root}%{_docdir}/%{name}
%endif
%makeinstall_std prefix=%{_prefix} mandir=%{_mandir} CFLAGS="%{optflags}" LDFLAGS="%{?ldflags}" CC=%{__cc}

%files
%doc %{_docdir}/%{name}
%{_sbindir}/dmidecode
%ifnarch ia64 %armx
%{_sbindir}/vpddecode
%{_sbindir}/ownership
%{_sbindir}/biosdecode
%endif
%{_mandir}/man8/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_sbindir}/dmidecode
%ifnarch ia64 %armx
%{uclibc_root}%{_sbindir}/vpddecode
%{uclibc_root}%{_sbindir}/ownership
%{uclibc_root}%{_sbindir}/biosdecode
%endif
%endif
