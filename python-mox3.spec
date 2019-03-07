# Created by pyp2rpm-1.1.1
%global pypi_name mox3

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

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

%package -n     python2-%{pypi_name}
Summary:        Mock object framework for Python
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:  python2-pbr
Requires:  python2-fixtures
Requires:  python2-six >= 1.9.0
Requires:  python2-testtools

BuildRequires:  python2-devel
BuildRequires:  python2-pbr

# test requires
BuildRequires:  python2-fixtures
BuildRequires:  python2-stestr
BuildRequires:  python2-subunit
BuildRequires:  python2-testtools
BuildRequires:  python2-six >= 1.9.0

%description -n python2-%{pypi_name}
%{common_desc}
 
%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Mock object framework for Python
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:  python3-pbr
Requires:  python3-fixtures
Requires:  python3-six >= 1.9.0
Requires:  python3-testtools

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-testrepository

# test requires
BuildRequires:  python3-fixtures
BuildRequires:  python3-stestr
BuildRequires:  python3-subunit >= 1.1.0-5
BuildRequires:  python3-testtools
BuildRequires:  python3-six >= 1.9.0

%description -n python3-%{pypi_name}
%{common_desc}

This is Python 3 version.
%endif

%prep
%autosetup -p1 -n %{pypi_name}-%{upstream_version}

# let RPM handle deps
%py_req_cleanup

%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif


%install
%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%if 0%{?with_python3}
PYTHON=python3 stestr-3 run
%endif
PYTHON=python2 stestr run

%files  -n python2-%{pypi_name}
%doc README.rst
%license COPYING.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}*.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info
%endif


%changelog
