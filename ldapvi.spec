%define name ldapvi
%define version 1.7
%define release %mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Performs an LDAP search and update results using a text editor
URL:		http://www.lichteblau.com/ldapvi.html
Source0: 	http://www.lichteblau.com/download/%{name}-%{version}.tar.gz
Source1: 	bash-completion
Patch:		ldapvi-makefile.in-destdir.patch
#Patch1:		http://w3.gofti.com/~pfnguyen/openldap/ldapvi_sasl.diff
License: 	GPL
Group: 		System/Configuration/Other
BuildRequires:	openldap-devel >= 2.2.0
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	popt-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	libxslt-proc

%description 
ldapvi allows a user to perform an LDAP search and update results using 
a text editor

%prep
%setup -q
%patch -p1 -b .orig
#%{?_with_sasl:%patch1 -b .sasl}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
#rm -Rf %{buildroot}/%{_datadir}/doc/%{name}/

xsltproc \
    %{buildroot}/%{_docdir}/%{name}/html.xsl \
    %{buildroot}/%{_docdir}/%{name}/manual.xml \
    > %{buildroot}/%{_docdir}/%{name}/manual.html

rm -f %{buildroot}/%{_docdir}/%{name}/html.xsl
rm -f %{buildroot}/%{_docdir}/%{name}/manual.xml
install -m 644 COPYING INSTALL NEWS %{buildroot}/%{_docdir}/%{name}

# bash completion
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/bash_completion.d/%{name}
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/*
