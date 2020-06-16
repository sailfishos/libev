%global package_version 4.33

Name:             libev
Version:          %{package_version}+git1
Release:          1
Summary:          High-performance event loop/event model with lots of features

License:          BSD or GPLv2+
URL:              http://software.schmorp.de/pkg/libev.html
Source0:          %{name}-%{package_version}.tar.gz
Source1:          README.md

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    coreutils
BuildRequires:    findutils
BuildRequires:    gcc
BuildRequires:    libtool
BuildRequires:    make
BuildRequires:    tar

Provides:         bundled(libecb) = 1.05

%description
Libev is modeled (very loosely) after libevent and the Event Perl
module, but is faster, scales better and is more correct, and also more
featureful. And also smaller.

%package devel
Summary:          Development headers for libev
Requires:         %{name} = %{version}-%{release}

%description devel
This package contains the development headers and libraries for libev.

%package libevent-devel
Summary:          Compatibility development header with libevent for %{name}.
Requires:         %{name}-devel = %{version}-%{release}

# The event.h file actually conflicts with the one from libevent-devel
Conflicts:        libevent-devel

%description libevent-devel
This package contains a development header to make libev compatible with
libevent.

%package doc
Summary:          Documentation of %{name}
BuildArch:        noarch

%description doc
This package contains the documentation for %{name}.

%prep
%autosetup -p0 -n %{name}-%{package_version}
autoreconf -vfi

%build
%configure --disable-static --with-pic
%make_build

%check
make check

%install
%make_install
rm -vf %{buildroot}%{_libdir}/%{name}.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/%{name}.so.4*

%files devel
%{_includedir}/ev++.h
%{_includedir}/ev.h
%{_libdir}/%{name}.so
%{_mandir}/man?/*

%files libevent-devel
%{_includedir}/event.h

%files doc
%license LICENSE
%doc Changes README
