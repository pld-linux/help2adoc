%include	/usr/lib/rpm/macros.perl
Summary:	help2adoc - tool to convert help output to asciidoc
Summary(pl.UTF-8):	help2adoc - narzędzie do konwersji wyjścia pomocy do formatu asciidoc
Name:		help2adoc
# see help2adoc.pl /VERSION
Version:	0.0.1
%define	snap	20170420
%define	gitref	37ed8924b40fb25ef6aab6ab838e0270718981df
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Applications/Text
Source0:	https://github.com/klali/help2adoc/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	6774c97d0c9da227d484b6bf95317354
URL:		https://github.com/klali/help2adoc
BuildRequires:	asciidoc
BuildRequires:	perl-base
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool to convert help output to asciidoc.

%description -l pl.UTF-8
Narzędzie do konwersji wyjścia pomocy do formatu asciidoc.

%prep
%setup -q -n %{name}-%{gitref}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -p help2adoc.pl $RPM_BUILD_ROOT%{_bindir}/help2adoc
cp -p help2adoc.1 $RPM_BUILD_ROOT%{_mandir}/man1/help2adoc.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/help2adoc
%{_mandir}/man1/help2adoc.1*
