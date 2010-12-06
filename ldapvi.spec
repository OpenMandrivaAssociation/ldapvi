%define name ldapvi
%define version 1.7
%define release %mkrel 12

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Performs an LDAP search and update results using a text editor
URL:		http://www.lichteblau.com/ldapvi.html
Source0: 	http://www.lichteblau.com/download/%{name}-%{version}.tar.gz
Patch:		ldapvi-makefile.in-destdir.patch
# (misc) patch to fix the naming conflict between function "getline" of stdio.h
# and private function getline in common.h, by renaming it
# comes from upstream : 256ced029c235687bfafdffd07be7d47bf7af39b
Patch1:     ldapvi-fix_naming_conflict.diff 
License: 	GPLv2+
Group: 		System/Configuration/Other
BuildRequires:	openldap-devel >= 2.2.0
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	popt-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	libxslt-proc
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description 
ldapvi allows a user to perform an LDAP search and update results using 
a text editor

%prep
%setup -q
%patch -p1 -b .orig
%patch1 -p2 -b .conflict

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

xsltproc \
    %{buildroot}/%{_docdir}/%{name}/html.xsl \
    %{buildroot}/%{_docdir}/%{name}/manual.xml \
    > %{buildroot}/%{_docdir}/%{name}/manual.html

rm -f %{buildroot}/%{_docdir}/%{name}/html.xsl
rm -f %{buildroot}/%{_docdir}/%{name}/manual.xml
install -m 644 COPYING INSTALL NEWS %{buildroot}/%{_docdir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/*
