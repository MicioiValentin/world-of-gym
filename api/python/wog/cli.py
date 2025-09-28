import argparse
from wog.progression import set_xp, apply_xp, xp_to_next
from wog.weight_classes import classify

def main():
    p = argparse.ArgumentParser(prog="wog-cli", description="World of Gym CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("set-xp", help="Compute XP for a set")
    s.add_argument("--reps", type=int, required=True)
    s.add_argument("--weight", type=float, required=True)
    s.add_argument("--level", type=int, required=True)

    a = sub.add_parser("apply-xp", help="Apply gained XP")
    a.add_argument("--level", type=int, required=True)
    a.add_argument("--xp", type=int, required=True)
    a.add_argument("--gained", type=int, required=True)

    n = sub.add_parser("next", help="XP to next level")
    n.add_argument("--level", type=int, required=True)

    c = sub.add_parser("classify", help="Classify weight class")
    c.add_argument("--bw", type=float, required=True)

    args = p.parse_args()

    if args.cmd == "set-xp":
        print(set_xp(args.reps, args.weight, args.level))
    elif args.cmd == "apply-xp":
        print(*apply_xp(args.level, args.xp, args.gained))
    elif args.cmd == "next":
        print(xp_to_next(args.level))
    elif args.cmd == "classify":
        print(classify(args.bw))

if __name__ == "__main__":
    main()
