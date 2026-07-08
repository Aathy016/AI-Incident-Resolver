import random
from datetime import datetime


errors=[
"Database connection timeout",
"Memory limit exceeded",
"Kubernetes pod crashed",
"CPU utilization above threshold",
"Application service unavailable"
]


with open("data/logs/application.log","w") as file:

    for i in range(20):

        error=random.choice(errors)

        file.write(
        f"{datetime.now()} ERROR {error}\n"
        )


print("Logs Generated")