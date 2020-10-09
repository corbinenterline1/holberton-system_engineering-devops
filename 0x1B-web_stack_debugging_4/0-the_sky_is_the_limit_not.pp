# fixes number of simultaneous requests for NGINX
exec { 'fix':
  path    => ['/usr/bin/', '/bin/', '/sbin', '/usr/sbin/'],
  command => "sed -i '5c ULIMIT=\"-n 3000\"' && sudo service nginx restart"
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
