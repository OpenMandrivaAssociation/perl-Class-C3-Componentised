%define upstream_name	 Class-C3-Componentised
%define upstream_version 1.0009

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:	Load mix-ins or components to your C3-based class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Class::C3)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Test::Exception)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This will inject base classes to your module using the Class::C3 method
resolution order.

Please note: these are not plugins that can take precedence over methods
declared in MyModule. If you want something like that, consider
MooseX::Object::Pluggable.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
