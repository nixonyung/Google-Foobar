import base64
from itertools import cycle

message = "FU4LGg0aEB0UFhIJTk4fHQsYAUlLERVQAQUUCg8eAAtAEQgTSQwLGwscGAsDFh4TSQweCQELAR1AEQgTSQAWDBwcEQcFXVcUQklfDg0RHAsRVF9WAB1fT1RZUhsJXV1QBQwcSEJZUhwGU1BaGhpfT1RZUh0GV1cUQklfCQEWUk5dERVEBwdZSBM="

key = bytes("nixonyung123", "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))
