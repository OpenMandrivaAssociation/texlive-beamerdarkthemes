%global tl_name beamerdarkthemes
%global tl_revision 55117

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.1
Release:	%{tl_revision}.1
Summary:	Dark color themes for beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerdarkthemes
License:	lppl1.3 cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerdarkthemes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerdarkthemes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package with three dark color themes for beamer, designed for
presentations with pictures and/or for bright rooms without screen.
These themes mix one dominant foreground colour and a black background.
Cormorant stands for green, frigatebird for red and magpie for blue.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes
%dir %{_datadir}/texmf-dist/tex/latex/beamerdarkthemes
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/README
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/beamerdarkthemesuserguide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/beamerdarkthemesuserguide.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/ccby.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/cormorantexampledefault.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/cormorantexampleinfolines.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/cormorantexamplesidebar.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/cormorantexampletree.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/dahut.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/example.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/frigatebirdexampledefault.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/frigatebirdexampleinfolines.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/frigatebirdexamplesidebar.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/frigatebirdexampletree.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/img_5630.jpg
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/magpieexampledefault.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/magpieexampleinfolines.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/magpieexamplesidebar.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/magpieexampletree.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/makecormorant.sh
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/makeexamples.sh
%doc %{_datadir}/texmf-dist/doc/latex/beamerdarkthemes/makemagpie.sh
%{_datadir}/texmf-dist/tex/latex/beamerdarkthemes/beamercolorthemecormorant.sty
%{_datadir}/texmf-dist/tex/latex/beamerdarkthemes/beamercolorthemefrigatebird.sty
%{_datadir}/texmf-dist/tex/latex/beamerdarkthemes/beamercolorthememagpie.sty
