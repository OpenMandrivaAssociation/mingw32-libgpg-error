%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}
%define _use_internal_dependency_generator 0
%define __find_requires %{_mingw32_findrequires}
%define __find_provides %{_mingw32_findprovides}

Name:           mingw32-libgpg-error
Version:        1.6
Release:        %mkrel 2
Summary:        MinGW Windows GnuPGP error library

License:        LGPLv2+
Group:          Development/Other
URL:            ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2.sig
Source2:        wk@g10code.com
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 27
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-iconv
BuildRequires:  mingw32-gettext

BuildRequires:  gettext


%description
MinGW Windows GnuPGP error library.


%prep
%setup -q -n libgpg-error-%{version}


%build
%{_mingw32_configure}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm $RPM_BUILD_ROOT%{_mingw32_libdir}/libgpg-error.a

%find_lang libgpg-error

%clean
rm -rf $RPM_BUILD_ROOT


%files -f libgpg-error.lang
%defattr(-,root,root)
%{_mingw32_bindir}/gpg-error-config
%{_mingw32_bindir}/gpg-error.exe
%{_mingw32_bindir}/libgpg-error-0.dll
%{_mingw32_libdir}/libgpg-error.dll.a
%{_mingw32_libdir}/libgpg-error.la
%{_mingw32_includedir}/gpg-error.h
%{_mingw32_datadir}/aclocal/gpg-error.m4
%{_mingw32_datadir}/common-lisp/source/gpg-error/*
