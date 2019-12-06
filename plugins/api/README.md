Api: QGIS Server Plugin to call the QGIS server api
=================================================================================

Description
-----------

This plugin adds a new request to QGIS Server `api` which allows to 

Installation
------------

We assume you have a fully functionnal QGIS Server.
See https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/index.html

We need to download the plugin, and tell QGIS Server where the plugins are stored, the reload the web server.
For example on Debian:

```
# Create needed directory to store plugins
mkdir -p /srv/qgis/plugins

# Get last version
cd /srv/qgis/plugins
wget "https://github.com/gem/oq-qgis-server-plugins/archive/master.zip"
unzip master.zip
mv oq-qgis-server-plugins-master/plugins/api api

# Make sure correct environment variables are set in your web server configuration
# for example in Apache2 with mod_fcgid
nano /etc/apache2/mods-available/fcgid.conf
FcgidInitialEnv QGIS_PLUGINPATH "/srv/qgis/plugins/"

# Reload server, for example with Apache2
service apache2 reload
```

You can now test your installation
