%define name    archivemail
%define version 0.8.1
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
./setup.py install --root=%{buildroot} --install-data=usr/share

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING FAQ README CHANGELOG TODO
%{_bindir}/*
%{_mandir}/man1/*
%py_sitedir/*.egg-info


