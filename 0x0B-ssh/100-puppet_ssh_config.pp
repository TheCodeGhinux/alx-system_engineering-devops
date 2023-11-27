#!/usr/bin/env bash
# using Puppet to make changes to our configuration file
file_line { 'no password':
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  ensure => present,
}
file_line { 'change private key':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
  ensure => present,
}