# kills process named killmenow
exec { 'killkillmenow':
  command  => 'pkill killmenow',
  provider => shell,
}
