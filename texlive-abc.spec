%global tl_name abc
%global tl_revision 41157

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0b
Release:	%{tl_revision}.1
Summary:	Support ABC music notation in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The abc package lets you include lines of music written in the ABC Plus
language. The package will then employ the \write18 facility to convert
your notation to PostScript (using the established utility abcm2ps) and
hence to the format needed for inclusion in your document.

