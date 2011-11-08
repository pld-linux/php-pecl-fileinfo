%define		modname	fileinfo
%define		smodname	Fileinfo
%define		status		beta
Summary:	%{modname} - libmagic bindings
Summary(pl.UTF-8):	%{modname} - dowiązania biblioteki libmagic
Name:		php-pecl-%{modname}
Version:	1.0.4
Release:	8
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{smodname}-%{version}.tgz
# Source0-md5:	2854e749db157365c769cb9496f5586f
Patch0:		pecl-fileinfo-defaultdb.patch
URL:		http://pecl.php.net/package/Fileinfo/
BuildRequires:	libmagic-devel
BuildRequires:	php-devel >= 4:5.0.4
BuildRequires:	rpmbuild(macros) >= 1.344
Provides:	php(fileinfo)
%{?requires_php_extension}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension allows retrieval of information regarding vast majority
of file. This information may include dimensions, quality, length
etc...

Additionally it can also be used to retrieve the MIME type for a
particular file and for text files proper language encoding.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
To rozszerzenie pozwala na uzyskanie wielu informacji na temat plików.
Informacje te uwzględniają między innymi rozmiar, jakość, długość itp.

Dodatkowo może być użyte do uzyskania typu MIME danego pliku, a dla
plików tekstowych - użytego kodowania.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{smodname}-%{version}/* .
%patch0 -p2

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS EXPERIMENTAL fileinfo.php
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
