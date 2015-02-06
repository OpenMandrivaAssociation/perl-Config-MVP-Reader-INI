%define upstream_name    Config-MVP-Reader-INI
%define upstream_version 2.101462

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.101462
Release:	3

Summary:	Multi-value capable .ini file reader (for plugins)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-MVP-Reader-INI-2.101462.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Config::INI::Reader)
BuildRequires:	perl(Config::MVP::Assembler)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.101.461-2mdv2011.0
+ Revision: 656893
- rebuild for updated spec-helper

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.101.461-1mdv2011.0
+ Revision: 595088
- update to new version 2.101461

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 2.101.460-2mdv2011.0
+ Revision: 553492
- extracting requires from meta.json

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.101.460-1mdv2011.0
+ Revision: 552607
- renaming to match upstream dist name
- renaming to match upstream name
- update to 2.101460, renaming to perl-Config-MVP-Reader-INI ongoing to match upstream dist name

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.24.0-1mdv2010.1
+ Revision: 461267
- update to 0.024

* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.23.0-1mdv2010.0
+ Revision: 400635
- update to 0.023

* Sun Jul 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.22.0-1mdv2010.0
+ Revision: 400199
- update to 0.022

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.21.0-1mdv2010.0
+ Revision: 399307
- update to 0.021

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.19.0-1mdv2010.0
+ Revision: 380976
- adding missing buildrequires:
- import perl-Config-INI-MVP


