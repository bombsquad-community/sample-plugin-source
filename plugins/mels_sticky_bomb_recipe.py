# ba_meta require api 7
import ba

# ba_meta export plugin
class MelsSecret(ba.Plugin):
    def on_app_running(self):
        ba.screenmessage(
            "Lo! The veil hath been lifted, uncovering "
            "the covert recipe of the volatile sticky bomb."
        )

    def has_settings_ui(self):
        return True

    def show_settings_ui(self, source_widget):
        ba.screenmessage(
            "Verily, the culinary alchemist, with deft hand "
            "and cunning mind, doth embark on a daring quest "
            "to amend the sacred recipe."
        )
