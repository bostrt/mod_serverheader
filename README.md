# mod_serverheader
<a href="https://copr.fedorainfracloud.org/coprs/bostrt/mod_serverheader/package/mod_serverheader/"><img src="https://copr.fedorainfracloud.org/coprs/bostrt/mod_serverheader/package/mod_serverheader/status_image/last_build.png" /></a>

## Installation

#### Fedora users
```
# dnf copr enable bostrt/mod_serverheader
# dnf install mod_serverheader
```
#### RHEL users
The `copr` plugin is now available for RHEL in Optional repos:
```
# yum install yum-plugin-copr
# yum copr enable bostrt/mod_serverheader
# yum install mod_serverheader
```
#### RHEL alternative
Drop YUM repo file into your `/etc/yum/repos.d/`. Here's the repo file for [RHEL 7](https://copr.fedorainfracloud.org/coprs/bostrt/mod_serverheader/repo/epel-7/bostrt-mod_serverheader-epel-7.repo).


## Configuration

`/etc/httpd/conf.d/mod_serverheader.conf`

## ServerHeader Directive 

[Description](https://httpd.apache.org/docs/2.4/mod/directive-dict.html#Description): Modify Server header contents  
[Syntax](https://httpd.apache.org/docs/2.4/mod/directive-dict.html#Syntax): ServerHeader *value*  
[Context](https://httpd.apache.org/docs/2.4/mod/directive-dict.html#Context): server config, virtual host  
[Module](https://httpd.apache.org/docs/2.4/mod/directive-dict.html#Module): mod_serverheader  

-----------

This directive allows you to override Apache HTTPD's `Server` response header. In addition to configuring this directive, you may also need to modify your [`ServerTokens`](https://httpd.apache.org/docs/2.4/mod/core.html#servertokens) directive to allow for a longer value to be used.

#### Example Usage:
```
LoadModule serverheader_module modules/mod_serverheader.so
ServerTokens Full
ServerHeader my-server
```

Client will see this:
```
# curl -I http://example.com/
HTTP/1.1 200 OK
Date: Sat, 25 Feb 2017 01:47:40 GMT
Server: my-server ◀◀◀◀◀◀◀◀
Content-Length: 8
Content-Type: text/html; charset=iso-8859-1
```

## Building
```
# git clone https://github.com/bostrt/mod_serverheader.git
# cd mod_serverheader
# apxs -i -a -c mod_serverheader.c
```

## Motivation

https://robertbost.wordpress.com/2017/03/19/introducing-mod_serverheader/
