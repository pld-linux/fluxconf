Name:		fluxconf
Summary:	Fluxbox configurator
Summary(pl):	Narzêdzie konfiguracyjne dla fluxbox
Version:	0.6
Release:	1
Group:		X11/Window Managers/Tools
License:	GPL
URL:		http://devaux.fabien.free.fr/flux/
Vendor:		University of Freiburg / Germany
Source0:	http://devaux.fabien.free.fr/flux/%{name}-%{version}.tar.bz2
BuildRoot: 	%{tmpdir}/%{name}-%{version}-build-root-%(id -u -n)
BuildRequires:  gtk+-devel

%define 	_x11bindir	%{_prefix}/X11R6/bin

%description
Fluxconf is a tool to configure Fluxbox

%description -l pl
Fluxconf jest narzêdziem s³u¿±cym do konfiguracji Fluxbox'a

%prep
%setup -q 

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_x11bindir}
install fluxconf $RPM_BUILD_ROOT%{_x11bindir}
install fluxkeys $RPM_BUILD_ROOT%{_x11bindir}


%files
%defattr(644,root,root,755)
#%doc src/*.gz
%attr(755,root,root) %{_x11bindir}/fluxconf
%attr(755,root,root) %{_x11bindir}/fluxkeys


%clean
rm -rf $RPM_BUILD_ROOT
