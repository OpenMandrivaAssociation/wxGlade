%define name wxGlade

Name:		%{name}
Summary:	A GUI builder for wxWindows/wxPython
Version:	0.6.5
Release:	2
License:	MIT
Group:		Development/Other
URL:		http://wxglade.sourceforge.net/
Source:		https://sourceforge.net/projects/wxglade/files/wxglade/0.6.5/%{name}-%{version}.tar.gz
Requires:	python >= 2.3
Requires:	wxPython >= 2.6
BuildRequires:	imagemagick
BuildArch:	noarch

%description
wxGlade is a GUI designer written in Python with the popular GUI toolkit 
wxPython, that helps you create wxWindows/wxPython user interfaces. At the 
moment it can generate Python, C++ and XRC (wxWindows' XML resources) code.

As you can guess by the name, its model is Glade, the famous GTK+/GNOME 
GUI builder, with which wxGlade shares the philosophy and the look & feel 
(but not a line of code).

It is not (and will never be) a full featured IDE, but simply a "designer": 
the generated code does nothing apart from displaying the created widgets. 
If you are looking for a complete IDE, maybe Boa Constructor or PythonCard 
is the right tool.

%prep
%setup -q

%build

%install 
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
install *.py* %{buildroot}/%{_datadir}/%{name}
cp -a docs icons codegen widgets edit_sizers %{buildroot}/%{_datadir}/%{name}
install license.txt credits.txt %{buildroot}/%{_datadir}/%{name}
echo -e "#!/bin/sh\npython %{_datadir}/%{name}/wxglade.py "\$@"" > %{buildroot}/%{_bindir}/wxglade


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A GUI builder for wxWindows/wxPython
Exec=%{_bindir}/wxglade
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-Tools;GUIDesigner;
EOF

convert -resize 32x32 icons/icon.xpm %{buildroot}/%{_iconsdir}/%{name}.png
convert -resize 16x16 icons/icon.xpm %{buildroot}/%{_miconsdir}/%{name}.png
convert -resize 48x48 icons/icon.xpm %{buildroot}/%{_liconsdir}/%{name}.png

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/*
%doc *.txt 
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.3-5mdv2010.0
+ Revision: 434985
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.3-4mdv2009.0
+ Revision: 262182
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.3-3mdv2009.0
+ Revision: 256474
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Feb 26 2008 Lev Givon <lev@mandriva.org> 0.6.3-1mdv2008.1
+ Revision: 175514
- Update to 0.6.3.

* Wed Jan 16 2008 Lev Givon <lev@mandriva.org> 0.6.2-1mdv2008.1
+ Revision: 153734
- Update to 0.6.2.

  + Thierry Vignaud <tvignaud@mandriva.com>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Oct 25 2007 Lev Givon <lev@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 102115
- Update to 0.6.1.

* Tue Aug 28 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.5-1mdv2008.0
+ Revision: 73223
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Lev Givon <lev@mandriva.org>
    - Update to 0.5.


* Mon Apr 02 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.1-2mdv2007.1
+ Revision: 150203
- Fix command path (bug #26950)
- Import wxGlade

* Thu Sep 07 2006 Buchan Milne <bgmilne@mandriva.org> 0.4.1-1mdv2007.0
- New release 0.4.1
- xdg menu

* Sat Feb 18 2006 Jerome Martin <jerome.f.martin@free.fr> 0.4-1mdk
- New release 0.4
- Use %%{1}mdv2007.1

* Sat Jun 04 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.3.5.1-1mdk
- New release 0.3.5.1

* Sun Aug 15 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.3.3-1mdk
- 0.3.3


