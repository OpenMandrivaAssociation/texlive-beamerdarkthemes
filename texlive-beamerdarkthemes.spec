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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package with three dark color themes for beamer, designed for
presentations with pictures and/or for bright rooms without screen.
These themes mix one dominant foreground colour and a black background.
Cormorant stands for green, frigatebird for red and magpie for blue.

