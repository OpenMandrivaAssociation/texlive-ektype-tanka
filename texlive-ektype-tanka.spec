Name:		texlive-ektype-tanka
Version:	63255
Release:	1
Summary:	Devanagari fonts by EkType
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ektype-tanka
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ektype-tanka.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ektype-tanka.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ek-ttaaiip sNsthecyaa kaahii utkRsstt devnaagrii ttNkaaNcaa
sNgrh. ek-ttaaip sNsthaa ke kii utkRsstt devnaagrii ttNkoN kaa
sNgrh / . This package provides a collection of some excellent
Devanagari fonts by EkType: Mukta, Baloo, Modak, and Jaini.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/truetype/public/ektype-tanka
%doc %{_texmfdistdir}/doc/fonts/ektype-tanka

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
