%define ver  	0.99.13
%define rel	%mkrel 9

Summary: 	GNOME/GTK Client for Masqdialer 
Name: 		gmasqdialer
Version: 	%{ver}
Release: 	%{rel}
License: 	GPL
Group:		Networking/Remote access
URL:		https://www.dpinson.com/software/gmasqdialer/
Source: 	%{URL}/files/%{name}-%{ver}.tar.bz2
# (fc) 0.99.13-3mdk disable gtk deprecation flags
Patch0:		gmasqdialer-0.99.13-deprecation.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel 
BuildRequires:	scrollkeeper
BuildRequires:	imagemagick
BuildRequires:	automake1.4

%description
Gnome client that allows a user to manipulate a Masqdialer controlled ppp link.

%prep
%setup -q
%patch0 -p1 -b .deprecation

#needed by patch0
automake-1.4

%build
%configure2_5x
%make

%install
%makeinstall

#Menu:

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gmasqdialer
Comment=Gnome Client for the masqdialer modem server
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-Internet-RemoteAccess;Network;RemoteAccess;Dialup;
EOF

mkdir -p %{buildroot}%{_liconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
convert -resize 48x48 %{name}-icon.png %{buildroot}%{_liconsdir}/%{name}.png
convert -resize 32x32 %{name}-icon.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 16x16 %{name}-icon.png %{buildroot}%{_miconsdir}/%{name}.png	

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_iconsdir}/*.png
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.13-9mdv2011.0
+ Revision: 618965
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.99.13-8mdv2010.0
+ Revision: 429219
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.99.13-7mdv2009.0
+ Revision: 246254
- rebuild
- fix description-line-too-long
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.99.13-5mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Sep 05 2006 Buchan Milne <bgmilne@mandriva.org>
+ 2006-09-05 13:13:40 (60054)
xdg menu

* Tue Sep 05 2006 Buchan Milne <bgmilne@mandriva.org>
+ 2006-09-05 12:52:40 (60051)
buildrequire automake1.4

* Tue Sep 05 2006 Buchan Milne <bgmilne@mandriva.org>
+ 2006-09-05 12:49:19 (60050)
Import gmasqdialer

* Sat May 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.99.13-3mdk
- Patch0: don't enable gtk deprecation flags
- Clean build requires to stop iurt spam

