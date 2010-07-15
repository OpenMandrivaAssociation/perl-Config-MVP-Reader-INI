%define upstream_name    Config-MVP-Reader-INI
%define upstream_version 2.101460

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Multi-value capable .ini file reader (for plugins)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config::INI::Reader)
BuildRequires: perl(Config::MVP::Assembler)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Obsoletes: perl-Config-INI-MVP
Obsoletes: perl-Config-INI-MVP

%description
The MVP INI file reader reads INI files, but can handle properties with
multiple values. The identification of properties that may have multiple
entries is done by section, on a plugin basis. For example, given the
following file:

  [Foo::Bar]
  x = 1
  y = 2
  y = 3

MVP will, upon reaching this section, load Foo::Bar and call a method (by
default 'multivalue_args') on it, to determine which property names may
have multiple entries. If the return value of that method includes 'y',
then the entry for 'y' in the Foo::Bar section will be an arrayref with two
values. If the list returned by 'multivalue_args' did not contain 'y', then
an exception would be raised while reading this section.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*
