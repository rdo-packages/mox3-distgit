# Created by pyp2rpm-1.1.1
%global pypi_name mox3

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora} > 21
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        0.20.0
Release:        1%{?dist}
Summary:        Mock object framework for Python

License:        ASL 2.0
URL:            http://git.openstack.org/cgit/openstack/mox3
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
 

%description
Mox3 is a mock object framework for Python 3 and 2.7.
Mox3 is an unofficial port of the Google mox framework to Python 3. It was
meant to be as compatible with mox as possible, but small enhancements have
been made.

%package -n     python2-%{pypi_name}
Summary:        Mock object framework for Python
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:  python-pbr
Requires:  python-fixtures
Requires:  python-six >= 1.9.0
Requires:  python-testtools

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-nose
BuildRequires:  python-testrepository

# test requires
BuildRequires:  python-fixtures
BuildRequires:  python-subunit
BuildRequires:  python-coverage
BuildRequires:  python-testtools
BuildRequires:  python-six >= 1.9.0

%description -n python2-%{pypi_name}
Mox3 is a mock object framework for Python 3 and 2.7.
Mox3 is an unofficial port of the Google mox framework to Python 3. It was
meant to be as compatible with mox as possible, but small enhancements have
been made.
 
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
BuildRequires:  python3-nose
BuildRequires:  python3-testrepository

# test requires
BuildRequires:  python3-fixtures
BuildRequires:  python3-subunit >= 1.1.0-5
BuildRequires:  python3-coverage
BuildRequires:  python3-testtools
BuildRequires:  python3-six >= 1.9.0

%description -n python3-%{pypi_name}
Mox3 is a mock object framework for Python 3 and 2.7.
Mox3 is an unofficial port of the Google mox framework to Python 3. It was
meant to be as compatible with mox as possible, but small enhancements have
been made.

This is Python 3 version.
%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# let RPM handle deps
rm -rf {test-,}requirements.txt

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
%{__python3} setup.py test
%endif
%{__python2} setup.py test

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
* Tue Feb 07 2017 Alfredo Moralejo <amoralej@redhat.com> 0.20.0-1
- Update to 0.20.0

