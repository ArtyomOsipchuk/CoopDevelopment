import argparse
import shlex
import cmd
import cowsay

class Twocows(cmd.Cmd):
    prompt = "twocows>> "
    parser = argparse.ArgumentParser(
            prog='twocows',
            description='cowsay or cowthink with 2 cows',
            epilog='Cows are cool!')
    parser.add_argument('message', type=str, help='message 1') # positional argument
    parser.add_argument('-e', type=str, default='oo', help='eyes of first cow') #eye_string
    parser.add_argument('-f', type=str, default='default', help='first special cow') #cowfile
    parser.add_argument('-n', action="store_true")
    parser.add_argument('-T', type=str, default='  ', help='tongue string') #tongue_string
    parser.add_argument('-W', type=int, default=40, help='column width') #column
    parser.add_argument('-b', action="store_true", help='borg == eyes')
    parser.add_argument('-d', action="store_true", help='dead XX eyes')
    parser.add_argument('-g', action="store_true", help='greedy $$ eyes')
    parser.add_argument('-p', action="store_true", help='paranoid @@ eyes')
    parser.add_argument('-s', action="store_true", help='stoned ** eyes')
    parser.add_argument('-t', action="store_true", help='tired -- eyes')
    parser.add_argument('-w', action="store_true", help='wired OO eyes')
    parser.add_argument('-y', action="store_true", help='young .. eyes')

    def _draw_cows(self, cow1, cow2):
        cow1 = cow1.split('\n')
        cow2 = cow2.split('\n')
        wid = max(len(i) for i in cow1 + cow2)
        sh = len(cow1) - len(cow2)
        if sh > 0:
            for i in range(sh):
                cow2.insert(0, ' ' * wid)
        elif sh < 0:
            for i in range(-sh):
                cow1.insert(0, ' ' * wid)
        for i in range(len(cow1)):
            print(cow1[i].ljust(wid) + cow2[i])

    def do_EOF(self, args):
        'End Of File'
        return 1

    def do_list_cows(self, args):
        'List of available cows'
        print(*cowsay.list_cows())
    
    def do_make_bubble(self, args):
        'Return speech bubble. Usage: make_bubble <text>'
        args = shlex.split(args)
        if not args:
            print("Usage: make_bubble <text>")
        else:
            print(cowsay.make_bubble(args[0]))

    def do_cowsay(self, args):
        'Two cows talking. Usage: cowsay [params for cow1, check -h] message1 reply [params for cow2] message2'
        shargs = shlex.split(args)
        try:
            if 'reply' not in shargs:
                raise SystemExit('Usage: cowthink [params for cow1, check -h] message1 reply [params for cow2] message2')
            args = self.parser.parse_args(args=shargs[:shargs.index('reply')]) 
            pr = ""
            if args.b:
                pr += "b"
            if args.d:
                pr += "d"
            if args.g:
                pr += "g"
            if args.p:
                pr += "p"
            if args.s:
                pr += "s"
            if args.t:
                pr += "t"
            if args.w:
                pr += "w"
            if args.y:
                pr += "y"
            cow1 = cowsay.cowsay(args.message,
                cow=args.f,
                preset=pr,
                eyes=args.e,
                tongue=args.T,
                width=args.W,
                wrap_text=not args.n,
            )
            args = self.parser.parse_args(args=shargs[shargs.index('reply') + 1:]) 
            pr = ""
            if args.b:
                pr += "b"
            if args.d:
                pr += "d"
            if args.g:
                pr += "g"
            if args.p:
                pr += "p"
            if args.s:
                pr += "s"
            if args.t:
                pr += "t"
            if args.w:
                pr += "w"
            if args.y:
                pr += "y"
            cow2 = cowsay.cowsay(args.message,
                cow=args.f,
                preset=pr,
                eyes=args.e,
                tongue=args.T,
                width=args.W,
                wrap_text=not args.n,
            )
            self._draw_cows(cow1, cow2)
        except SystemExit as e:
            print(e)
        except Exception as e:
            print(e)

    def do_cowthink(self, args):
        'Two cows thinking. Usage: cowthink [params for cow1, check -h] message1 reply [params for cow2] message2'
        shargs = shlex.split(args)
        try:
            if 'reply' not in shargs:
                raise SystemExit('Usage: cowthink [params for cow1, check -h] message1 reply [params for cow2] message2')
            args = self.parser.parse_args(args=shargs[:shargs.index('reply')]) 
            pr = ""
            if args.b:
                pr += "b"
            if args.d:
                pr += "d"
            if args.g:
                pr += "g"
            if args.p:
                pr += "p"
            if args.s:
                pr += "s"
            if args.t:
                pr += "t"
            if args.w:
                pr += "w"
            if args.y:
                pr += "y"
            cow1 = cowsay.cowthink(args.message,
                cow=args.f,
                preset=pr,
                eyes=args.e,
                tongue=args.T,
                width=args.W,
                wrap_text=not args.n,
            )
            args = self.parser.parse_args(args=shargs[shargs.index('reply') + 1:]) 
            pr = ""
            if args.b:
                pr += "b"
            if args.d:
                pr += "d"
            if args.g:
                pr += "g"
            if args.p:
                pr += "p"
            if args.s:
                pr += "s"
            if args.t:
                pr += "t"
            if args.w:
                pr += "w"
            if args.y:
                pr += "y"
            cow2 = cowsay.cowthink(args.message,
                cow=args.f,
                preset=pr,
                eyes=args.e,
                tongue=args.T,
                width=args.W,
                wrap_text=not args.n,
            )
            self._draw_cows(cow1, cow2)
        except SystemExit as e:
            print(e)
        except Exception as e:
            print(e)
    
    def complete_cowsay(self, text, line, begidx, endidx):
        words = (line[:endidx] + ".").split()
        DICT = []
        if words[-2] == '-f':
            DICT = cowsay.list_cows()
        return [c for c in DICT if c.startswith(text)]

    def complete_cowthink(self, text, line, begidx, endidx):
        return self.complete_cowsay(text, line, begidx, endidx)

if __name__ == '__main__':
    Twocows().cmdloop()
