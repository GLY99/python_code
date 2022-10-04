def get_formatted_name(first: str, last: str) -> str:
    """
    生成整洁的名字
    :param first: 姓
    :param last: 名
    :return: 格式化后的名字
    """
    full_name = f"{first} {last}"
    return full_name.title()