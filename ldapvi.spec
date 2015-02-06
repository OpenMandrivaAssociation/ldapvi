%define name ldapvi
%define version 1.7
%define release 13

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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7-12mdv2011.0
+ Revision: 612716
- the mass rebuild of 2010.1 packages

* Thu Apr 08 2010 Michael Scherer <misc@mandriva.org> 1.7-11mdv2010.1
+ Revision: 532993
- rebuild for new openssl
- fix License
- add fix from upstream, to fix rebuilding due to conflict in function naming

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Feb 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-9mdv2009.1
+ Revision: 344743
- rebuild against new readline

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-8mdv2009.1
+ Revision: 337588
- keep bash completion in its own package
- slight completion enhancements

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.7-6mdv2009.0
+ Revision: 248334
- rebuild

* Mon Feb 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-4mdv2008.1
+ Revision: 165120
- rebuild against ldap 2.4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-3mdv2008.1
+ Revision: 116490
- bash completion

* Fri Aug 31 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-2mdv2008.0
+ Revision: 77091
- build html manual

* Mon Jun 04 2007 Buchan Milne <bgmilne@mandriva.org> 1.7-1mdv2008.0
+ Revision: 35152
- New version 1.7


* Sun Jan 28 2007 Buchan Milne <bgmilne@mandriva.org> 1.6-2mdv2007.0
+ Revision: 114578
- Buildrequire readline-devel
- new version 1.6
  update makefile patch
- Import ldapvi

* Mon Dec 12 2005 Buchan Milne <bgmilne@mandriva.org> 1.5-1mdk
- New release 1.5

* Fri Dec 09 2005 Buchan Milne <bgmilne@mandriva.org> 1.4-1mdk
- New release 1.4

* Wed Aug 31 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.1-3mdk
- Rebuild for libldap2.3

* Mon Feb 07 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.1-2mdk
- rebuild for ldap2.2_7

* Mon Feb 02 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.1-1mdk
- Initial package

