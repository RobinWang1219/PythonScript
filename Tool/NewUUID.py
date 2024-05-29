import uuid
import sys

# make a random UUID
sys.stdout.write(str(uuid.uuid4()).upper())