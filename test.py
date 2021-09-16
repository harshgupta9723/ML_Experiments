import pandas as pd
import pyarrow as pa
import redis

data = pd.read_csv("user.csv")

df = pd.DataFrame({
    "key": data["key"],
    "userfeedback": data["userfeedback"]
})

# print(df.head())

r = redis.Redis(host='localhost', port=6379, db=0)

context = pa.default_serialization_context()
r.set("key", context.serialize(df).to_buffer().to_pybytes())
print(
    context.deserialize(r.get("key"))
)
