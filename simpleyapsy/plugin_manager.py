class PluginManager(object):
    def __init__(self):
        self.plugins = []
        self.blacklisted_plugins = []

    def get_plugins(self):
        return self.plugins

    def blacklist_plugins(self, plugins):
        self.blacklisted_plugins.extend(plugins)

    def add_plugins(self, plugins):
        if not isinstance(plugins, list):
            plugins = [plugins]

        for plugin in plugins:
            if plugin not in self.blacklisted_plugins:
                self.plugins.append(plugin)

    def set_plugins(self, plugins):
        if not isinstance(plugins, list):
            plugins = [plugins]
        self.plugins = []

        for plugin in plugins:
            if plugin not in self.blacklisted_plugins:
                self.plugins.append(plugin)

    def get_active_plugins(self):
        active_plugins = []
        for plugin in self.plugins:
            if plugin.active:
                active_plugins.append(plugin)
        return active_plugins

    def deactivate_all_plugins(self):
        for plugin in self.plugins:
            plugin.deactivate()

    def activate_all_plugins(self):
        for plugin in self.plugins:
            plugin.activate()
