%global tl_name istgame
%global tl_revision 79171

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1.1
Release:	%{tl_revision}.1
Summary:	Draw Game Trees with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/istgame
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/istgame.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/istgame.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides macros based on TikZ to draw a game tree.
The main idea underlying its core macros is the completion of a whole
tree by using a sequence of simple 'parent-child' tree structures, with
no longer nested relations involved (like the use of 'grandchildren' or
'great-grandchildren'). Using this package you can draw a game tree as
easily as drawing a game tree with pen and paper. This package depends
on expl3, TikZ, and xparse. The 'ist' prefix stands for "it's a simple
tree" or "In-Sung's simple tree."

