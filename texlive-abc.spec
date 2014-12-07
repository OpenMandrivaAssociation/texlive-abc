# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/abc
# catalog-date 2008-03-08 20:47:21 +0100
# catalog-license lppl
# catalog-version .0
Name:		texlive-abc
Version:	20080308
Release:	9
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
%{_texmfdistdir}/tex/latex/abc/abc.sty
%{_texmfdistdir}/tex/latex/abc/mup.sty
%doc %{_texmfdistdir}/doc/latex/abc/README
%doc %{_texmfdistdir}/doc/latex/abc/abc.pdf
%doc %{_texmfdistdir}/doc/latex/abc/example.tex
%doc %{_texmfdistdir}/doc/latex/abc/mupexa.tex
%doc %{_texmfdistdir}/doc/latex/abc/poll.abc
%doc %{_texmfdistdir}/doc/latex/abc/simple.mup
#- source
%doc %{_texmfdistdir}/source/latex/abc/abc.dtx
%doc %{_texmfdistdir}/source/latex/abc/abc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080308-2
+ Revision: 749043
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080308-1
+ Revision: 719757
- texlive-abc
- texlive-abc
- texlive-abc
- texlive-abc
- texlive-abc

