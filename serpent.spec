#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : serpent
Version  : 1.30
Release  : 10
URL      : https://files.pythonhosted.org/packages/6d/e3/ccca30f16ce04f2ca079c2032a385e0a80ec9ccd0ef7f6b0eeda5560595a/serpent-1.30.tar.gz
Source0  : https://files.pythonhosted.org/packages/6d/e3/ccca30f16ce04f2ca079c2032a385e0a80ec9ccd0ef7f6b0eeda5560595a/serpent-1.30.tar.gz
Summary  : Serialization based on ast.literal_eval
Group    : Development/Tools
License  : MIT
Requires: serpent-license = %{version}-%{release}
Requires: serpent-python = %{version}-%{release}
Requires: serpent-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytz
BuildRequires : tox
BuildRequires : virtualenv

%description
Serpent serialization library (Python/.NET/Java)
================================================

%package license
Summary: license components for the serpent package.
Group: Default

%description license
license components for the serpent package.


%package python
Summary: python components for the serpent package.
Group: Default
Requires: serpent-python3 = %{version}-%{release}

%description python
python components for the serpent package.


%package python3
Summary: python3 components for the serpent package.
Group: Default
Requires: python3-core

%description python3
python3 components for the serpent package.


%prep
%setup -q -n serpent-1.30
cd %{_builddir}/serpent-1.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580143024
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/serpent
cp %{_builddir}/serpent-1.30/LICENSE %{buildroot}/usr/share/package-licenses/serpent/5063209c5ff4fd059b046f7affa7497f5eb72ea7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/serpent/5063209c5ff4fd059b046f7affa7497f5eb72ea7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
