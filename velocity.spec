# TODO:
# - .desktop patch with pl desc
# - pl desc
# - update BR with ilbraries versions and check BRs
# - maybe better DESTDIR.patch (it's dirty)
# - files section corretcion for right premissions
Summary:	File manager for GNOME 2 platform
Summary(pl):	Zarz±dca plików dla platformy GNOME 2
Name:		velocity
Version:	0.1
Release:	0.beta.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.ckatechnologies.com/velocity/%{name}-%{version}beta.tar.bz2
# Source0-md5:	4c7b90a40337e53d00ffc58560bc0ef7
Patch0:		%{name}-DESTDIR.patch
URL:		http://velocity.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libart_lgpl-devel
BuildRequires:	libbonoboui-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Velocity integrates access to files, applications, media,
Internet-based resources and the Web. Velocity delivers a dynamic and
rich user experience. Velocity is a free software project developed
under the GNU General Public License and will be a core component of
the GNOME desktop project.

%description -l pl
write me

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
glib-gettextize --copy --force
%{__libtoolize}
intltoolize --copy --force
%{__aclocal} -I macros/
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/plugins
%attr(755,root,root) %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/templates
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*
%{_desktopdir}/*
