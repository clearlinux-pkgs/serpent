#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : serpent
Version  : 1.30.2
Release  : 19
URL      : https://files.pythonhosted.org/packages/55/88/5ab0e433000e430c648cddfd1ff767208bc8d60f73788f196e77b438dbe1/serpent-1.30.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/55/88/5ab0e433000e430c648cddfd1ff767208bc8d60f73788f196e77b438dbe1/serpent-1.30.2.tar.gz
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
Serpent is a simple serialization library based on ast.literal_eval.
        
        Because it only serializes literals and recreates the objects using ast.literal_eval(),
        the serialized data is safe to transport to other machines (over the network for instance)
        and de-serialize it there.
        
        *There is also a Java and a .NET (C#) implementation available. This allows for easy data transfer between the various ecosystems.
        You can get the full source distribution, a Java .jar file, and a .NET assembly dll.*
        The java library can be obtained from Maven central (groupid ``net.razorvine`` artifactid ``serpent``),
        and the .NET assembly can be obtained from Nuget.org (package ``Razorvine.Serpent``).
        
        
        **API**

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
Provides: pypi(serpent)

%description python3
python3 components for the serpent package.


%prep
%setup -q -n serpent-1.30.2
cd %{_builddir}/serpent-1.30.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133894
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
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
cp %{_builddir}/serpent-1.30.2/LICENSE %{buildroot}/usr/share/package-licenses/serpent/5063209c5ff4fd059b046f7affa7497f5eb72ea7
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
