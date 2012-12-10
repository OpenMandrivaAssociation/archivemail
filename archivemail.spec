%define name    archivemail
%define version 0.9.0
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Summary:        A tool for archiving and compressing old email
Group:          System/Servers
URL:            http://archivemail.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/archivemail/%{name}-%{version}.tar.bz2
BuildRequires:  python-devel
BuildRequires:  docbook-dtd30-sgml
BuildRequires:  docbook-utils
Requires:       python
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
archivemail is a tool written in Python for archiving and compressing old email
in mailboxes. It can move messages older than the specified number of days to a
separate mbox format mailbox that is compressed with gzip, or optionally just
delete old email.

%prep
%setup -q

%build
%{__make} archivemail.1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%py_sitedir
./setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING FAQ README CHANGELOG TODO
%{_bindir}/*
%{_mandir}/man1/*
%py_sitedir/*.egg-info




%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.0-1mdv2011
+ Revision: 690420
- new version

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.8.2-2mdv2011.0
+ Revision: 592380
- rebuild for python 2.7

* Wed Oct 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1mdv2011.0
+ Revision: 586953
- update to new version 0.8.2

* Sun Oct 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.1-1mdv2011.0
+ Revision: 582667
- update to new version 0.8.1

* Fri Aug 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 569453
- update to new version 0.8.0

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.7.2-5mdv2010.0
+ Revision: 436656
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.7.2-4mdv2009.1
+ Revision: 324164
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.7.2-3mdv2009.0
+ Revision: 266177
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.2-2mdv2009.0
+ Revision: 202339
- add python dependency (fix #40536)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 111212
- update to new version 0.7.2


* Wed Nov 29 2006 Michael Scherer <misc@mandriva.org> 0.7.0-1mdv2007.0
+ Revision: 88663
- fix build with new python

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version
    - Import archivemail

