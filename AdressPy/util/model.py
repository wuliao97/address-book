from typing import Union
import phonenumbers
import re


def phone_num_check(num: str):
    pattern = re.compile(r'\D+')
    num = re.sub(pattern, '', num)

    if len(str(num)) > 9:
        country_list = ['JP', 'CN', 'IN', 'US', 'ID', 'PK', 'BR', 'NG', 'BD', 'RU', 'MX', 'PH', 'ET', 'EG',
                        'VN', 'DE', 'IR', 'TR', 'CD', 'TH', 'FR', 'GB', 'IT', 'ZA', 'MM', 'KE', 'KR', 'CO',
                        'ES', 'UA', 'TZ', 'AR', 'UG', 'PL', 'CA', 'AF', 'MY', 'MA', 'PE', 'UZ', 'VE', 'SA',
                        'GH', 'YE', 'NP', 'MM', 'KR', 'JP', 'NG', 'BD', 'RU', 'MX', 'PH', 'VN', 'ET', 'EG',
                        'DE', 'TR', 'TH', 'GB', 'FR', 'IT', 'MM', 'ZA', 'KE', 'CO', 'ES', 'UA', 'AR', 'TZ',
                        'UG', 'PL', 'AF', 'CA', 'MA', 'UZ', 'PE', 'VE', 'MY', 'GH', 'YE', 'NP', 'MM', 'SA',
                        'AU', 'CI', 'CM', 'MM', 'KE', 'SD', 'UA', 'UG', 'DZ', 'PL', 'CA', 'MA', 'AF', 'MY',
                        'UZ', 'VE', 'PE', 'GH', 'MM', 'NP', 'CI', 'CM', 'SD', 'AU']
        for i in country_list:
            phone_number = phonenumbers.parse(num, i)
            if phonenumbers.is_valid_number(phone_number):
                return re.sub(pattern, '', phonenumbers.format_number(phonenumbers.parse(num, i),
                                                                      phonenumbers.PhoneNumberFormat.NATIONAL))
    return ""


class AddrStd:
    name: str
    phone_number: str
    address_line: str
    city: str
    region: str
    country: str
    post_code: int

    def __init__(self,
                 name: str,
                 phone_number: str,
                 address_line: str,
                 city: str,
                 region: str,
                 country: str,
                 post_code: str,
                 ):
        self.name = name
        self.phone_number = phone_num_check(phone_number)
        self.address_line = address_line
        self.city = city
        self.region = region
        self.country = country
        self.post_code = int(post_code.replace("-", "").replace(" ", ""))


# class AddrExt:
#     name: str
#     phone_number: int
#     address_line: str
#     city: str
#     region: str
#     country: str
#     post_code: int


AddrType = Union[
    AddrStd,
    # AddrExt
]
