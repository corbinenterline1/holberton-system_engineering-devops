exec { 'fixdapheeps':
  path    => [ '/bin/', '/usr/bin/', '/sbin/' ],
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
