
from cmdr import Cmdr, Command, subcmd

class Echo1(Command):
    """A simple Echo Command as a basic subclass"""
    def execute(self, *args):
        print "Echo1!"
        print args[0]

class Echo2(Command):
    """echo2 - a simple echo command.
    \t\t\tAvailable subcommands:
    \t\t\t\techo carets
    \t\t\t\techo stars <args>
    """
    @subcmd
    def stars(self):
        print "****Echo2: stars() ****"

    @subcmd
    def carets(self, *args):
        print "^^^^Echo2: carets() ^^^^"
        if not args:
            raise TypeError("carets() takes at least 1 argument (%s given)" % len(args))
        print args[0]

    def execute(self):
        print self.__doc__

app = Cmdr(__name__, registered_commands=[Echo1(), Echo2()])

@app.cmd("echo3")
def echo3(*args):
    print "Echo3"
    print args[0]

app.start()
