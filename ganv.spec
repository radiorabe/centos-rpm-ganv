Name:     ganv

Version:  1.4.2
Release:  1%{?dist}
Summary:  Ganv is an interactive Gtk canvas widget for graph-based interfaces (patchers, modular synthesizers, finite state automata, interactive graphs, etc).
License:  GPLv3+
URL:      http://drobilla.net/software/ganv
Source0:  http://download.drobilla.net/ganv-%{version}.tar.bz2

BuildRequires: python

%description
Ganv is an interactive Gtk canvas widget for graph-based interfaces (patchers, modular synthesizers, finite state automata, interactive graphs, etc).

%package -n ganv-devel
Summary:  Development packages for %{name}

%description -n ganv-devel
Development packages for %{name}

%prep
%setup -q

%build
./waf --destdir=%{buildroot} --prefix=%{_prefix} configure
./waf 

%install
./waf --destdir=%{buildroot} --prefix=%{_prefix} install
install -d %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}%{_exec_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%files
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/ganv_bench
%{_includedir}/%{name}-1/ganv/*

%files -n ganv-devel
%{_exec_prefix}/lib/libganv*
%{_libdir}/pkgconfig/*.pc
