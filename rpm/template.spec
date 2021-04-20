%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-tf2
Version:        0.17.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS tf2 package

License:        BSD
URL:            http://www.ros.org/wiki/tf2
Source0:        %{name}-%{version}.tar.gz

Requires:       console-bridge-devel
Requires:       ros-galactic-console-bridge-vendor
Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-rcutils
Requires:       ros-galactic-ros-workspace
BuildRequires:  console-bridge-devel
BuildRequires:  ros-galactic-ament-cmake
BuildRequires:  ros-galactic-ament-cmake-gtest
BuildRequires:  ros-galactic-ament-lint-auto
BuildRequires:  ros-galactic-ament-lint-common
BuildRequires:  ros-galactic-console-bridge-vendor
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-rcutils
BuildRequires:  ros-galactic-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

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
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/galactic" \
    -DAMENT_PREFIX_PATH="/opt/ros/galactic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/galactic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Tue Apr 20 2021 Chris Lalancette <clalancette@openrobotics.org> - 0.17.1-2
- Autogenerated by Bloom

* Tue Apr 06 2021 Chris Lalancette <clalancette@openrobotics.org> - 0.17.1-1
- Autogenerated by Bloom

* Thu Mar 25 2021 Chris Lalancette <clalancette@openrobotics.org> - 0.17.0-2
- Autogenerated by Bloom

* Fri Mar 19 2021 Chris Lalancette <clalancette@openrobotics.org> - 0.17.0-1
- Autogenerated by Bloom

* Thu Mar 11 2021 Chris Lalancette <clalancette@openrobotics.org> - 0.16.0-2
- Autogenerated by Bloom

* Mon Mar 08 2021 Chris Lalancette <clalancette@openrobotics.org> - 0.16.0-1
- Autogenerated by Bloom

