Summary:	Fuse utilities
Summary(pl):	Programy u¿ytkowe do fuse'a
Name:		fuse-utils
Version:	0.6.0
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.srcf.ucam.org/~pak21/spectrum/%{name}-%{version}.tar.gz
URL:		http://www.srcf.ucam.org/~pak21/spectrum/fuse.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libspectrum-devel > 0.1.0
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

%description -l pl
Programy u¿ytkowe do fuse'a to kilka narzêdzi, które mog± siê przydaæ
gdy u¿ywamy plików emulatorów ZX Spectrum. Wcze¶niej by³y
dystrybuowane z Fuse - emulatorem ZX Spectrum, ale teraz s± niezale¿ne
i mog± byæ u¿ywane samodzielnie.

Dostêpne s±:

- rzxdump: wy¶wietla zawarto¶æ pliku RZX.
- rzxtool: dodaje, wyjmuje lub usuwa zanurzony snapshot z pliku RZX, a
  tak¿e kompresuje lub dekompresuje pliki.
- tzxconv: konwersuje pliki TZX do formatu TAP.
- tzxlist: wy¶wietla zawarto¶æ pliku TZX.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
