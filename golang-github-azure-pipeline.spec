# Run tests in check section
%bcond_without check

# https://github.com/Azure/azure-pipeline-go
%global goipath         github.com/Azure/azure-pipeline-go
Version:                0.1.8

%global common_description %{expand:
Package pipeline implements an HTTP request/response middleware pipeline whose 
policy objects mutate an HTTP request's URL, query parameters, and/or headers 
before the request is sent over the wire.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Implements an HTTP request/response middleware pipeline%
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Oct 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.8-1
- First package for Fedora

