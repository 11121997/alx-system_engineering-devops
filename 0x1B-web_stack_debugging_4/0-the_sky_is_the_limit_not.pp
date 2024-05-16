#testing how well our web server setup featuring Nginx is doing under pressure
#fix our stack so that we get to 0

exec { 'fix--for-nginx':
  command => '/usr/bin/env sed -i s/15/2000/ /etc/nginx/nginx.conf; sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
