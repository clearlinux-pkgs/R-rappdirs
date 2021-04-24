#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rappdirs
Version  : 0.3.3
Release  : 21
URL      : https://cran.r-project.org/src/contrib/rappdirs_0.3.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rappdirs_0.3.3.tar.gz
Summary  : Application Directories: Determine Where to Save Data, Caches,
Group    : Development/Tools
License  : MIT
Requires: R-rappdirs-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
users computer you should use to save data, caches and logs. A port of

%package lib
Summary: lib components for the R-rappdirs package.
Group: Libraries

%description lib
lib components for the R-rappdirs package.


%prep
%setup -q -c -n rappdirs
cd %{_builddir}/rappdirs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612200706

%install
export SOURCE_DATE_EPOCH=1612200706
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rappdirs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rappdirs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rappdirs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rappdirs || :


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
/usr/lib64/R/library/rappdirs/libs/rappdirs.so
