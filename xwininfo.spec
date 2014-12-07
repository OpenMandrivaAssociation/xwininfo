Name:		xwininfo
Version:	1.1.3
Release:	8
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
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xwininfo
%{_mandir}/man1/xwininfo.*


%changelog
* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.2-1mdv2012.0
+ Revision: 699276
- update to new version 1.1.2

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2
+ Revision: 671377
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 591903
- new release

* Mon Sep 27 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 581412
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.5-1mdv2010.1
+ Revision: 464766
- New version: 1.0.5

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.4-2mdv2009.1
+ Revision: 350740
- rebuild

* Mon Jun 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.4-1mdv2009.0
+ Revision: 230104
- New version

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2009.0
+ Revision: 166812
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 154294
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.3-1mdv2008.0
+ Revision: 72236
- new upstream release: 1.0.3

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:24:58 (31400)
- fill in a couple of missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

