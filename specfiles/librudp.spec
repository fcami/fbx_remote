
Name:           librudp
Version:        1.0
Release:        1%{?dist}
Summary:        Reliable UDP transport library

License:        BSD
URL:            https://github.com/fbx/librudp
Source0:        %{name}-1.0.tar.gz

BuildRequires:  libela-devel

%description
Rudp is a library aimed at adding reliability features to UDP.
* Deliver packets in order
* Mark certain packets as reliable, retransmit them
* Drop unordered packets
* Implement server and client models


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
%{_libdir}/librudp.so.0
%{_libdir}/librudp.so.0.0.0

%files misc
#%{_bindir}/fd
%{_bindir}/test-client
%{_bindir}/test-server

%files devel
%{_includedir}/rudp/address.h
%{_includedir}/rudp/client.h
%{_includedir}/rudp/compiler.h
%{_includedir}/rudp/endpoint.h
%{_includedir}/rudp/error.h
%{_includedir}/rudp/list.h
%{_includedir}/rudp/packet.h
%{_includedir}/rudp/peer.h
%{_includedir}/rudp/rudp.h
%{_includedir}/rudp/server.h
%{_includedir}/rudp/time.h
%{_libdir}/librudp.a
%{_libdir}/librudp.la
%{_libdir}/librudp.so
%{_libdir}/pkgconfig/rudp.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sat Aug 12 2017 François Cami <fcami@fedoraproject.org> - 1.0-1
- Initial package.

