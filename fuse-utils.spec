Summary:	Fuse utilities
Summary(pl.UTF-8):	Programy użytkowe do fuse'a
Name:		fuse-utils
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://download.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# Source0-md5:	ae3821d721a2744a5f285177c4083098
URL:		http://fuse-emulator.sourceforge.net/
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libspectrum-devel >= 1.0.0
Requires:	libspectrum >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Fuse utilities are a few tools which may be of occasional use when
dealing with ZX Spectrum emulator files. They were originally
distributed with Fuse, the Free Unix Spectrum Emulator, but are now
independent of Fuse and can be used on their own.

The available utilities are:

- rzxdump: list the contents of an RZX input recording file.
- rzxtool: add, extract or remove the embedded snapshot from an RZX
  file, or compress or uncompress the file.
- tzxconv: do a best-guess conversion of a TZX file to a .tap file.
- tzxlist: list the contents of a TZX file.

%description -l pl.UTF-8
Programy użytkowe do fuse'a to kilka narzędzi, które mogą się przydać
gdy używamy plików emulatorów ZX Spectrum. Wcześniej były
dystrybuowane z Fuse - emulatorem ZX Spectrum, ale teraz są niezależne
i mogą być używane samodzielnie.

Dostępne są:

- rzxdump: wyświetla zawartość pliku RZX.
- rzxtool: dodaje, wyjmuje lub usuwa zanurzony snapshot z pliku RZX, a
  także kompresuje lub dekompresuje pliki.
- tzxconv: konwersuje pliki TZX do formatu TAP.
- tzxlist: wyświetla zawartość pliku TZX.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
