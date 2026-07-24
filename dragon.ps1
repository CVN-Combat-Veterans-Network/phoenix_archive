import sys
import datetime
import os

DRAGON_REGISTRY = {}

def dragon_register_head(name, verbs):
    DRAGON_REGISTRY[name] = verbs

def runid_auto():
    return datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%SZ")

def HA_81__seal_plate(args):
    name = args[0]
    runid = args[1] if len(args) > 1 else runid_auto()

    archive_dir = os.path.join("archives", runid)
    os.makedirs(archive_dir, exist_ok=True)

    return f"[HA_81_] Sealed plate {name} into {archive_dir}"

dragon_register_head("HA_81_", {
    "seal plate": HA_81__seal_plate,
})

def dragon_dispatch(argv):
    if len(argv) < 2:
        raise ValueError("Usage: dragon <head> <verb> [args...]")

    head = argv[0]
    verb = " ".join(argv[1:3]) if len(argv) > 2 else argv[1]

    if head not in DRAGON_REGISTRY:
        raise ValueError(f"Unknown Dragon head: {head}")

    verbs = DRAGON_REGISTRY[head]

    if verb not in verbs:
        raise ValueError(f"Unknown verb '{verb}' for head '{head}'")

    handler = verbs[verb]
    return handler(argv[3:])

if __name__ == "__main__":
    result = dragon_dispatch(sys.argv[1:])
    print(result)