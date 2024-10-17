%define upstream_name	 Class-C3-Componentised
%define upstream_version 1.001000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Load mix-ins or components to your C3-based class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/Class-C3-Componentised-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Test::Exception)

BuildArch:	noarch

%description
This will inject base classes to your module using the Class::C3 method
resolution order.

Please note: these are not plugins that can take precedence over methods
declared in MyModule. If you want something like that, consider
MooseX::Object::Pluggable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Wed Mar 23 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.0.900-1mdv2011.0
+ Revision: 648060
- update to new version 1.0009

* Wed Mar 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.0.800-1
+ Revision: 641319
- update to new version 1.0008

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.0.600-1mdv2011.0
+ Revision: 437215
- bumping epoch
- update to 1.0006

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0005-1mdv2010.0
+ Revision: 370024
- update to new version 1.0005

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0004-1mdv2009.1
+ Revision: 357729
- update to new version 1.0004

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0003-3mdv2009.0
+ Revision: 255890
- rebuild

* Mon Mar 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0003-1mdv2008.1
+ Revision: 183290
- update to new version 1.0003

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0001-1mdv2008.0
+ Revision: 78720
- import perl-Class-C3-Componentised


* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0001-1mdv2008.0
- first mdv release

