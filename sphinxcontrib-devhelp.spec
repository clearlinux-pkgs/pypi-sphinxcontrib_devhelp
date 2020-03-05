#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-devhelp
Version  : 1.0.2
Release  : 10
URL      : https://files.pythonhosted.org/packages/98/33/dc28393f16385f722c893cb55539c641c9aaec8d1bc1c15b69ce0ac2dbb3/sphinxcontrib-devhelp-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/33/dc28393f16385f722c893cb55539c641c9aaec8d1bc1c15b69ce0ac2dbb3/sphinxcontrib-devhelp-1.0.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/98/33/dc28393f16385f722c893cb55539c641c9aaec8d1bc1c15b69ce0ac2dbb3/sphinxcontrib-devhelp-1.0.2.tar.gz.asc
Summary  : sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-devhelp-license = %{version}-%{release}
Requires: sphinxcontrib-devhelp-python = %{version}-%{release}
Requires: sphinxcontrib-devhelp-python3 = %{version}-%{release}
Requires: flake8
Requires: mypy
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : mypy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.

%package license
Summary: license components for the sphinxcontrib-devhelp package.
Group: Default

%description license
license components for the sphinxcontrib-devhelp package.


%package python
Summary: python components for the sphinxcontrib-devhelp package.
Group: Default
Requires: sphinxcontrib-devhelp-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-devhelp package.


%package python3
Summary: python3 components for the sphinxcontrib-devhelp package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_devhelp)

%description python3
python3 components for the sphinxcontrib-devhelp package.


%prep
%setup -q -n sphinxcontrib-devhelp-1.0.2
cd %{_builddir}/sphinxcontrib-devhelp-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583452230
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-devhelp
cp %{_builddir}/sphinxcontrib-devhelp-1.0.2/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-devhelp/7ff1f231e0b27a80eb835961e888560c43a649ca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-devhelp/7ff1f231e0b27a80eb835961e888560c43a649ca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
