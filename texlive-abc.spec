Name:		texlive-abc
Version:	2.0b
Release:	1
Summary:	Support ABC music notation in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/abc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The abc package lets you include lines of music written in the
ABC Plus language. The package will then employ the \write18
facility to convert your notation to PostScript (using the
established utility abcm2ps) and hence to the format needed for
inclusion in your document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/abc
%doc %{_texmfdistdir}/doc/latex/abc
#- source
%doc %{_texmfdistdir}/source/latex/abc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
