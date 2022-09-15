class LB_Terminal():
    "The class for the terminal- Might as well be fancy and use a class instead of just using a constant loop. Makes readability easier too, ig"

    # Constructing ig
    def __init__(self, name, command):
        self.name = name
        self.command = command
    
    # All the basic terminal workings
    def enanet(self):
        "Enable remote connections via WiFi + ZeroTier. Allows remote access via SSH."
    
    def disnet(self):
        "Disable remote connections via WiFi + ZeroTier."

    def signout(self):
        "Signout of current LOCKBOX session, re-lock 2FA, re-encrypt and delete decrypted files, and run `DISNET()` automatically."

    def ssh(self):
        "Check the number of SSH connections, their identities, and locations."

    def ssh_term(self):
        "Terminates all active SSH sessions."

    def rem_2fa(self):
        "Whether remote 2FA while `ENANET()` is active is allowed. Takes one of two parameters: `True` and `False`. `False` by default."