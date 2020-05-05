Summary:	Tool for dumping a computer's DMI table contents
Name:		dmidecode
Version:	3.2
Release:	3
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.nongnu.org/dmidecode/
Source0:	http://download.savannah.gnu.org/releases/dmidecode/%{name}-%{version}.tar.xz
Patch0:		0000-dmidecode-Fix-Redfish-Hostname-print-length.patch
Patch1:		0001-dmidecode-Don-t-use-memcpy-on-dev-mem-on-arm64.patch
Patch2:		0002-dmidecode-Use-the-most-appropriate-unit-for-cache-si.patch
Patch3:		0003-dmidecode-Use-dmi_cache_size_2-in-dmi_cache_size.patch
Patch4:		0004-dmidecode-Add-Logical-non-volatile-device-to-the-mem.patch
Patch5:		0005-dmidecode-Reformat-the-FILES-section-of-the-manual-p.patch
Patch6:		0006-dmidecode-Document-how-the-UUID-fields-are-interpret.patch
Patch7:		0007-Use-comments-to-separate-sections-in-manual-pages.patch
Patch8:		0008-dmidecode-Add-missing-standard-include.patch
Patch9:		0009-dmidecode-Only-scan-dev-mem-for-entry-point-on-x86.patch
Patch10:	0010-Use-larger-units-for-memory-device-and-BIOS-size.patch
Patch11:	0011-Fix-formatting-of-TPM-table-output.patch
Patch12:	0012-dmidecode-Adding-bios-revision-to-s-option.patch
Patch13:	0013-dmidecode-Adding-firmware-revision-support-to-s-opti.patch
Patch14:	0014-dmidecode-Fix-System-Slot-Information-for-PCIe-SSD.patch
Patch15:	0015-Typo.patch
Patch16:	0016-dmidecode-Add-enumerated-values-from-SMBIOS-3.3.0.patch
Patch17:	0017-dmidecode-Decode-system-slot-base-bus-width-and-peer.patch
Patch18:	0018-dmidecode-Print-type-33-name-unconditionally.patch
Patch19:	0019-dmidecode-Don-t-choke-on-invalid-processor-voltage.patch
Patch20:	0040-Allow-overriding-build-settings-from-the-environment.patch

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
%setup_compile_flags
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
