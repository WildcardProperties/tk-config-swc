# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook that gets executed every time an engine has been fully initialized.
"""

from tank import Hook
import sentry_sdk

class EngineInit(Hook):
    def execute(self, engine, **kwargs):
        """
        Executed when a Toolkit engine has been fully initialized.

        At this point, all apps and frameworks have been loaded,
        and the engine is fully operational.

        The default implementation does nothing.

        :param engine: Engine that has been initialized.
        :type engine: :class:`~sgtk.platform.Engine`
        """

        config_release = f'{self.sgtk.configuration_descriptor.system_name}@{self.sgtk.configuration_descriptor.version}'
        if self.sgtk.configuration_descriptor.is_dev():
            config_env = "dev"
        else:
            config_env = "production"

        sentry_sdk.init(
            dsn="https://ead63d02fd9544c091baf83427e649da@o339527.ingest.sentry.io/4504868950179840",

            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=1.0,
            release=config_release,
            environment=config_env
        )

        sentry_sdk.set_user({"email": "self.sgtk.get_authenticated_user()"})

        # Give a bunch of tags to Sentry
        engine_metrics = engine.get_metrics_properties()

        sentry_sdk.set_tag("engine", engine_metrics['Engine'])
        sentry_sdk.set_tag("engine.version", engine_metrics['Engine Version'])
        sentry_sdk.set_tag("engine.host_app", engine_metrics['Host App'])
        sentry_sdk.set_tag("engine.host_app_version", engine_metrics['Host App Version'])

        if engine.name == "tk-maya":
            self.logger.info("Custom Maya Init Hook")
            import maya.cmds as cmds
            try:
                cmds.loadPlugin("wc_sgias.py")
            except RuntimeError:
                self.logger.info("Wildcard Tools not found while initializing engine.")
        pass
