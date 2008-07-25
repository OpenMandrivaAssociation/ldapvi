%define name ldapvi
%define version 1.7
%define release %mkrel 6

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Performs an LDAP search and update results using a text editor
URL:		http://www.lichteblau.com/ldapvi.html
Source0: 	http://www.lichteblau.com/download/%{name}-%{version}.tar.gz
Source1: 	bash-completion
Patch:		ldapvi-makefile.in-destdir.patch
License: 	GPL
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
