Name: xwininfo
Version: 1.0.3
Release: %mkrel 2
Summary: Window information utility for X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxext-devel	>= 1.0.0
BuildRequires: libxmu-devel	>= 1.0.3

%description
Xwininfo is a utility for displaying information about windows.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xwininfo
%{_mandir}/man1/xwininfo.*
