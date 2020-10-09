# fixes number of simultaneous requests for NGINX
exec { 'fix':
  path    => ['/usr/bin/', '/bin/', '/sbin', '/usr/sbin/'],
  command => 'echo ULIMIT=\" -n 1000\" >> /etc/default/nginx',
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
