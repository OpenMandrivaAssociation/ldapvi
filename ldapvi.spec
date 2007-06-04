%define name ldapvi
%define version 1.7
%define release %mkrel 1

Summary: 	Performs an LDAP search and update results using a text editor
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
URL:		http://www.lichteblau.com/ldapvi.html
Source0: 	http://www.lichteblau.com/download/%{name}-%{version}.tar.gz
Patch:		ldapvi-makefile.in-destdir.patch
#Patch1:		http://w3.gofti.com/~pfnguyen/openldap/ldapvi_sasl.diff
License: 	GPL
Group: 		System/Configuration/Other
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	openldap-devel >= 2.2.0 glib2-devel ncurses-devel popt-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel

%description 
ldapvi allows a user to perform an LDAP search and update results using 
a text editor

%prep
%setup -q
%patch -p1 -b .orig
#%{?_with_sasl:%patch1 -b .sasl}

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -Rf %{buildroot}/%{_datadir}/doc/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING INSTALL NEWS
%doc manual/manual.css manual/manual.xml manual/bg.png manual/html.xsl
%{_bindir}/%{name}
%{_mandir}/man?/*


