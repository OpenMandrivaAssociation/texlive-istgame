Name:		texlive-istgame
Version:	62946
Release:	1
Summary:	Draw Game Trees with TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/istgame
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/istgame.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/istgame.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides macros based on TikZ to draw a game
tree. The main idea underlying its core macros is the
completion of a whole tree by using a sequence of simple
'parent-child' tree structures, with no longer nested relations
involved (like the use of 'grandchildren' or
'great-grandchildren'). Using this package you can draw a game
tree as easily as drawing a game tree with pen and paper. This
package depends on expl3, TikZ, and xparse. The 'ist' prefix
stands for "it's a simple tree" or "In-Sung's simple tree."

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/istgame
%doc %{_texmfdistdir}/doc/latex/istgame

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
