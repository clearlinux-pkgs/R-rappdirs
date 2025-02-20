#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-rappdirs
Version  : 0.3.3
Release  : 42
URL      : https://cran.r-project.org/src/contrib/rappdirs_0.3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rappdirs_0.3.3.tar.gz
Summary  : Application Directories: Determine Where to Save Data, Caches,
Group    : Development/Tools
License  : MIT
Requires: R-rappdirs-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
users computer you should use to save data, caches and logs. A port of

%package lib
Summary: lib components for the R-rappdirs package.
Group: Libraries

%description lib
lib components for the R-rappdirs package.


%prep
%setup -q -n rappdirs
pushd ..
cp -a rappdirs buildavx2
popd
pushd ..
cp -a rappdirs buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737154697

%install
export SOURCE_DATE_EPOCH=1737154697
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rappdirs/DESCRIPTION
/usr/lib64/R/library/rappdirs/INDEX
/usr/lib64/R/library/rappdirs/LICENSE
/usr/lib64/R/library/rappdirs/Meta/Rd.rds
/usr/lib64/R/library/rappdirs/Meta/features.rds
/usr/lib64/R/library/rappdirs/Meta/hsearch.rds
/usr/lib64/R/library/rappdirs/Meta/links.rds
/usr/lib64/R/library/rappdirs/Meta/nsInfo.rds
/usr/lib64/R/library/rappdirs/Meta/package.rds
/usr/lib64/R/library/rappdirs/NAMESPACE
/usr/lib64/R/library/rappdirs/NEWS.md
/usr/lib64/R/library/rappdirs/R/rappdirs
/usr/lib64/R/library/rappdirs/R/rappdirs.rdb
/usr/lib64/R/library/rappdirs/R/rappdirs.rdx
/usr/lib64/R/library/rappdirs/help/AnIndex
/usr/lib64/R/library/rappdirs/help/aliases.rds
/usr/lib64/R/library/rappdirs/help/paths.rds
/usr/lib64/R/library/rappdirs/help/rappdirs.rdb
/usr/lib64/R/library/rappdirs/help/rappdirs.rdx
/usr/lib64/R/library/rappdirs/html/00Index.html
/usr/lib64/R/library/rappdirs/html/R.css
/usr/lib64/R/library/rappdirs/tests/testthat.R
/usr/lib64/R/library/rappdirs/tests/testthat/_snaps/appdir.md
/usr/lib64/R/library/rappdirs/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/rappdirs/tests/testthat/test-appdir.r
/usr/lib64/R/library/rappdirs/tests/testthat/test-cache.r
/usr/lib64/R/library/rappdirs/tests/testthat/test-data.r
/usr/lib64/R/library/rappdirs/tests/testthat/test-log.r
/usr/lib64/R/library/rappdirs/tests/testthat/test-utils.r

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/rappdirs/libs/rappdirs.so
/V4/usr/lib64/R/library/rappdirs/libs/rappdirs.so
/usr/lib64/R/library/rappdirs/libs/rappdirs.so
