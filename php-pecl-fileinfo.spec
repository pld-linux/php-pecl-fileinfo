%define		_modname	fileinfo
%define		_smodname	Fileinfo
%define		_status		beta
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)

Summary:	%{_modname} - libmagic bindings
Summary(pl):	%{_modname} - dowi�zania biblioteki libmagic
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_smodname}-%{version}.tgz
# Source0-md5:	66503ab12c7d9cc1958b653845baa49c
URL:		http://pecl.php.net/package/Fileinfo/
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.254
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension allows retrieval of information regarding vast majority
of file. This information may include dimensions, quality, length
etc...

Additionally it can also be used to retrieve the MIME type for a
particular file and for text files proper language encoding.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie pozwala na uzyskanie wielu informacji na temat plik�w.
Informacje te uwzgl�dniaj� mi�dzy innymi rozmiar, jako��, d�ugo��
itp.

Dodatkowo mo�e by� u�yte do uzyskania typu MIME danego pliku, a dla
plik�w tekstowych - u�ytego kodowania.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c 

%build
cd %{_smodname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_smodname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc %{_smodname}-%{version}/{CREDITS,EXPERIMENTAL,fileinfo.php}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
