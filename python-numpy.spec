%define		module	numpy

Summary:	Python numerical facilities
Name:		python-%{module}
Version:	1.9.0
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/numpy/%{module}-%{version}.tar.gz
# Source0-md5:	a93dfc447f3ef749b31447084839930b
URL:		http://sourceforge.net/projects/numpy/
BuildRequires:	lapack-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Obsoletes:	python-numpy-numarray
Obsoletes:	python-numpy-numarray-devel
Obsoletes:	python-numpy-oldnumeric
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%package devel
Summary:	C header files for numerical modules
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
C header files for numerical modules.

%package -n f2py
Summary:	Fortran to Python interface generator
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n f2py
Fortran to Python interface generator.

%prep
%setup -qn %{module}-%{version}

%build
export CC="%{__cc}"
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/doc
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/%{module}/core/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/fft/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/lib/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/linalg/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/random/*.so
%dir %{py_sitedir}/%{module}
%dir %{py_sitedir}/%{module}/compat
%dir %{py_sitedir}/%{module}/core
%dir %{py_sitedir}/%{module}/distutils
%dir %{py_sitedir}/%{module}/distutils/command
%dir %{py_sitedir}/%{module}/distutils/fcompiler
%dir %{py_sitedir}/%{module}/fft
%dir %{py_sitedir}/%{module}/lib
%dir %{py_sitedir}/%{module}/linalg
%dir %{py_sitedir}/%{module}/matrixlib
%dir %{py_sitedir}/%{module}/polynomial
%dir %{py_sitedir}/%{module}/random
%dir %{py_sitedir}/%{module}/testing
%dir %{py_sitedir}/numpy/ma
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/compat/*.py[co]
%{py_sitedir}/%{module}/core/*.py[co]
%{py_sitedir}/%{module}/distutils/*.py[co]
%{py_sitedir}/%{module}/distutils/command/*.py[co]
%{py_sitedir}/%{module}/distutils/fcompiler/*.py[co]
%{py_sitedir}/%{module}/fft/*.py[co]
%{py_sitedir}/%{module}/lib/*.py[co]
%{py_sitedir}/%{module}/linalg/*.py[co]
%{py_sitedir}/%{module}/matrixlib/*.py[co]
%{py_sitedir}/%{module}/polynomial/*.py[co]
%{py_sitedir}/%{module}/random/*.py[co]
%{py_sitedir}/%{module}/testing/*.py[co]
%{py_sitedir}/%{module}/tests
%{py_sitedir}/numpy/ma/*.py[co]

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/core/include
%{py_sitedir}/%{module}/core/lib
%{py_sitedir}/%{module}/random/*.h

%files -n f2py
%defattr(644,root,root,755)
%attr(744,root,root) %{_bindir}/f2py
%dir %{py_sitedir}/%{module}/f2py
%{py_sitedir}/%{module}/f2py/*.py[co]
%{py_sitedir}/%{module}/f2py/src

