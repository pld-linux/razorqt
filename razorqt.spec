# TODO
# - lang tag stuff: /usr/share/razor/razor-desktop/analogclock/analogclock_ru_RU.qm
Summary:	Razor a lightweight desktop toolbox
Summary(pl.UTF-8):	Razor jest lekkim zestawem narzędzi na biurko
Name:		razorqt
Version:	0.3.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/razor-qt/files/%{name}-%{version}.tar.bz2
# Source0-md5:	bf53bac8f3e74cea504415a3c0110ec8
URL:		http://razor-qt.sf.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	libmagic-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-linguist
BuildRequires:	qt4-qmake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-panel = %{version}-%{release}
Requires:	%{name}-session = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package libs
Summary:	RazorQt shared library
Summary(pl.UTF-8):	Współdzielona biblioteka RazorQt
Group:		Libraries

%description libs
RazorQt shared library.

%description libs -l pl.UTF-8
Współdzielona biblioteka RazorQt.

%package devel
Summary:	RazorQt development package
Summary(pl.UTF-8):	Pakiet programistyczny RazorQt
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
RazorQt development package.

%description devel -l pl.UTF-8
Pakiet programistyczny RazorQt.

%package appswitcher
Summary:	RazorQt application switcher
Summary(pl.UTF-8):	Przełącznik aplikacji RazorQt
Group:		X11/Applications
Requires:	%{name}-resources = %{version}-%{release}

%description appswitcher
RazorQt application switcher.

%description appswitcher -l pl.UTF-8
Przełącznik aplikacji dla RazorQt.

%package desktop
Summary:	RazorQt desktop
Summary(pl.UTF-8):	Pulpit RazorQt
Group:		X11/Applications
Requires:	%{name}-resources = %{version}-%{release}

%description desktop
RazorQt desktop.

%description desktop -l pl.UTF-8
Pulpit RazorQt.

%package panel
Summary:	RazorQt panel
Summary(pl.UTF-8):	Panel RazorQt
Group:		X11/Applications
Requires:	%{name}-resources = %{version}-%{release}

%description panel
RazorQt panel.

%description panel -l pl.UTF-8
Panel RazorQt.

%package resources
Summary:	RazorQt resources
Summary(pl.UTF-8):	Zasoby RazorQt
Group:		X11/Applications

%description resources
RazorQt resources.

%description resources -l pl.UTF-8
Zasoby RazorQt.

%package session
Summary:	RazorQt session manager
Summary(pl.UTF-8):	Menedżer sesji RazorQt
Group:		X11/Applications
Requires:	%{name}-resources = %{version}-%{release}
Requires:	%{name}-wm = %{version}-%{release}

%description session
RazorQt session manager.

%description session -l pl.UTF-8
Menedżer sesji RazorQt.

%package openbox
Summary:	RazorQt OpenDesktop session
Summary(pl.UTF-8):	Sesja OpenDesktop dla RazorQt
Group:		X11/Applications
Requires:	%{name}-session = %{version}-%{release}
Requires:	openbox
Provides:	%{name}-wm = %{version}-%{release}

%description openbox
RazorQt OpenDesktop session.

%description openbox -l pl.UTF-8
Sesja OpenDesktop dla RazorQt.

%package eggwm
Summary:	RazorQt EggWM session
Summary(pl.UTF-8):	Sesja EggWM dla RazorQt
Group:		X11/Applications
Requires:	%{name}-session = %{version}-%{release}
Requires:	eggwm
Provides:	%{name}-wm = %{version}-%{release}

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

# Makefiles and cmake installed:S
rm -r $RPM_BUILD_ROOT%{_datadir}/razor/themes/Makefile
rm -r $RPM_BUILD_ROOT%{_datadir}/razor/themes/[Cc][Mm]ake*

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	panel -p /sbin/ldconfig
%postun	panel -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librazorqt.so.*.*.*
%ghost %{_libdir}/librazorqt.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/librazorqt.so
%{_includedir}/%{name}

%files appswitcher
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-appswitcher

%files desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-desktop
%dir %{_libdir}/razor-desktop
%attr(755,root,root) %{_libdir}/razor-desktop/libanalogclock.so
%attr(755,root,root) %{_libdir}/razor-desktop/libdesktop-razor.so
%attr(755,root,root) %{_libdir}/razor-desktop/libdesktop-wm_native.so
%attr(755,root,root) %{_libdir}/razor-desktop/libhelloworld.so
%attr(755,root,root) %{_libdir}/razor-desktop/libiconview.so

%files panel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-panel
%dir %{_libdir}/razor-panel
%attr(755,root,root) %{_libdir}/razor-panel/libclock.so
%attr(755,root,root) %{_libdir}/razor-panel/libdesktopswitch.so
%attr(755,root,root) %{_libdir}/razor-panel/libmainmenu.so
%attr(755,root,root) %{_libdir}/razor-panel/libquicklaunch.so
%attr(755,root,root) %{_libdir}/razor-panel/libtaskbar.so
%attr(755,root,root) %{_libdir}/razor-panel/libtray.so

%files session
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/razor-session
%{_datadir}/xsessions/razor.desktop

%files resources
%defattr(644,root,root,755)
%{_datadir}/razor
# temp files - it will be removed when it becomes part of upstream
%dir %{_libdir}/razor-xdg-tools
# NOTE: are part of pld package, check me
%attr(755,root,root) %{_libdir}/razor-xdg-tools/xdg-mime
%attr(755,root,root) %{_libdir}/razor-xdg-tools/xdg-open

%files openbox
%defattr(644,root,root,755)
%{_datadir}/xsessions/razor-openbox.desktop

%files eggwm
%defattr(644,root,root,755)
%{_datadir}/xsessions/razor-eggwm.desktop
