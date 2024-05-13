%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-tf2
Version:        0.36.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tf2 package

License:        BSD
URL:            http://www.ros.org/wiki/tf2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-builtin-interfaces
Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-rcutils
Requires:       ros-jazzy-rosidl-runtime-cpp
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-ament-cmake-ros
BuildRequires:  ros-jazzy-builtin-interfaces
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-rcutils
BuildRequires:  ros-jazzy-rosidl-runtime-cpp
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-copyright
BuildRequires:  ros-jazzy-ament-cmake-cppcheck
BuildRequires:  ros-jazzy-ament-cmake-cpplint
BuildRequires:  ros-jazzy-ament-cmake-gtest
BuildRequires:  ros-jazzy-ament-cmake-lint-cmake
BuildRequires:  ros-jazzy-ament-cmake-uncrustify
BuildRequires:  ros-jazzy-ament-cmake-xmllint
%endif

%description
tf2 is the second generation of the transform library, which lets the user keep
track of multiple coordinate frames over time. tf2 maintains the relationship
between coordinate frames in a tree structure buffered in time, and lets the
user transform points, vectors, etc between any two coordinate frames at any
desired point in time.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Mon May 13 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.3-1
- Autogenerated by Bloom

* Thu Apr 18 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.2-2
- Autogenerated by Bloom

* Wed Apr 10 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.2-1
- Autogenerated by Bloom

* Thu Mar 28 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.1-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.36.0-2
- Autogenerated by Bloom

