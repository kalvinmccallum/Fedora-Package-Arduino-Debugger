Name:           python-arduino-dbg
Version:        0.2.0
Release:        1%{?dist}
Summary:        Interactive debugger for Arduino device sketches
License:        BSD
URL:            https://github.com/kimballa/arduino-dbg
Source:         %{pypi_source arduino-dbg}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a console debugger for use with sketches running on an embedded Arduino system. After uploading your sketch to the Arduino, you can connect the serial port to your computer and debug your running sketch with this application.}

%description %_description

%package -n     python3-arduino-dbg

Summary:        %{summary}

%description -n python3-arduino-dbg %_description

%prep
%autosetup -p1 -n arduino-dbg-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*' +auto

%check
%pyproject_check_import

%files -n python3-arduino-dbg -f %{pyproject_files}

%changelog
* Fri Mar 24 2023 Kalvin McCallum <kalvin_mccallum@student.uml.edu> - 0.2.0-1
- Initial package
