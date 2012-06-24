#
# TODO:
# - add desktop file in Settings/.
#
Summary:	Fluxbox configurator
Summary(pl):	Narz�dzie konfiguracyjne dla fluxboksa
Name:		fluxconf
Version:	0.6
Release:	1
License:	GPL
Vendor:		University of Freiburg / Germany
Group:		X11/Window Managers/Tools
Source0:	http://devaux.fabien.free.fr/flux/%{name}-%{version}.tar.bz2
# Source0-md5:	17099e2f6cb7206aac2a9f599b4c084b
URL:		http://devaux.fabien.free.fr/flux/
BuildRequires:	gtk+-devel
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Fluxconf is a tool to configure Fluxbox.

%description -l pl
Fluxconf jest narz�dziem s�u��cym do konfiguracji Fluxboksa.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install fluxconf fluxkeys $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
