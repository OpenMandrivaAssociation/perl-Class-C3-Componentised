%define module	Class-C3-Componentised
%define name	perl-%{module}
%define version 1.0003
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Load mix-ins or components to your C3-based class
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires:  perl(Class::C3)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Test::Exception)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This will inject base classes to your module using the Class::C3 method
resolution order.

Please note: these are not plugins that can take precedence over methods
declared in MyModule. If you want something like that, consider
MooseX::Object::Pluggable.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

