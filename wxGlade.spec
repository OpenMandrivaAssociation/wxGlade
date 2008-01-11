%define name wxGlade
%define version 0.6.1
%define release %mkrel 1

Name:		%{name}
Summary:	A GUI builder for wxWindows/wxPython
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Development/Other
URL:		http://wxglade.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/wxglade/%{name}-%{version}.tar.bz2
Requires:	python >= 2.3
Requires:	wxPython >= 2.6
BuildRequires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
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
rm -Rf %{buildroot}
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

%clean
rm -rf %buildroot

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root,-)
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/*
%doc *.txt 
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


