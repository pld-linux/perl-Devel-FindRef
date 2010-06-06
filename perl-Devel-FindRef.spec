#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	FindRef
Summary:	Devel::FindRef - where is that reference to my variable hiding?
Summary(pl.UTF-8):	Devel::FindRef - znajduje referecje do zmiennych
Name:		perl-Devel-FindRef
Version:	1.422
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://ftp.man.poznan.pl/pub/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c92401767653f1ba8b98f36f23fae8d
URL:		http://search.cpan.org/dist/Devel-FindRef/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tracking down reference problems (e.g. you expect some object to be
destroyed, but there are still references to it that keep it alive)
can be very hard. Fortunately, perl keeps track of all its values, so
tracking references "backwards" is usually possible.

The track function can help track down some of those references back
to the variables containing them.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Devel/*.pm
%dir %{perl_vendorarch}/auto/Devel/FindRef
%{perl_vendorarch}/auto/Devel/FindRef/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/FindRef/*.so
%{_mandir}/man3/*
