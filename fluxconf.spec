#
# TODO:
# - add desktop file in Settings/.
#
Summary:	Fluxbox configurator
Summary(pl):	Narzêdzie konfiguracyjne dla fluxboksa
Name:		fluxconf
Version:	0.9.7
Release:	2
License:	GPL v2
Vendor:		University of Freiburg / Germany
Group:		X11/Window Managers/Tools
Source0:	http://devaux.fabien.free.fr/flux/%{name}-%{version}.tar.gz
# Source0-md5:	207faf932e07642c779e54aba549c804
Patch0:		%{name}-Makefile.patch
URL:		http://devaux.fabien.free.fr/flux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fluxconf is a tool to configure Fluxbox.

%description -l pl
Fluxconf jest narzêdziem s³u¿±cym do konfiguracji Fluxboksa.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS ChangeLog NEWS README
