
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data



def main():
    OPERATION_URL = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc" \
                    "/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz" \
                    "-Credential=AKIAT73L2G45EIPT3X45%2F20230208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date" \
                    "=20230208T131534Z&X-Amz-Expires=86400&X-Amz-Signature" \
                    "=4cd83dd9ab064d1ed2695b2117a467d14bced9d36853e35910890093ed7b4ae3&X-Amz-SignedHeaders=host" \
                    "&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject "


    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5
    data, info = get_data(OPERATION_URL)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filtered_data(data,  filtered_empty_from=FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_LAST_WALUES)
    data = get_formatted_data(data)

    print("INFO: Вывод данных")
    for row in data:
        print(row, end='\n\n')



if __name__ == "__main__":
    main()
