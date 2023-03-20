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
Hook that gets executed every time a new PipelineConfiguration instance is created.
"""

from tank import Hook
import sys, os

class PipelineConfigurationInit(Hook):
    def execute(self, **kwargs):
        """
        Executed when a new PipelineConfiguration instance is initialized.

        The default implementation does nothing.
        """

        sys.path.append(os.path.join(os.path.dirname(os.path.dirname(self.disk_location)), "resources", "python", "core"))
        # extra_modules_path = os.path.join(os.path.dirname(os.path.dirname(self.disk_location)), "resources", "python")
        # self.add_module_folders(extra_modules_path)

        pass

    # def add_module_folders(self, path):
    #     for entry in os.listdir(path):
    #         dir_path = os.path.join(path, entry)
    #         if os.path.isdir(dir_path) and dir_path not in sys.path:
    #             sys.path.append(dir_path)