#
# TODO:
# - add desktop file in Settings/.
#
Summary:	Fluxbox configurator
Summary(pl):	Narzêdzie konfiguracyjne dla fluxboksa
Name:		fluxconf
Version:	0.9.5
Release:	1
License:	GPL v2
Vendor:		University of Freiburg / Germany
Group:		X11/Window Managers/Tools
Source0:	http://devaux.fabien.free.fr/flux/%{name}-%{version}.tar.gz
# Source0-md5:	262a3c285979fd3fba89eb7f45528292
Patch0:		%{name}-Makefile.patch
URL:		http://devaux.fabien.free.fr/flux/
BuildRequires:	autoconf
BuildRequires:	automake
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS ABOUT-NLS ChangeLog COPYING INSTALL NEWS README
