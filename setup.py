from setuptools import setup

setup(
    name='cycling-cap-server',
    version='0.0.1',
    packages=['base', 'venv.lib.python3.7.site-packages.jwt', 'venv.lib.python3.7.site-packages.jwt.contrib',
              'venv.lib.python3.7.site-packages.jwt.contrib.algorithms', 'venv.lib.python3.7.site-packages.cffi',
              'venv.lib.python3.7.site-packages.idna', 'venv.lib.python3.7.site-packages.pytz',
              'venv.lib.python3.7.site-packages.yaml', 'venv.lib.python3.7.site-packages.zope.dottedname',
              'venv.lib.python3.7.site-packages.empty', 'venv.lib.python3.7.site-packages.django',
              'venv.lib.python3.7.site-packages.django.db', 'venv.lib.python3.7.site-packages.django.db.models',
              'venv.lib.python3.7.site-packages.django.db.models.sql',
              'venv.lib.python3.7.site-packages.django.db.models.fields',
              'venv.lib.python3.7.site-packages.django.db.models.functions',
              'venv.lib.python3.7.site-packages.django.db.backends',
              'venv.lib.python3.7.site-packages.django.db.backends.base',
              'venv.lib.python3.7.site-packages.django.db.backends.dummy',
              'venv.lib.python3.7.site-packages.django.db.backends.mysql',
              'venv.lib.python3.7.site-packages.django.db.backends.oracle',
              'venv.lib.python3.7.site-packages.django.db.backends.sqlite3',
              'venv.lib.python3.7.site-packages.django.db.backends.postgresql',
              'venv.lib.python3.7.site-packages.django.db.backends.postgresql_psycopg2',
              'venv.lib.python3.7.site-packages.django.db.migrations',
              'venv.lib.python3.7.site-packages.django.db.migrations.operations',
              'venv.lib.python3.7.site-packages.django.apps', 'venv.lib.python3.7.site-packages.django.conf',
              'venv.lib.python3.7.site-packages.django.conf.urls',
              'venv.lib.python3.7.site-packages.django.conf.locale',
              'venv.lib.python3.7.site-packages.django.conf.locale.ar',
              'venv.lib.python3.7.site-packages.django.conf.locale.az',
              'venv.lib.python3.7.site-packages.django.conf.locale.bg',
              'venv.lib.python3.7.site-packages.django.conf.locale.bn',
              'venv.lib.python3.7.site-packages.django.conf.locale.bs',
              'venv.lib.python3.7.site-packages.django.conf.locale.ca',
              'venv.lib.python3.7.site-packages.django.conf.locale.cs',
              'venv.lib.python3.7.site-packages.django.conf.locale.cy',
              'venv.lib.python3.7.site-packages.django.conf.locale.da',
              'venv.lib.python3.7.site-packages.django.conf.locale.de',
              'venv.lib.python3.7.site-packages.django.conf.locale.el',
              'venv.lib.python3.7.site-packages.django.conf.locale.en',
              'venv.lib.python3.7.site-packages.django.conf.locale.eo',
              'venv.lib.python3.7.site-packages.django.conf.locale.es',
              'venv.lib.python3.7.site-packages.django.conf.locale.et',
              'venv.lib.python3.7.site-packages.django.conf.locale.eu',
              'venv.lib.python3.7.site-packages.django.conf.locale.fa',
              'venv.lib.python3.7.site-packages.django.conf.locale.fi',
              'venv.lib.python3.7.site-packages.django.conf.locale.fr',
              'venv.lib.python3.7.site-packages.django.conf.locale.fy',
              'venv.lib.python3.7.site-packages.django.conf.locale.ga',
              'venv.lib.python3.7.site-packages.django.conf.locale.gd',
              'venv.lib.python3.7.site-packages.django.conf.locale.gl',
              'venv.lib.python3.7.site-packages.django.conf.locale.he',
              'venv.lib.python3.7.site-packages.django.conf.locale.hi',
              'venv.lib.python3.7.site-packages.django.conf.locale.hr',
              'venv.lib.python3.7.site-packages.django.conf.locale.hu',
              'venv.lib.python3.7.site-packages.django.conf.locale.id',
              'venv.lib.python3.7.site-packages.django.conf.locale.is',
              'venv.lib.python3.7.site-packages.django.conf.locale.it',
              'venv.lib.python3.7.site-packages.django.conf.locale.ja',
              'venv.lib.python3.7.site-packages.django.conf.locale.ka',
              'venv.lib.python3.7.site-packages.django.conf.locale.km',
              'venv.lib.python3.7.site-packages.django.conf.locale.kn',
              'venv.lib.python3.7.site-packages.django.conf.locale.ko',
              'venv.lib.python3.7.site-packages.django.conf.locale.lt',
              'venv.lib.python3.7.site-packages.django.conf.locale.lv',
              'venv.lib.python3.7.site-packages.django.conf.locale.mk',
              'venv.lib.python3.7.site-packages.django.conf.locale.ml',
              'venv.lib.python3.7.site-packages.django.conf.locale.mn',
              'venv.lib.python3.7.site-packages.django.conf.locale.nb',
              'venv.lib.python3.7.site-packages.django.conf.locale.nl',
              'venv.lib.python3.7.site-packages.django.conf.locale.nn',
              'venv.lib.python3.7.site-packages.django.conf.locale.pl',
              'venv.lib.python3.7.site-packages.django.conf.locale.pt',
              'venv.lib.python3.7.site-packages.django.conf.locale.ro',
              'venv.lib.python3.7.site-packages.django.conf.locale.ru',
              'venv.lib.python3.7.site-packages.django.conf.locale.sk',
              'venv.lib.python3.7.site-packages.django.conf.locale.sl',
              'venv.lib.python3.7.site-packages.django.conf.locale.sq',
              'venv.lib.python3.7.site-packages.django.conf.locale.sr',
              'venv.lib.python3.7.site-packages.django.conf.locale.sv',
              'venv.lib.python3.7.site-packages.django.conf.locale.ta',
              'venv.lib.python3.7.site-packages.django.conf.locale.te',
              'venv.lib.python3.7.site-packages.django.conf.locale.th',
              'venv.lib.python3.7.site-packages.django.conf.locale.tr',
              'venv.lib.python3.7.site-packages.django.conf.locale.uk',
              'venv.lib.python3.7.site-packages.django.conf.locale.vi',
              'venv.lib.python3.7.site-packages.django.conf.locale.de_CH',
              'venv.lib.python3.7.site-packages.django.conf.locale.en_AU',
              'venv.lib.python3.7.site-packages.django.conf.locale.en_GB',
              'venv.lib.python3.7.site-packages.django.conf.locale.es_AR',
              'venv.lib.python3.7.site-packages.django.conf.locale.es_CO',
              'venv.lib.python3.7.site-packages.django.conf.locale.es_MX',
              'venv.lib.python3.7.site-packages.django.conf.locale.es_NI',
              'venv.lib.python3.7.site-packages.django.conf.locale.es_PR',
              'venv.lib.python3.7.site-packages.django.conf.locale.pt_BR',
              'venv.lib.python3.7.site-packages.django.conf.locale.sr_Latn',
              'venv.lib.python3.7.site-packages.django.conf.locale.zh_Hans',
              'venv.lib.python3.7.site-packages.django.conf.locale.zh_Hant',
              'venv.lib.python3.7.site-packages.django.core', 'venv.lib.python3.7.site-packages.django.core.mail',
              'venv.lib.python3.7.site-packages.django.core.mail.backends',
              'venv.lib.python3.7.site-packages.django.core.cache',
              'venv.lib.python3.7.site-packages.django.core.cache.backends',
              'venv.lib.python3.7.site-packages.django.core.files',
              'venv.lib.python3.7.site-packages.django.core.checks',
              'venv.lib.python3.7.site-packages.django.core.checks.security',
              'venv.lib.python3.7.site-packages.django.core.checks.compatibility',
              'venv.lib.python3.7.site-packages.django.core.servers',
              'venv.lib.python3.7.site-packages.django.core.handlers',
              'venv.lib.python3.7.site-packages.django.core.management',
              'venv.lib.python3.7.site-packages.django.core.serializers',
              'venv.lib.python3.7.site-packages.django.http', 'venv.lib.python3.7.site-packages.django.test',
              'venv.lib.python3.7.site-packages.django.urls', 'venv.lib.python3.7.site-packages.django.forms',
              'venv.lib.python3.7.site-packages.django.utils',
              'venv.lib.python3.7.site-packages.django.utils.translation',
              'venv.lib.python3.7.site-packages.django.views', 'venv.lib.python3.7.site-packages.django.views.generic',
              'venv.lib.python3.7.site-packages.django.views.decorators',
              'venv.lib.python3.7.site-packages.django.contrib', 'venv.lib.python3.7.site-packages.django.contrib.gis',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.models',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.models.sql',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.backends',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.backends.base',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.backends.mysql',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.backends.oracle',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.backends.postgis',
              'venv.lib.python3.7.site-packages.django.contrib.gis.db.backends.spatialite',
              'venv.lib.python3.7.site-packages.django.contrib.gis.gdal',
              'venv.lib.python3.7.site-packages.django.contrib.gis.gdal.raster',
              'venv.lib.python3.7.site-packages.django.contrib.gis.gdal.prototypes',
              'venv.lib.python3.7.site-packages.django.contrib.gis.geos',
              'venv.lib.python3.7.site-packages.django.contrib.gis.geos.prototypes',
              'venv.lib.python3.7.site-packages.django.contrib.gis.admin',
              'venv.lib.python3.7.site-packages.django.contrib.gis.forms',
              'venv.lib.python3.7.site-packages.django.contrib.gis.utils',
              'venv.lib.python3.7.site-packages.django.contrib.gis.geoip2',
              'venv.lib.python3.7.site-packages.django.contrib.gis.sitemaps',
              'venv.lib.python3.7.site-packages.django.contrib.gis.serializers',
              'venv.lib.python3.7.site-packages.django.contrib.auth',
              'venv.lib.python3.7.site-packages.django.contrib.auth.handlers',
              'venv.lib.python3.7.site-packages.django.contrib.auth.management',
              'venv.lib.python3.7.site-packages.django.contrib.auth.migrations',
              'venv.lib.python3.7.site-packages.django.contrib.admin',
              'venv.lib.python3.7.site-packages.django.contrib.admin.views',
              'venv.lib.python3.7.site-packages.django.contrib.admin.migrations',
              'venv.lib.python3.7.site-packages.django.contrib.admin.templatetags',
              'venv.lib.python3.7.site-packages.django.contrib.sites',
              'venv.lib.python3.7.site-packages.django.contrib.sites.migrations',
              'venv.lib.python3.7.site-packages.django.contrib.humanize',
              'venv.lib.python3.7.site-packages.django.contrib.humanize.templatetags',
              'venv.lib.python3.7.site-packages.django.contrib.messages',
              'venv.lib.python3.7.site-packages.django.contrib.messages.storage',
              'venv.lib.python3.7.site-packages.django.contrib.postgres',
              'venv.lib.python3.7.site-packages.django.contrib.postgres.forms',
              'venv.lib.python3.7.site-packages.django.contrib.postgres.fields',
              'venv.lib.python3.7.site-packages.django.contrib.postgres.aggregates',
              'venv.lib.python3.7.site-packages.django.contrib.sessions',
              'venv.lib.python3.7.site-packages.django.contrib.sessions.backends',
              'venv.lib.python3.7.site-packages.django.contrib.sessions.migrations',
              'venv.lib.python3.7.site-packages.django.contrib.sitemaps',
              'venv.lib.python3.7.site-packages.django.contrib.admindocs',
              'venv.lib.python3.7.site-packages.django.contrib.flatpages',
              'venv.lib.python3.7.site-packages.django.contrib.flatpages.migrations',
              'venv.lib.python3.7.site-packages.django.contrib.flatpages.templatetags',
              'venv.lib.python3.7.site-packages.django.contrib.redirects',
              'venv.lib.python3.7.site-packages.django.contrib.redirects.migrations',
              'venv.lib.python3.7.site-packages.django.contrib.staticfiles',
              'venv.lib.python3.7.site-packages.django.contrib.staticfiles.templatetags',
              'venv.lib.python3.7.site-packages.django.contrib.syndication',
              'venv.lib.python3.7.site-packages.django.contrib.contenttypes',
              'venv.lib.python3.7.site-packages.django.contrib.contenttypes.management',
              'venv.lib.python3.7.site-packages.django.contrib.contenttypes.migrations',
              'venv.lib.python3.7.site-packages.django.dispatch', 'venv.lib.python3.7.site-packages.django.template',
              'venv.lib.python3.7.site-packages.django.template.loaders',
              'venv.lib.python3.7.site-packages.django.template.backends',
              'venv.lib.python3.7.site-packages.django.middleware',
              'venv.lib.python3.7.site-packages.django.templatetags', 'venv.lib.python3.7.site-packages.jinja2',
              'venv.lib.python3.7.site-packages.certifi', 'venv.lib.python3.7.site-packages.chardet',
              'venv.lib.python3.7.site-packages.chardet.cli', 'venv.lib.python3.7.site-packages.coreapi',
              'venv.lib.python3.7.site-packages.coreapi.codecs', 'venv.lib.python3.7.site-packages.coreapi.transports',
              'venv.lib.python3.7.site-packages.MySQLdb', 'venv.lib.python3.7.site-packages.MySQLdb.constants',
              'venv.lib.python3.7.site-packages.pymysql', 'venv.lib.python3.7.site-packages.pymysql.constants',
              'venv.lib.python3.7.site-packages.urllib3', 'venv.lib.python3.7.site-packages.urllib3.util',
              'venv.lib.python3.7.site-packages.urllib3.contrib',
              'venv.lib.python3.7.site-packages.urllib3.contrib._securetransport',
              'venv.lib.python3.7.site-packages.urllib3.packages',
              'venv.lib.python3.7.site-packages.urllib3.packages.backports',
              'venv.lib.python3.7.site-packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.7.site-packages.guardian', 'venv.lib.python3.7.site-packages.guardian.conf',
              'venv.lib.python3.7.site-packages.guardian.testapp',
              'venv.lib.python3.7.site-packages.guardian.testapp.tests',
              'venv.lib.python3.7.site-packages.guardian.testapp.migrations',
              'venv.lib.python3.7.site-packages.guardian.management',
              'venv.lib.python3.7.site-packages.guardian.management.commands',
              'venv.lib.python3.7.site-packages.guardian.migrations',
              'venv.lib.python3.7.site-packages.guardian.templatetags', 'venv.lib.python3.7.site-packages.requests',
              'venv.lib.python3.7.site-packages.pycparser', 'venv.lib.python3.7.site-packages.pycparser.ply',
              'venv.lib.python3.7.site-packages.asn1crypto', 'venv.lib.python3.7.site-packages.asn1crypto._perf',
              'venv.lib.python3.7.site-packages.coreschema', 'venv.lib.python3.7.site-packages.coreschema.encodings',
              'venv.lib.python3.7.site-packages.markupsafe', 'venv.lib.python3.7.site-packages.simplejson',
              'venv.lib.python3.7.site-packages.simplejson.tests', 'venv.lib.python3.7.site-packages.uritemplate',
              'venv.lib.python3.7.site-packages.cryptography', 'venv.lib.python3.7.site-packages.cryptography.x509',
              'venv.lib.python3.7.site-packages.cryptography.hazmat',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.backends',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.backends.openssl',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.bindings',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.bindings.openssl',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.primitives',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.primitives.kdf',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.primitives.ciphers',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.primitives.twofactor',
              'venv.lib.python3.7.site-packages.cryptography.hazmat.primitives.asymmetric',
              'venv.lib.python3.7.site-packages.openapi_codec', 'venv.lib.python3.7.site-packages.rest_framework',
              'venv.lib.python3.7.site-packages.rest_framework.utils',
              'venv.lib.python3.7.site-packages.rest_framework.schemas',
              'venv.lib.python3.7.site-packages.rest_framework.authtoken',
              'venv.lib.python3.7.site-packages.rest_framework.authtoken.management',
              'venv.lib.python3.7.site-packages.rest_framework.authtoken.management.commands',
              'venv.lib.python3.7.site-packages.rest_framework.authtoken.migrations',
              'venv.lib.python3.7.site-packages.rest_framework.templatetags',
              'venv.lib.python3.7.site-packages.rest_framework_jwt',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.idna',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pytoml',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.certifi',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.chardet.cli',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.distlib._backport',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.msgpack',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.util',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.backports',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.colorama',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib._trie',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.filters',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treewalkers',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treeadapters',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.html5lib.treebuilders',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.lockfile',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.progress',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.requests',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.packaging',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.cachecontrol.caches',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.webencodings',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._vendor.pkg_resources',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.req',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.vcs',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.utils',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.models',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.commands',
              'venv.lib.python3.7.site-packages.pip-10.0.1-py3.7.egg.pip._internal.operations',
              'venv.lib.python3.7.site-packages.rest_framework_swagger',
              'venv.lib.python3.7.site-packages.django_rest_swagger_swaggerdoc',
              'venv.lib.python3.7.site-packages.django_rest_swagger_swaggerdoc.tests', 'entry', 'utils', 'common',
              'dictionary'],
    url='',
    license='MIT',
    author='Gucci Wu',
    author_email='gucciwu57@gmail.com',
    description='A Tour Designer',
    install_requires=['pymysql', 'django', 'djangorestframework', 'djangorestframework-jwt', 'googlemaps']
)
