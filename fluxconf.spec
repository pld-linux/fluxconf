Summary:	Fluxbox configurator
Summary(pl):	Narzêdzie konfiguracyjne dla fluxboksa
Name:		fluxconf
Version:	0.6
Release:	1
License:	GPL
Vendor:		University of Freiburg / Germany
Group:		X11/Window Managers/Tools
Source0:	http://devaux.fabien.free.fr/flux/%{name}-%{version}.tar.bz2
URL:		http://devaux.fabien.free.fr/flux/
BuildRequires:  gtk+-devel
BuildRoot: 	%{tmpdir}/%{name}-%{version}-build-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
Fluxconf is a tool to configure Fluxbox.

%description -l pl
Fluxconf jest narzêdziem s³u¿±cym do konfiguracji Fluxboksa.

%prep
%setup -q 

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install fluxconf $RPM_BUILD_ROOT%{_bindir}
install fluxkeys $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fluxconf
%attr(755,root,root) %{_bindir}/fluxkeys
