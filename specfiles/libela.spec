
Name:           libela
Version:        1.0
Release:        1%{?dist}
Summary:        Runtime Event Loop Abstraction library

License:        BSD
URL:            https://github.com/fbx/libela/
Source0:        %{name}-1.0.tar.gz

BuildRequires:  libevent-devel

%description
The event loop abstraction library aims to provide an uniform event
loop API for utility libraries like glib (under gtk), CFRunLoop (in
CoreFoundation, under Cocoa), QCoreApplication (in Qt), libevent...

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%package misc
Summary:        Misc files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description misc
Don't try to install this.

%prep
%setup -q -n %{name}
libtoolize
autoreconf --install
automake --add-missing

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.TXT
%doc AUTHORS
%{_libdir}/libela.so.0
%{_libdir}/libela.so.0.0.0

%files misc
%{_bindir}/fd
%{_bindir}/fd_timeout
%{_bindir}/timeout

%files devel
%{_includedir}/ela/backend.h
%{_includedir}/ela/ela.h
%{_includedir}/ela/libevent.h
%{_libdir}/libela.a
%{_libdir}/libela.la
%{_libdir}/libela.so
%{_libdir}/pkgconfig/ela.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sat Aug 12 2017 François Cami <fcami@fedoraproject.org> - 1.0-1
- Initial package.

