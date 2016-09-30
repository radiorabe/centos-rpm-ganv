Name:     ganv

Version:  1.4.2
Release:  1%{?dist}
Summary:  Ganv is an interactive Gtk canvas widget for graph-based interfaces (patchers, modular synthesizers, finite state automata, interactive graphs, etc).
License:  GPLv3+
URL:      http://drobilla.net/software/ganv
Source0:  http://download.drobilla.net/ganv-%{version}.tar.bz2

BuildRequires: python
BuildRequires: gtk2-devel
BuildRequires: gtkmm24-devel

%description
Ganv is an interactive Gtk canvas widget for graph-based interfaces (patchers, modular synthesizers, finite state automata, interactive graphs, etc).

%package -n ganv-devel
Summary:  Development packages for %{name}
Requires:       %{name} = %{version}-%{release}

%description -n ganv-devel
Development packages for %{name}

%prep
%setup -q

%build
./waf --destdir=%{buildroot} --prefix=%{_prefix} configure
./waf 

%install
./waf --destdir=%{buildroot} --prefix=%{_prefix} install
install -d %{buildroot}%{_libdir}/
mv %{buildroot}%{_exec_prefix}/lib/* %{buildroot}%{_libdir}/

%files
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/ganv_bench
%{_libdir}/libganv*

%files -n ganv-devel
%{_includedir}/%{name}-1/ganv/*
%{_libdir}/pkgconfig/*.pc
