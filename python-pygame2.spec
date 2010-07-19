#
# TODO: - unpackaged files:
#		_site-packages/pygame/dll/*
#		_site-packages/pygame/examples/*
#		_site-packages/pygame/freetype/*
#		_site-packages/pygame/sdl/*
#		_site-packages/pygame/sdltext/*
#		_site-packages/pygame/sdlglx/*
#		_site-packages/pygame/sdlimage/*
#		_site-packages/pygame/sdlmixer/*
#		_site-packages/pygame/sdlttf/*
#		_site-packages/pygame/sprite/*
#		_site-packages/pygame/test/*
#

%define		module	pygame2
%define		_alpha	alpha5

Summary:	Python modules designed for writing games
Summary(pl.UTF-8):	Moduły Pythona dla piszących gry
Name:		python-%{module}
Version:	2.0.0
Release:	0.%{_alpha}.1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://pgreloaded.googlecode.com/files/%{module}-%{version}-%{_alpha}.tar.gz
# Source0-md5:	9b79ae86fddb613e08cbdc8bc8b96a56
URL:		http://www.pygame.org/
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel >= 1.2.10
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	portmidi-devel
BuildRequires:	python-Numeric-devel
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	smpeg-devel
Obsoletes:	python-pygame
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pygame is a set of Python modules designed for writing games. It is
written on top of the excellent SDL library. This allows you to create
fully featured games and multimedia programs in the python language.
The package is highly portable, with games running on Windows, NT4,
MacOS, OSX, BeOS, FreeBSD, IRIX, and Linux.

%description -l pl.UTF-8
Pygame jest zbiorem modułów Pythona zaprojektowanych do pisania gier.
Moduły te zostały napisane na bazie wspaniałej biblioteki SDL. Dzięki
temu możliwe jest tworzenie bogatych w multimedia gier w języku
Python.

%package devel
Summary:	C header files for pygame modules
Summary(pl.UTF-8):	Pliki nagłówkowe języka C modułów pygame
Group:		Development/Languages/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-pygame-devel

%description devel
C header files for pygame modules.

%description devel -l pl.UTF-8
Pliki nagłówkowe języka C modułów pygame.

%prep
%setup -q -n %{module}-%{version}-%{_alpha}

%build
CFLAGS="%{rpmcflags} -I/usr/include/smpeg"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.txt PKG-INFO README.txt TODO.txt doc/*
%dir %{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/threads/
%{py_sitedir}/%{module}/threads/*.py[co]

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{module}
%{_examplesdir}/%{name}-%{version}
