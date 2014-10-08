Summary:	Fuse utilities
Summary(pl.UTF-8):	Programy użytkowe do fuse'a
Name:		fuse-utils
Version:	1.1.1
Release:	4
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# Source0-md5:	76832afc4fc42b3ec5f38cdd4e764170
Patch0:		ffmpeg_enum_codecid.patch
URL:		http://fuse-emulator.sourceforge.net/
BuildRequires:	audiofile-devel >= 0.2.3
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 1.0.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libspectrum-devel >= 1.1.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	libspectrum >= 1.1.1
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
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/audio2tape
%attr(755,root,root) %{_bindir}/createhdf
%attr(755,root,root) %{_bindir}/fmfconv
%attr(755,root,root) %{_bindir}/listbasic
%attr(755,root,root) %{_bindir}/profile2map
%attr(755,root,root) %{_bindir}/raw2hdf
%attr(755,root,root) %{_bindir}/rzxcheck
%attr(755,root,root) %{_bindir}/rzxdump
%attr(755,root,root) %{_bindir}/rzxtool
%attr(755,root,root) %{_bindir}/scl2trd
%attr(755,root,root) %{_bindir}/snap2tzx
%attr(755,root,root) %{_bindir}/snapconv
%attr(755,root,root) %{_bindir}/tape2wav
%attr(755,root,root) %{_bindir}/tapeconv
%attr(755,root,root) %{_bindir}/tzxlist
%{_mandir}/man1/audio2tape.1*
%{_mandir}/man1/createhdf.1*
%{_mandir}/man1/fmfconv.1*
%{_mandir}/man1/fuse-utils.1*
%{_mandir}/man1/listbasic.1*
%{_mandir}/man1/profile2map.1*
%{_mandir}/man1/raw2hdf.1*
%{_mandir}/man1/rzxcheck.1*
%{_mandir}/man1/rzxdump.1*
%{_mandir}/man1/rzxtool.1*
%{_mandir}/man1/scl2trd.1*
%{_mandir}/man1/snap2tzx.1*
%{_mandir}/man1/snapconv.1*
%{_mandir}/man1/tape2wav.1*
%{_mandir}/man1/tapeconv.1*
%{_mandir}/man1/tzxlist.1*
