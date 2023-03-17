import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": "OAuth " + self.token}
        params = {"path": "/" + file_path.split("/")[-1]}
        response = requests.get(url, headers=headers, params=params)

        href = response.json().get("href", "")
        if not href:
            print("Ошибка, не получили URL")
            return False

        with open(file_path, "rb") as f:
            response = requests.put(href, data=f)

        if response.status_code != 201:
            print("Ошибка при загрузке файла")
            return False

        print("Файл успешно загружен")
        return True


if __name__ == "__main__":
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите OAuth token: ")
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# С помощью библиотеки yadisk
# import yadisk


# if __name__ == '__main__':
#     ya = yadisk.YaDisk(token="....")
    # ya.upload("test", "/text.txt")