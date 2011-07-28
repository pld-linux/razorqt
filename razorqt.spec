Name:		razorqt
Version:	0.3.0
Release:	1
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Summary:	Razor a lightweight desktop toolbox
Summary(pl.UTF-8):	Razor jest lekkim zestawem narzędzi na biurko
Group:		X11/Applications
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-linguist
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequireS:	xorg-lib-libX11-devel
Requires:	%{name}-desktop
Requires:	%{name}-panel
Requires:	%{name}-session
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%package	devel
Summary:	RazorQt development package
Summary(pl.UTF-8):	Pakiet programistyczny RazorQt
Group:		Development/Libraries
Requires:	%{name}-libs

%package	libs
Summary:	RazorQt shared library
Summary(pl.UTF-8):	Współdzielona biblioteka RazorQt
Group:		Libraries

%package	appswitcher
Summary:	RazorQt application switcher
Summary(pl.UTF-8):	Przełącznik aplikacji RazorQt
Group:		X11/Applications
Requires:	%{name}-resources

%package	desktop
Summary:	RazorQt desktop
Summary(pl.UTF-8):	Pulpit RazorQt
Group:		X11/Applications
Requires:	%{name}-resources

%package	panel
Summary:	RazorQt panel
Summary(pl.UTF-8):	Panel RazorQt
Group:		X11/Applications
Requires:	%{name}-resources

%package	resources
Summary:	RazorQt resources
Summary(pl.UTF-8):	Zasoby RazorQt
Group:		X11/Applications

%package	session
Summary:	RazorQt session manager
Summary(pl.UTF-8):	Menedżer sesji RazorQt
Group:		X11/Applications
Requires:	%{name}-resources
Requires:	%{name}-wm

%package	openbox
Summary:	RazorQt OpenDesktop session
Summary(pl.UTF-8):	Sesja OpenDesktop dla RazorQt
Group:		X11/Applications
Requires:	%{name}-session
Requires:	openbox
Provides:	%{name}-wm

%package	eggwm
Summary:	RazorQt EggWM session
Summary(pl.UTF-8):	Sesja EggWM dla RazorQt
Group:		X11/Applications
Requires:	%{name}-session
Requires:	eggwm
Provides:	%{name}-wm


%description
Razor-Qt is a lightweight, built upon Qt4 desktop environment for
UNIX-like operating systems.

As mainstream desktop environments grows up to be more and more
heavyweight there is (as we believe) still place for a lightweight but
nice and powerful set of tools to make user's desktop nicer and easier
to use.

%description -l pl.UTF-8
Razor-Qt jest lekkim, bazującym na Qt4 środowiskiem graficznym dla
UNIKSowych systemów operacyjnych.

Pomimo że mainstreamowe środowiska graficzne stają się coraz bardziej
ociężałe, to jednak wciąż jest miejsce(a przynajmniej tak wierzymy)
dla lekkiego, ale nowoczesnego i potężnego zestawu narzędzi, które
sprawią że pulpit użytkownika stanie się ładniejszy i przyjaźniejszy w
uzytku.

%description libs
RazorQt shared library.

%description libs -l pl.UTF-8
Współdzielona biblioteka RazorQt.

%description devel
RazorQt development package.

%description devel -l pl.UTF-8
Pakiet programistyczny RazorQt.

%description appswitcher
RazorQt application switcher.

%description appswitcher -l pl.UTF-8
Przełącznik aplikacji dla RazorQt.

%description desktop
RazorQt desktop.

%description desktop -l pl.UTF-8
Pulpit RazorQt.

%description panel
RazorQt panel.

%description panel -l pl.UTF-8
Panel RazorQt.

%description resources
RazorQt resources.

%description resources -l pl.UTF-8
Zasoby RazorQt.

%description session
RazorQt session manager.

%description session -l pl.UTF-8
Menedżer sesji RazorQt.

%description openbox
RazorQt OpenDesktop session.

%description openbox -l pl.UTF-8
Sesja OpenDesktop dla RazorQt.

%description eggwm
RazorQt EggWM session.

%description eggwm -l pl.UTF-8
Sesja EggWM dla RazorQt.

%prep
%setup -q

%build
%cmake
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs
ldconfig

%post panel
ldconfig

%postun	libs
ldconfig

%postun panel
ldconfig

%files
%defattr(644,root,root,755)
%doc README

%files libs
%defattr(644,root,root,755)

%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%files appswitcher
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-appswitcher

%files desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-desktop
%{_libdir}/razor-desktop

%files panel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-panel
%{_libdir}/razor-panel/

%files session
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-session
%{_datadir}/xsessions/razor.desktop

%files resources
%defattr(644,root,root,755)
%{_datadir}/razor/
# temp files - it will be removed when it becomes part of upstream
%{_libdir}/razor-xdg-tools

%files openbox
%defattr(644,root,root,755)
%{_datadir}/xsessions/razor-openbox.desktop

%files eggwm
%defattr(644,root,root,755)
%{_datadir}/xsessions/razor-eggwm.desktop
