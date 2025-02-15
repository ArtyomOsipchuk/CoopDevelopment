import argparse
import cowsay

parser = argparse.ArgumentParser(
                    prog='Twocows',
                    description='Cowsay with 2 cows',
                    epilog='Cows is cool.')

parser.add_argument('message1') # positional argument
parser.add_argument('message2') # positional argument
parser.add_argument('-e') #eye_string
parser.add_argument('-f') #cowfile
parser.add_argument('-n', action="store_true") 
parser.add_argument('-T') #tongue_string
parser.add_argument('-W') #column
parser.add_argument('-E') #eye_string
parser.add_argument('-F') #cowfile
parser.add_argument('-N', action="store_true") 
parser.add_argument('-b', action="store_true") 
parser.add_argument('-g', action="store_true") 
parser.add_argument('-p', action="store_true") 
parser.add_argument('-s', action="store_true") 
parser.add_argument('-t', action="store_true") 
parser.add_argument('-w', action="store_true") 
parser.add_argument('-y', action="store_true") 

args = parser.parse_args()
pr = ""
if args.b:
    pr += "b"
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
cow1 = cowsay.cowsay(args.message1,
    cow=args.f if args.f else 'default',
    preset=pr, eyes=args.e if args.e else 'oo',
    tongue=args.T if args.T else '  ',
    width=int(args.W) if args.W else 40,
    wrap_text=not args.n,
).split("\n")
cow2 = cowsay.cowsay(args.message2,
    cow=args.F if args.F else 'default',
    preset=pr, eyes=args.E if args.E else 'oo',
    tongue=args.T if args.T else '  ',
    width=int(args.W) if args.W else 40,
    wrap_text=not args.N,
).split('\n')
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
