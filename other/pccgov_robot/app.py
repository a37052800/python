import configparser, time
from datetime import datetime
from search_client import Client


def read_config(config_file="e:\github\python\other\pccgov_robot\config.ini"):
    config = configparser.ConfigParser()
    with open(config_file, "r", encoding="utf-8") as f:
        config.read_file(f)
    return config["DEFAULT"]


def main():
    try:
        config = read_config()

        org_name = config.get("org_name")
        tender_name = config.get("tender_name")
        start_date = config.get("start_date")
        end_date = config.get("end_date")
        execution_interval = config.getint("execution_interval")

        client = Client(org_name, tender_name, start_date, end_date)
        client.search()

        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 已完成搜尋標案資訊"
        )

    except Exception as e:
        print(f"發生錯誤: {e}")


if __name__ == "__main__":
    main()
