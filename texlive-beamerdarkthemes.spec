Name:		texlive-beamerdarkthemes
Version:	55117
Release:	2
Summary:	Dark color themes for beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamerdarkthemes
License:	lppl1.3 cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerdarkthemes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerdarkthemes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package with three dark color themes for beamer, designed for
presentations with pictures and/or for bright rooms without
screen. These themes mix one dominant foreground colour and a
black background. Cormorant stands for green, frigatebird for
red and magpie for blue.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamerdarkthemes
%doc %{_texmfdistdir}/doc/latex/beamerdarkthemes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
