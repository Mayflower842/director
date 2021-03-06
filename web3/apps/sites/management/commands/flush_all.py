# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from web3.apps.sites.models import Site
from web3.apps.sites.helpers import make_site_dirs, fix_permissions, reload_services, reload_nginx_config, create_config_files


class Command(BaseCommand):
    help = "Rewrite all site configurations and reset all permissions"

    def add_arguments(self, parser):
        parser.add_argument('--no-permissions', action='store_true', dest='noperms', default=False, help="Don't reset permissions.")
        parser.add_argument('--no-config', action='store_true', dest='noconfig', default=False, help="Don't create configuration files.")

    def handle(self, **options):
        for site in Site.objects.all():
            make_site_dirs(site)
            if not options["noperms"]:
                fix_permissions(site)
            if not options["noconfig"]:
                create_config_files(site)
            self.stdout.write("Finished {}".format(site.name))
        reload_services()
        reload_nginx_config()
