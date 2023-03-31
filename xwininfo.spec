%define _disable_rebuild_configure 1

Name:		xwininfo
Version:	1.1.5
Release:	2
Summary:	Window information utility for X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
Xwininfo is a utility for displaying information about windows.

%prep
%autosetup -p1

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xwininfo
%{_mandir}/man1/xwininfo.*
