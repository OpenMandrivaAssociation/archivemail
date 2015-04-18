%define name    archivemail
%define version 0.9.0
%define release 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Summary:        A tool for archiving and compressing old email
Group:          System/Servers
URL:            http://archivemail.sourceforge.net/
Source:         http://prdownloads.sourceforge.net/archivemail/%{name}-%{version}.tar.bz2
BuildRequires:  python2-devel
BuildRequires:  docbook-dtd30-sgml
BuildRequires:  docbook-utils
Requires:       python2
BuildArch:      noarch


%description 
archivemail is a tool written in Python for archiving and compressing old email
in mailboxes. It can move messages older than the specified number of days to a
separate mbox format mailbox that is compressed with gzip, or optionally just
delete old email.

%prep
%setup -q

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH
export LDFLAGS="$LDFLAGS -lpython2.7"

%{__make} archivemail.1

%install

mkdir -p %{buildroot}/%py2_sitedir
%__python2 setup.py install --root=%{buildroot}

%files
%doc COPYING FAQ README CHANGELOG TODO
%{_bindir}/*
%{_mandir}/man1/*
%py2_sitedir/*.egg-info

