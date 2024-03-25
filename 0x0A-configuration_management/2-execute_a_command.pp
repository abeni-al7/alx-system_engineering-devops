# Executes kill
exec {'killmenow':
  command => 'pkill -f killmenow',
}
