#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-npsurv
Version  : 0.5.0
Release  : 32
URL      : https://cran.r-project.org/src/contrib/npsurv_0.5-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/npsurv_0.5-0.tar.gz
Summary  : Nonparametric Survival Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lsei
BuildRequires : R-lsei
BuildRequires : buildreq-R

%description
interval-censored observations. The methods implemented
	     are developed by Wang (2007)

%prep
%setup -q -c -n npsurv
cd %{_builddir}/npsurv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641067212

%install
export SOURCE_DATE_EPOCH=1641067212
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library npsurv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library npsurv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library npsurv
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc npsurv || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/npsurv/DESCRIPTION
/usr/lib64/R/library/npsurv/INDEX
/usr/lib64/R/library/npsurv/Meta/Rd.rds
/usr/lib64/R/library/npsurv/Meta/data.rds
/usr/lib64/R/library/npsurv/Meta/features.rds
/usr/lib64/R/library/npsurv/Meta/hsearch.rds
/usr/lib64/R/library/npsurv/Meta/links.rds
/usr/lib64/R/library/npsurv/Meta/nsInfo.rds
/usr/lib64/R/library/npsurv/Meta/package.rds
/usr/lib64/R/library/npsurv/NAMESPACE
/usr/lib64/R/library/npsurv/R/npsurv
/usr/lib64/R/library/npsurv/R/npsurv.rdb
/usr/lib64/R/library/npsurv/R/npsurv.rdx
/usr/lib64/R/library/npsurv/data/acfail.rda
/usr/lib64/R/library/npsurv/data/ap.rda
/usr/lib64/R/library/npsurv/data/cancer.rda
/usr/lib64/R/library/npsurv/data/gastric.rda
/usr/lib64/R/library/npsurv/data/leukemia.rda
/usr/lib64/R/library/npsurv/data/marijuana.rda
/usr/lib64/R/library/npsurv/data/nzmort.rda
/usr/lib64/R/library/npsurv/help/AnIndex
/usr/lib64/R/library/npsurv/help/aliases.rds
/usr/lib64/R/library/npsurv/help/npsurv.rdb
/usr/lib64/R/library/npsurv/help/npsurv.rdx
/usr/lib64/R/library/npsurv/help/paths.rds
/usr/lib64/R/library/npsurv/html/00Index.html
/usr/lib64/R/library/npsurv/html/R.css
