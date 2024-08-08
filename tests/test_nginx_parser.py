import unittest
from pprint import pprint  # For better output formatting

from kobozo_crossplane.nginx_parser import loads as nginx_parser_loads


class TestNginxParser(unittest.TestCase):
    """Test suite for NginxParser."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.config_text = """
        user www-data;
        worker_processes auto;

        error_log /var/log/nginx/error.log;
        pid /run/nginx.pid;

        events {
            worker_connections 1024;
        }

        http {
            sendfile on;
            tcp_nopush on;
            tcp_nodelay on;
            keepalive_timeout 65;
            types_hash_max_size 2048;

            include /etc/nginx/mime.types;
            default_type application/octet-stream;

            access_log /var/log/nginx/access.log;
            error_log /var/log/nginx/error.log;

            gzip on;
            gzip_disable "msie6";

            server {
                listen 80;
                server_name example.com www.example.com;

                root /var/www/html;

                index index.html index.htm;

                location / {
                    access_by_lua_block {
                        local header_map = {
                            Authorization = "credential.attributes['common|authz_header']",
                            x_tb_session  = ''
                        }
                        require("trustbuilder-gateway.protect").web_app(header_map)
                    }
                    try_files $uri $uri/ =404;
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header X-Forwarded-Proto $scheme;
                    set var1 "value1{";
                }

                error_page 404 /404.html;

                error_page 500 502 503 504 /50x.html;

                location ~ /\\.ht {
                    deny all;
                }

                location ~* ^/location/case/insensitive {
                    deny all;
                }

                location /on-one-line {
                    set $var value;
                }

                add_header X-Frame-Options "SAMEORIGIN";
                add_header X-Content-Type-Options "nosniff";
                add_header X-XSS-Protection "1; mode=block";
            }
        }
        """
        # Expected JSON-like dictionary structure from the config_text
        self.expected_result = {
            "user": "www-data",
            "worker_processes": "auto",
            "error_log": "/var/log/nginx/error.log",
            "pid": "/run/nginx.pid",
            "events": [
                {
                    "worker_connections": "1024",
                },
            ],
            "http": [
                {
                    "sendfile": "on",
                    "tcp_nopush": "on",
                    "tcp_nodelay": "on",
                    "keepalive_timeout": "65",
                    "types_hash_max_size": "2048",
                    "include": "/etc/nginx/mime.types",
                    "default_type": "application/octet-stream",
                    "access_log": "/var/log/nginx/access.log",
                    "error_log": "/var/log/nginx/error.log",
                    "gzip": "on",
                    "gzip_disable": "msie6",
                    "server": [
                        {
                            "listen": "80",
                            "server_name": "example.com www.example.com",
                            "root": "/var/www/html",
                            "index": "index.html index.htm",
                            "location": [
                                {
                                    "args": ["/"],
                                    "access_by_lua_block": [
                                        (
                                            "local header_map = { "
                                            "Authorization = "
                                            '"credential.attributes[\'common|authz_header\']", '
                                            "x_tb_session  = '' "
                                            "} "
                                            'require("trustbuilder-gateway.protect").web_app(header_map)'
                                        ),
                                    ],
                                    "try_files": "$uri $uri/ =404",
                                    "proxy_set_header": {
                                        "Host": ["$host"],
                                        "X-Real-IP": ["$remote_addr"],
                                        "X-Forwarded-For": ["$proxy_add_x_forwarded_for"],
                                        "X-Forwarded-Proto": ["$scheme"],
                                    },
                                    "set": {
                                        "var1": ["value1{"],
                                    },
                                },
                                {
                                    "args": ["~", "/\\.ht"],
                                    "deny": "all",
                                },
                                {
                                    "args": ["~*", "^/location/case/insensitive"],
                                    "deny": "all",
                                },
                                {
                                    "args": ["/on-one-line"],
                                    "set": {
                                        "$var": ["value"],
                                    },
                                },
                            ],
                            "error_page": {
                                "404": "/404.html",
                                "500": "/50x.html",
                                "502": "/50x.html",
                                "503": "/50x.html",
                                "504": "/50x.html",
                            },
                            "add_header": {
                                "X-Frame-Options": ["SAMEORIGIN"],
                                "X-Content-Type-Options": ["nosniff"],
                                "X-XSS-Protection": ["1; mode=block"],
                            },
                        },
                    ],
                },
            ],
        }

    def test_parse_nginx_config(self) -> None:
        """Test parsing of a sample NGINX configuration."""
        result = nginx_parser_loads(self.config_text)
        # Use pprint for better readability of output during debugging
        pprint(result)
        self.assertDictEqual(result, self.expected_result)


if __name__ == "__main__":
    unittest.main()
