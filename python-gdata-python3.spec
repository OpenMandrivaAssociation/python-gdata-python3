Name:		python-gdata-python3
Version:	3.0.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/gdata-python3/gdata-python3-%{version}.tar.gz
Summary:	Python client library for Google data APIs
URL:		https://pypi.org/project/gdata-python3/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python client library for Google data APIs

%prep
%autosetup -p1 -n gdata-python3-%{version}

%files
%{py_sitedir}/atom
%{py_sitedir}/gdata
%{py_sitedir}/gdata_python3-*.*-info
