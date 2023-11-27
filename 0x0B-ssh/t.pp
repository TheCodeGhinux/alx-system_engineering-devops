#!/usr/bin/env bash
#  practice using Puppet to make changes to our configuration file

#Puupet to configure SSH clint
file_line { 'Turn off passwd auth':
	path => '/etc/ssh/ssd_config',
	line => 'PasswordAuthentication no',
	ensure => present,
 }

file_line { 'Declare identity file':
	path => '/etc/ssh/ssh_config',
	line => 'IdentityFile `/.ssh/school',
	ensure => present,
}
