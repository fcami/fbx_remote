
Name:           foils_hid
Version:        1.0
Release:        1%{?dist}
Summary:        HID device UDP client

License:        BSD
URL:            https://github.com/fbx/foils_hid
Source0:        %{name}-1.0.tar.gz

BuildRequires:  librudp-devel
BuildRequires:  libela-devel

%description
Foils-HID is a library for creating Freebox Network HID devices.
It uses libela for event loop abstraction and librudp for low-level
UDP transport. Libela makes it abstract from a particular event loop
so it should be embeddable in any GUI toolkit.

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
#%{_libdir}/

%files misc
%{_bindir}/mouse
%{_bindir}/remote

%files devel
%{_includedir}/foils/hid.h
%{_includedir}/foils/hid_device.h
%{_includedir}/foils/rudp_hid_client.h
%{_libdir}/libfoils_hid.a

# quite unnecessary in this case
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sat Aug 12 2017 François Cami <fcami@fedoraproject.org> - 1.0-1
- Initial package.

