# ba_meta require api 8
import babase

# ba_meta export babase.Plugin
class Cyborgian(babase.Plugin):
    def on_app_running(self):
        babase.screenmessage(
            "I'm an experimental cyborg undergoing scientific research."
        )

    def has_settings_ui(self):
        return True

    def show_settings_ui(self, source_widget):
        babase.screenmessage(
            "Once I'm ready, you can add new or rip apart my existing "
            "modules modules here."
        )
