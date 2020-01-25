#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%define	pdir	Devel
%define	pnam	FindRef
Summary:	Devel::FindRef - where is that reference to my variable hiding?
Summary(pl.UTF-8):	Devel::FindRef - znajdowanie referecji do zmiennych
Name:		perl-Devel-FindRef
Version:	1.422
Release:	8
# same as perl 5.8.8 or later perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c92401767653f1ba8b98f36f23fae8d
URL:		http://search.cpan.org/dist/Devel-FindRef/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-common-sense
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tracking down reference problems (e.g. you expect some object to be
destroyed, but there are still references to it that keep it alive)
can be very hard. Fortunately, perl keeps track of all its values, so
tracking references "backwards" is usually possible.

The track function can help track down some of those references back
to the variables containing them.

%description -l pl.UTF-8
Śledzenie problemów z referencjami (np. kiedy oczekujemy, że obiekt
zostanie zniszczony, ale jeszcze istnieją referencje do niego, więc
jest utrzymywany) może być bardzo trudne. Na szczęście perl trzyma
ślady wszystkich ich wartości, więc zwykle można wyśledzić referencje
"wstecznie".

Funkcja track pozwala prześledzić referencje wstecz do zmiennych je
zawierających.

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
%doc COPYING Changes README
%{perl_vendorarch}/Devel/FindRef.pm
%dir %{perl_vendorarch}/auto/Devel/FindRef
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/FindRef/FindRef.so
%{_mandir}/man3/Devel::FindRef.3pm*
