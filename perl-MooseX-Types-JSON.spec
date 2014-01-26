#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooseX
%define		pnam	Types-JSON
%include	/usr/lib/rpm/macros.perl
Summary:	MooseX::Types::JSON - JSON datatype for Moose
#Summary(pl.UTF-8):	
Name:		perl-MooseX-Types-JSON
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48f0a59545f8c49c4375665cc6c9a2c1
URL:		http://search.cpan.org/dist/MooseX-Types-JSON/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-JSON-XS
BuildRequires:	perl-Moose
BuildRequires:	perl-MooseX-Types
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON datatype for Moose.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Types/JSON.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
