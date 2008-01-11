%define ver  	0.99.13
%define rel	%mkrel 5

Summary: 	GNOME/GTK Client for Masqdialer 
Name: 		gmasqdialer
Version: 	%{ver}
Release: 	%{rel}
License: 	GPL
Group:		Networking/Remote access
URL:		http://www.dpinson.com/software/gmasqdialer/
Source: 	%{URL}/files/%{name}-%{ver}.tar.bz2
# (fc) 0.99.13-3mdk disable gtk deprecation flags
Patch0:		gmasqdialer-0.99.13-deprecation.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel 
BuildRequires:	scrollkeeper
BuildRequires:	ImageMagick
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

%post
%update_menus

%postun
%clean_menus

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

