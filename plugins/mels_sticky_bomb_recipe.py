# ba_meta require api 8
import babase

# ba_meta export babase.Plugin
class MelsSecret(babase.Plugin):
    def on_app_running(self):
        babase.screenmessage(
            "Lo! The veil hath been lifted, uncovering "
            "the covert recipe of the volatile sticky bomb."
        )

    def has_settings_ui(self):
        return True

    def show_settings_ui(self, source_widget):
        babase.screenmessage(
            "Verily, the culinary alchemist, with deft hand "
            "and cunning mind, doth embark on a daring quest "
            "to amend the sacred recipe."
        )
