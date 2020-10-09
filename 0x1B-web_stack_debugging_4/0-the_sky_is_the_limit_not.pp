# fixes number of simultaneous requests for NGINX
exec { 'reqfix':
  path    => ['/usr/bin/', '/bin/'],
  command => 'echo ULIMIT=\"-n 4096\" >> /etc/default/nginx',
}
exec { 'always':
  provider => 'shell',
  command  => 'sudo service nginx restart',
}
