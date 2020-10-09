# fixes number of simultaneous requests for NGINX
exec { 'fix':
  path    => ['/usr/bin/', '/bin/'],
  command => "sed -i 's/15/3000/g' /etc/default/nginx"
}
exec { 'restart':
  provider => 'shell',
  command  => 'sudo service nginx restart'
}
