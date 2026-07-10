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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The abc package lets you include lines of music written in the ABC Plus
language. The package will then employ the \write18 facility to convert
your notation to PostScript (using the established utility abcm2ps) and
hence to the format needed for inclusion in your document.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/abc
%dir %{_datadir}/texmf-dist/source/latex/abc
%dir %{_datadir}/texmf-dist/tex/latex/abc
%doc %{_datadir}/texmf-dist/doc/latex/abc/README
%doc %{_datadir}/texmf-dist/doc/latex/abc/abc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abc/example.tex
%doc %{_datadir}/texmf-dist/doc/latex/abc/jacky.abc
%doc %{_datadir}/texmf-dist/doc/latex/abc/mupexa.tex
%doc %{_datadir}/texmf-dist/doc/latex/abc/poll.abc
%doc %{_datadir}/texmf-dist/doc/latex/abc/simple.mup
%doc %{_datadir}/texmf-dist/source/latex/abc/abc.dtx
%doc %{_datadir}/texmf-dist/source/latex/abc/abc.ins
%{_datadir}/texmf-dist/tex/latex/abc/abc.sty
%{_datadir}/texmf-dist/tex/latex/abc/mup.sty
