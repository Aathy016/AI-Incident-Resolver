import re


def parse_logs():

    logs=[]

    with open(
    "data/logs/application.log"
    ) as file:

        for line in file:

            match=re.search(
            r"(.*) ERROR (.*)",
            line
            )

            if match:

                logs.append(
                {
                "time":match.group(1),
                "error":match.group(2),
                "severity":"HIGH"
                }
                )

    return logs



if __name__=="__main__":

    result=parse_logs()

    for log in result:
        print(log)