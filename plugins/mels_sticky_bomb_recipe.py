# ba_meta require api 7
import ba

# ba_meta export plugin
class MelsSecret(ba.Plugin):
    def on_app_running(self):
        ba.screenmessage(
            "Lo! The veil hath been lifted, uncovering "
            "the covert recipe of the volatile sticky bomb."
        )
