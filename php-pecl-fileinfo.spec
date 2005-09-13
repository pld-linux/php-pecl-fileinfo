%define		_modname	fileinfo
%define		_smodname	Fileinfo
%define		_status		beta

Summary:	%{_modname} - libmagic bindings
Summary(pl):	%{_modname} - dowi±zania biblioteki libmagic
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_smodname}-%{version}.tgz
# Source0-md5:	e228172c2486c4866c1242d752bae54d
URL:		http://pecl.php.net/package/Fileinfo/
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This extension allows retrieval of information regarding vast majority
of file. This information may include dimensions, quality, length
etc...

Additionally it can also be used to retrieve the MIME type for a
particular file and for text files proper language encoding.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie pozwala na uzyskanie wielu informacji na temat plików.
Informacje te uwzglêdniaj± miêdzy innymi rozmiar, jako¶æ, d³ugo¶æ,
itp.

Dodatkowo mo¿e byæ u¿yte do uzyskania typu MIME danego pliku, a dla
plików tekstowych u¿ytego kodowania.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c -n php-pear-%{_smodname}

%build
cd %{_smodname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_smodname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_smodname}-%{version}/{CREDITS,EXPERIMENTAL}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
