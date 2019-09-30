# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
# Created by pyp2rpm-1.1.1
%global pypi_name mox3

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
Mox3 is a mock object framework for Python 3 and 2.7. \
Mox3 is an unofficial port of the Google mox framework to Python 3. It was \
meant to be as compatible with mox as possible, but small enhancements have \
been made.

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Mock object framework for Python

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/mox3
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n     python%{pyver}-%{pypi_name}
Summary:        Mock object framework for Python
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}
%if %{pyver} == 3
Obsoletes: python2-%{pypi_name} < %{version}-%{release}
%endif

Requires:  python%{pyver}-pbr
Requires:  python%{pyver}-fixtures
Requires:  python%{pyver}-six >= 1.9.0
Requires:  python%{pyver}-testtools

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr

# test requires
BuildRequires:  python%{pyver}-fixtures
BuildRequires:  python%{pyver}-stestr
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-six >= 1.9.0

%description -n python%{pyver}-%{pypi_name}
%{common_desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}

# let RPM handle deps
%py_req_cleanup

%build
%{pyver_bin} setup.py build

%install
%{pyver_install}

%check
PYTHON=python%{pyver} stestr-%{pyver} run

%files -n python%{pyver}-%{pypi_name}
%doc README.rst
%license COPYING.txt
%{pyver_sitelib}/%{pypi_name}
%{pyver_sitelib}/%{pypi_name}*.egg-info

%changelog
